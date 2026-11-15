const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1087,height:216}});
const svg=require('fs').readFileSync('../../site/assets/logo-dark.svg','utf8');
await p.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
await p.locator('svg').screenshot({path:'logo.png',omitBackground:true});await b.close()})();
