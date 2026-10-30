const p=require('/home/claude/shot/node_modules/puppeteer-core');const [,,rid,dir,mode,...ts]=process.argv;
(async()=>{const b=await p.launch({executablePath:'/tmp/chromium',args:['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});const pg=await b.newPage();pg.on('pageerror',e=>console.log('ERR',e.message));
await pg.setViewport({width:1080,height:1920});await pg.goto('http://localhost:8123/clinic.html?reel=reel_'+rid,{waitUntil:'networkidle0'});await pg.waitForFunction('window.ready',{timeout:90000});await pg.evaluate(()=>document.fonts.ready);
if(mode==='keys'){for(const t of ts){await pg.evaluate(t=>render(+t),t);await pg.screenshot({path:`${dir}/k_${t}.jpg`,type:'jpeg',quality:80});}}
else{const [dur,fps]=ts.map(Number);const n=Math.round(dur*fps);for(let i=0;i<n;i++){await pg.evaluate(t=>render(t),i/fps);await pg.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});if(i%150==0)console.log(rid,i,'/',n)}}
await b.close();})();
