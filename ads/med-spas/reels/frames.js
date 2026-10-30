const p=require('/home/claude/shot/node_modules/puppeteer-core');const [,,html,dir,dur,fps]=process.argv;
(async()=>{const b=await p.launch({executablePath:'/tmp/chromium',args:['--no-sandbox']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file://'+html,{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);const n=Math.round(dur*fps);
for(let i=0;i<n;i++){await pg.evaluate(t=>render(t),i/fps);await pg.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();console.log('frames',n)})();
