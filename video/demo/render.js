const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const name=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('http://localhost:8822/demo.html');await p.evaluate(()=>document.fonts.ready);
const dur=await p.evaluate(n=>setup(n),name);await p.evaluate(()=>ready());const N=Math.round(dur*30);
const tmp=`out/${name}.tmp.mp4`;
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30',tmp]);
for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/30);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();ff.on('close',c=>{if(c===0)fs.renameSync(tmp,`out/${name}.mp4`);console.log(name,N,c);b.close();});})();
