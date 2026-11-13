import numpy as np,soundfile as sf
from kokoro_onnx import Kokoro
from scipy.signal import resample_poly
k=Kokoro('kokoro.onnx','voices.bin')
P=[(0.3,"Okay, stop scrolling."),(2.0,"You have to see this!"),
 (4.0,"First, click New Funnel."),(6.0,"Start from blank,"),(8.2,"let A.I. build it for you,"),(10.1,"or pick from over a thousand templates!"),
 (14.0,"These are real funnels."),(15.7,"Built to sell!"),(17.5,"Pick one,"),
 (21.1,"and boom!"),(22.2,"Your whole funnel is ready."),
 (26.8,"Now. Need better copy?"),(28.8,"Just ask A.I."),(32.0,"Look at that! A new headline, in seconds."),
 (36.4,"Or click any text,"),(37.9,"and type!"),
 (39.6,"Drag in a countdown timer,"),(43.8,"urgency, done!"),
 (45.3,"Your page is ready."),(48.0,"Hit publish,"),(49.9,"and you're live!"),
 (52.0,"And here's the best part!"),(54.2,"Every sale,"),(55.4,"shows up right here!"),
 (59.9,"All of this, for just seventeen dollars a month."),(62.9,"Oceanic Funnels dot com!")]
SR=44100;N=int(66.5*SR);v=np.zeros(N);prev_end=0
for i,(a,txt) in enumerate(P):
    s,sr=k.create(txt,voice='af_heart',speed=1.05,lang='en-us')
    idx=np.where(np.abs(s)>.01)[0];s=s[max(0,idx[0]-150):idx[-1]+1800]
    x=resample_poly(s,147,80);d=len(x)/SR
    nxt=P[i+1][0] if i+1<len(P) else 65.2
    flag='OVERLAP' if a+d>nxt-.15 else ''
    if a<prev_end+.15: flag+=' TOOCLOSE'
    print(f'{a:5.1f}-{a+d:5.2f} next {nxt:5.1f} {flag} {txt}')
    j=int(a*SR);v[j:j+len(x)]+=x;prev_end=a+d
sf.write('voice_phrased.wav',v/np.abs(v).max()*.9,SR)
