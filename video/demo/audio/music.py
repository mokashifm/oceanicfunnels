import numpy as np,soundfile as sf
SR=44100;BPM=112;beat=60/BPM;DUR=66.5
N=int(SR*DUR);L=np.zeros(N);R=np.zeros(N)
rng=np.random.default_rng(7)
def midi(m):return 440*2**((m-69)/12)
def add(buf,start,sig,g=1.0):
    i=int(start*SR);j=min(N,i+len(sig))
    if i<N: buf[i:j]+=sig[:j-i]*g
def env(n,a,d,s=0,r=0):
    t=np.arange(n)/SR;e=np.minimum(1,t/max(a,1e-4))*np.exp(-t/d) if s==0 else np.minimum(1,t/a)
    return e
def lp(x,c):  # one-pole lowpass
    a=np.exp(-2*np.pi*c/SR);y=np.zeros_like(x);acc=0.
    from scipy.signal import lfilter
    return lfilter([1-a],[1,-a],x)
from scipy.signal import lfilter
# progression: F G Em Am (in C), 1 bar each (4 beats)
prog=[[53,57,60,64],[55,59,62,65],[52,55,59,62],[57,60,64,67]]
bass=[41,43,40,45]
bar=4*beat
nbars=int(DUR/bar)+1
def saw(f,n,det=0):
    t=np.arange(n)/SR;return 2*((t*f*(1+det))%1)-1
for b in range(nbars):
    t0=b*bar;ch=prog[b%4]
    # section energy
    sec = 0 if t0<3.2 else (1 if t0<59.0 else 2)
    # pad
    n=int(bar*SR)+int(.6*SR)
    pad=np.zeros(n)
    for m in ch:
        f=midi(m+12)
        for d in (-.004,0,.004): pad+=saw(f,n,d)
    pad=lfilter([1-np.exp(-2*np.pi*1400/SR)],[1,-np.exp(-2*np.pi*1400/SR)],pad)
    tt=np.arange(n)/SR;pe=np.minimum(1,tt/.25)*np.minimum(1,np.maximum(0,(bar+.6-tt)/.6))
    g=0.018 if sec!=1 else 0.014
    add(L,t0,pad*pe,g);add(R,t0+.012,pad*pe,g)
    if sec==0:continue
    # bass (8ths)
    for k in range(8):
        n=int(beat/2*SR);tt=np.arange(n)/SR
        f=midi(bass[b%4]-12+ (12 if k in (3,7) else 0))
        s=np.sin(2*np.pi*f*tt)+.3*np.sin(4*np.pi*f*tt)
        s*=np.minimum(1,tt/.005)*np.exp(-tt/.18)
        add(L,t0+k*beat/2,s,.16);add(R,t0+k*beat/2,s,.16)
    if sec==2 and t0>62:continue
    # pluck arpeggio 16ths
    pat=[0,2,1,3,2,1,3,2]*2
    for k in range(16):
        m=ch[pat[k]]+24;n=int(.35*SR);tt=np.arange(n)/SR;f=midi(m)
        s=(np.sin(2*np.pi*f*tt)+.25*np.sin(2*np.pi*2*f*tt)+.1*np.sin(2*np.pi*3*f*tt))*np.minimum(1,tt/.002)*np.exp(-tt/.09)
        pan=.5+.35*np.sin(k*.7)
        add(L,t0+k*beat/4,s,.05*(1-pan)*2*.6);add(R,t0+k*beat/4,s,.05*pan*2*.6)
    # drums
    for k in range(4):
        tb=t0+k*beat
        n=int(.35*SR);tt=np.arange(n)/SR
        f=50+90*np.exp(-tt/.03);ph=2*np.pi*np.cumsum(f)/SR
        kick=np.sin(ph)*np.exp(-tt/.12)
        add(L,tb,kick,.42);add(R,tb,kick,.42)
        if k in(1,3):
            n=int(.25*SR);tt=np.arange(n)/SR
            cl=rng.standard_normal(n);cl=lfilter([1,-1],[1,-.6],cl)*np.exp(-tt/.06)
            add(L,tb,cl,.05);add(R,tb+.004,cl,.05)
        for h in (0,.5):
            n=int(.06*SR);tt=np.arange(n)/SR
            hh=lfilter([1,-1],[1],rng.standard_normal(n))*np.exp(-tt/.015)
            gg=.02 if h else .012
            add(L,tb+h*beat,hh,gg*1.1);add(R,tb+h*beat,hh,gg*.9)
# riser into 3.2s
n=int(3.0*SR);tt=np.arange(n)/SR
ri=lfilter([1],[1,-.95],rng.standard_normal(n))*(tt/3.0)**2*.02
add(L,.25,ri);add(R,.25,ri)
# simple reverb
ir_n=int(1.8*SR);tt=np.arange(ir_n)/SR
irL=rng.standard_normal(ir_n)*np.exp(-tt/.45);irR=rng.standard_normal(ir_n)*np.exp(-tt/.45)
from scipy.signal import fftconvolve
L2=L+.03*fftconvolve(L,irL)[:N]/np.sqrt(ir_n)*30;R2=R+.03*fftconvolve(R,irR)[:N]/np.sqrt(ir_n)*30
st=np.stack([L2,R2],1)
# fades
fi=int(.3*SR);st[:fi]*=np.linspace(0,1,fi)[:,None]
fo=int(3*SR);st[-fo:]*=np.linspace(1,0,fo)[:,None]**1.5
st/=np.abs(st).max()*1.12
sf.write('music.wav',st,SR);print('ok',st.shape)
