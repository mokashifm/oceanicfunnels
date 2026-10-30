const p=require('/home/claude/shot/node_modules/puppeteer-core');const jobs=require(process.argv[2]);
(async()=>{const b=await p.launch({executablePath:'/tmp/chromium',args:['--no-sandbox']});const pg=await b.newPage();
for(const [h,o,H] of jobs){await pg.setViewport({width:1080,height:H});await pg.goto('file://'+h,{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
const ov=await pg.evaluate(()=>{const w=document.querySelector('.w');return w.scrollHeight>w.clientHeight+2});if(ov)console.log('OVERFLOW',o);
await pg.screenshot({path:o});}await b.close();console.log('done',jobs.length)})();
