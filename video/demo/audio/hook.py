import numpy as np,soundfile as sf,json
from kokoro_onnx import Kokoro
from scipy.signal import resample_poly
k=Kokoro('kokoro.onnx','voices.bin')
P=[("Oh, you made it.",.35),("Listen, you are a business owner",.08),("or an entrepreneur,",.12),("or you want to create a digital product",.05),("and sell it online.",.35),
   ("You landed at the right place.",.25),("You need to start right now.",.2),("The price goes up on November twentieth,",.06),("so you want to hurry up.",.35),
   ("Make sure you sign up right now.",.2),("Pick a template, let A.I. build your page,",.06),("and hit publish.",.2),("All right, so you can start taking payments today.",.3),
   ("Seventeen dollars a month.",.25),("I can't wait to see what you build.",.5)]
SR=44100;t=0.35;parts=[];segs=[]
for txt,gap in P:
    s,sr=k.create(txt,voice='af_heart',speed=1.05,lang='en-us')
    idx=np.where(np.abs(s)>.01)[0];s=s[max(0,idx[0]-150):idx[-1]+1500]
    x=resample_poly(s,147,80);segs.append((t,x));d=len(x)/SR
    parts.append({'a':round(t,3),'b':round(t+d,3),'txt':txt});t+=d+gap
N=int((t+.4)*SR);v=np.zeros(N)
for a,x in segs:i=int(a*SR);v[i:i+len(x)]+=x
sf.write('hook_vo.wav',v/np.abs(v).max()*.9,SR)
json.dump({'dur':round(N/SR,2),'p':parts},open('hook.json','w'),indent=0);print(N/SR)
for p in parts:print(p)
