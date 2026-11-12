from kokoro_onnx import Kokoro
import soundfile as sf,numpy as np,json,sys
voice=sys.argv[1]; sp=float(sys.argv[2])
k=Kokoro('kokoro.onnx','voices.bin')
# (start time in final video, slot end, text)
L=[(0.25,3.4,"Still paying a developer just to launch one sales page?"),
   (3.6,13.3,"Watch this. Click New Funnel. Start from blank, let A.I. build it for you, or pick from over a thousand templates."),
   (13.7,20.7,"And these aren't mockups. They're real funnels, built to sell."),
   (21.0,26.1,"Pick one, and your whole funnel is ready. Page, booking, and thank you page."),
   (26.5,35.6,"Need better copy? Just ask A.I. It rewrites your headline in seconds."),
   (36.1,39.3,"Or click any text, and type. No code. No designer."),
   (39.6,44.6,"Drag in a countdown timer, to add urgency."),
   (44.9,51.0,"Your page is done. Hit publish, and you're live."),
   (51.5,59.5,"And the best part? Every sale shows up right here."),
   (59.8,64.2,"Start today for just seventeen dollars a month, at Oceanic Funnels dot com.")]
out=[]
for i,(a,b,txt) in enumerate(L):
    s,sr=k.create(txt,voice=voice,speed=sp,lang='en-us')
    # trim silence
    th=0.01;idx=np.where(np.abs(s)>th)[0];s=s[max(0,idx[0]-200):idx[-1]+2400]
    sf.write(f'l{i}.wav',s,sr);d=len(s)/sr
    out.append((a,b,d));print(i,round(d,2),'slot',round(b-a,2),'OVER' if d>b-a else '')
json.dump(out,open('timing.json','w'))
