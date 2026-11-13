import sys,numpy as np,soundfile as sf
from kokoro_onnx import Kokoro
from scipy.signal import resample_poly
voice,base,lang=sys.argv[1],float(sys.argv[2]),sys.argv[3]
k=Kokoro('kokoro.onnx','voices.bin')
L=[(0.2,3.75,"Okay, stop scrolling! You have to see this!"),
   (3.85,13.3,"Watch! Click New Funnel. Start from blank, let A.I. build it for you, or pick from over a thousand templates!"),
   (13.7,20.7,"And these are not mockups! These are real funnels, built to sell!"),
   (21.0,26.1,"Pick one, and boom! Your whole funnel is ready!"),
   (26.5,35.6,"Need better copy? Just ask A.I.! It rewrites your headline in seconds!"),
   (35.6,39.45,"Or click any text, and type! No code! No designer!"),
   (39.6,44.6,"Drag in a countdown timer. Urgency, done!"),
   (44.9,51.0,"Your page is ready! Hit publish, and you are live!"),
   (51.5,59.5,"And here's the best part! Every single sale shows up right here!"),
   (59.8,65.0,"All of this, for just seventeen dollars a month! Go to Oceanic Funnels dot com!")]
SR=44100;N=int(66.5*SR);v=np.zeros(N)
for i,(a,b,txt) in enumerate(L):
    sp=base
    for _ in range(6):
        s,sr=k.create(txt,voice=voice,speed=sp,lang=lang)
        idx=np.where(np.abs(s)>.01)[0];s=s[max(0,idx[0]-200):idx[-1]+2400]
        if len(s)/sr<=b-a-.05 or sp>=1.15:break
        sp=round(sp*((len(s)/sr)/(b-a-.1))+.01,3)
    x=resample_poly(s,147,80);j=int(a*SR);v[j:j+len(x)]+=x[:N-j]
    print(voice,i,round(len(s)/sr,2),'slot',round(b-a,2),'speed',sp)
sf.write(f'voice_{voice}_x.wav',v/np.abs(v).max()*.9,SR)
