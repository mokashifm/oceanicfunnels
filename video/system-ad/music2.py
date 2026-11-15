import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve
SR=48000; DUR=36.5; N=int(DUR*SR); t=np.arange(N)/SR
BPM=100; B=60/BPM; rng=np.random.default_rng(7)
def lp(x,f,o=2): return sosfilt(butter(o,f/(SR/2),'low',output='sos'),x)
def hp(x,f,o=2): return sosfilt(butter(o,f/(SR/2),'high',output='sos'),x)
def env(n,a,r):
    e=np.ones(n); A=int(a*SR); R=int(r*SR)
    e[:A]=np.linspace(0,1,A); e[-R:]*=np.linspace(1,0,R); return e
def saw(f,n,det=0):
    tt=np.arange(n)/SR; return sum(2*((tt*f*(1+d))%1)-1 for d in (-det,0,det))/3
def note(m): return 440*2**((m-69)/12)
# chords (A minor): Am F C G, 2 bars each (8 beats = 4.8s)
CH=[[57,60,64],[53,57,60],[48,55,60],[55,59,62]]; ROOT=[45,41,48,43]
bar=8*B
pad=np.zeros(N); bass=np.zeros(N); arp=np.zeros(N)
k=0; s=0.0
while s<DUR:
    i=int(s*SR); n=min(int(bar*SR),N-i); c=CH[k%4]
    p=sum(saw(note(m),n,.004) for m in c)/3
    pad[i:i+n]+=lp(p,1400)*env(n,.8,.8)
    bass[i:i+n]+=np.sin(2*np.pi*note(ROOT[k%4])*np.arange(n)/SR)*env(n,.05,.3)
    # 16th arp
    seq=[c[0]+12,c[1]+12,c[2]+12,c[1]+24,c[2]+12,c[0]+24,c[1]+12,c[2]+12]
    for j in range(32):
        a=i+int(j*B/4*SR); m=int(B/4*SR*0.9)
        if a+m>N: break
        f=note(seq[j%8]); tt=np.arange(m)/SR
        tone=(np.sin(2*np.pi*f*tt)+.3*np.sin(2*np.pi*2*f*tt))*np.exp(-tt*14)
        arp[a:a+m]+=tone
    k+=1; s+=bar
# drums
kick=np.zeros(N); hat=np.zeros(N); duck=np.ones(N)
def kick_at(s,g=1):
    i=int(s*SR); m=int(.45*SR)
    if i+m>N: return
    tt=np.arange(m)/SR; f=50+90*np.exp(-tt*28)
    kick[i:i+m]+=g*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*7)
    d=1-.55*np.exp(-np.arange(int(.3*SR))/SR*9); j=min(len(d),N-i); duck[i:i+j]=np.minimum(duck[i:i+j],d[:j])
def hat_at(s,g=1):
    i=int(s*SR); m=int(.06*SR)
    if i+m>N: return
    hat[i:i+m]+=g*hp(rng.standard_normal(m),7000)*np.exp(-np.arange(m)/SR*60)
b=0
while b*B<DUR:
    st=b*B
    if 3.4<=st<29.2: kick_at(st, .9)
    if 10.1<=st<29.2:
        hat_at(st+B/2,.35)
        if 19.6<=st: hat_at(st+B/4,.18); hat_at(st+3*B/4,.18)
    b+=1
# riser into logo + impact
riser=np.zeros(N); i0=int(26.6*SR); i1=int(29.85*SR); m=i1-i0
ns=rng.standard_normal(m); prog=np.linspace(0,1,m)
r=np.zeros(m)
for q in range(0,m,2048):
    seg=ns[q:q+2048]; r[q:q+len(seg)]=hp(seg,300+6000*prog[q]**2)
riser[i0:i1]=r*prog**2.5*.5
imp=np.zeros(N); i=int(29.9*SR); m=int(4*SR); tt=np.arange(m)/SR
imp[i:i+m]=(np.sin(2*np.pi*(38+40*np.exp(-tt*10))*tt)*np.exp(-tt*1.6)+lp(rng.standard_normal(m),900)*np.exp(-tt*3)*.4)
# arrangement gains
def ramp(pts): return np.interp(t,[p[0] for p in pts],[p[1] for p in pts])
g_pad=ramp([(0,0),(1.2,.55),(29.4,.55),(29.9,.85),(36.5,0)])
g_arp=ramp([(0,0),(3.2,0),(3.6,.22),(10,.28),(26.5,.32),(29.5,0),(31,.12),(34,.0)])
g_bass=ramp([(0,0),(3.3,0),(3.6,.5),(29.4,.5),(29.6,0),(29.9,.4),(35,0)])
mix=pad*g_pad+arp*g_arp*duck+bass*g_bass*duck+kick*.8+hat+riser+imp*.9
# reverb
ir_n=int(2.2*SR); ir=rng.standard_normal(ir_n)*np.exp(-np.arange(ir_n)/SR*2.8); ir=lp(ir,5000)
wet=fftconvolve(mix,ir)[:N]; wet/=np.abs(wet).max()
mix=mix/np.abs(mix).max()*.8+wet*.25
mix=np.tanh(mix*1.2); mix/=np.abs(mix).max()
L=mix; R=np.roll(fftconvolve(mix,ir*0.0+0,mode='same') if False else mix,int(.012*SR))
sf.write('ad_music2.wav',np.stack([L,R],1)*.9,SR); print('ok')
