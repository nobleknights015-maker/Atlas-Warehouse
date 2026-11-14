// Read-only characterization of the current Sprite Studio. No production mutations.
// node audit-generator.mjs /absolute/path/to/bearframe-ghost-signal [results.json]
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import {resolve,join} from 'node:path';
import {writeFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
const project=resolve(process.argv[2]);
const require=createRequire(join(project,'frontend/package.json'));
const {createCanvas,ImageData}=require('@napi-rs/canvas');
globalThis.ImageData=ImageData;
globalThis.document={createElement(type){if(type!=='canvas')throw Error(type);return createCanvas(1,1);}};
const load=p=>import(pathToFileURL(join(project,'frontend/public/studio/lib',p)).href);
const {MACHINE_PRESETS}=await load('machine-presets.js');
const {renderRig}=await load('machine-rig.js');
const {machineProject,buildSheet}=await load('sprite-sheet.js');
const {legIK}=await load('android-chassis.js');
const digest=c=>createHash('sha256').update(c.getContext('2d').getImageData(0,0,c.width,c.height).data).digest('hex');
const render=(rig,dir,type,i,n)=>{const c=createCanvas(rig.w,rig.h);renderRig(c.getContext('2d'),rig,dir,type,i,n,c.width,c.height);return c;};
const diff=(a,b)=>{const x=a.getContext('2d').getImageData(0,0,a.width,a.height).data,y=b.getContext('2d').getImageData(0,0,b.width,b.height).data;let count=0;for(let i=0;i<x.length;i+=4)if(x[i]!==y[i]||x[i+1]!==y[i+1]||x[i+2]!==y[i+2]||x[i+3]!==y[i+3])count++;return count;};
const overscan=(rig,pad=48)=>{const r=JSON.parse(JSON.stringify(rig));r.w+=2*pad;r.h+=2*pad;for(const view of Object.values(r.views)){const ids=new Set(view.map(p=>p.id));for(const p of view)if(!p.p||!ids.has(p.p)){p.x+=pad;p.y+=pad;}}return r;};
const result={study:'echo-grid-integration',scope:'Read-only characterization. Findings are probes, not art acceptance.',commit:execFileSync('git',['rev-parse','HEAD'],{cwd:project,encoding:'utf8'}).trim(),presets:[],ikReachProbes:[],renderCases:0,repeatMismatches:0};
for(const [name,make] of Object.entries(MACHINE_PRESETS)){
 const rig=make(),views={};
 for(const [dir,parts] of Object.entries(rig.views)){
  const ids=new Set(),duplicates=[],parents=[];for(const p of parts){if(ids.has(p.id))duplicates.push(p.id);ids.add(p.id);}for(const p of parts)if(p.p&&!ids.has(p.p))parents.push({id:p.id,parent:p.p});
  const byId=new Map(parts.map(p=>[p.id,p])),cycles=[];for(const p of parts){const path=new Set();let q=p;while(q){if(path.has(q.id)){cycles.push([...path,q.id]);break;}path.add(q.id);q=byId.get(q.p);}}
  views[dir]={parts:parts.length,duplicates,missingParents:parents,cycles};
 }
 const n=8,entry={name,size:[rig.w,rig.h],tiles:rig.tiles,authoredViews:Object.keys(rig.views),leftMirrored:!rig.views.left&&!!rig.views.right,views,actions:Object.keys(rig.anims),loopEndpointPixelDifferences:[],overscan:[]};
 const expanded=overscan(rig);
 for(const dir of ['down','up','right','left'])for(const type of Object.keys(rig.anims)){
  let maxOutside=0,framesWithOutside=0;
  for(let i=0;i<n;i++){
   const c=render(rig,dir,type,i,n);if(digest(c)!==digest(render(rig,dir,type,i,n)))result.repeatMismatches++;result.renderCases++;
   const over=render(expanded,dir,type,i,n),d=over.getContext('2d').getImageData(0,0,over.width,over.height).data;let outside=0;
   for(let y=0;y<over.height;y++)for(let x=0;x<over.width;x++)if((x<48||x>=48+rig.w||y<48||y>=48+rig.h)&&d[(y*over.width+x)*4+3])outside++;
   if(outside)framesWithOutside++;maxOutside=Math.max(maxOutside,outside);
  }
  if(maxOutside)entry.overscan.push({dir,type,framesWithOutside,maxOutsidePixels:maxOutside});
  if(['idle','walk'].includes(type))entry.loopEndpointPixelDifferences.push({dir,type,pixels:diff(render(rig,dir,type,0,n),render(rig,dir,type,n,n))});
 }
 const p=machineProject(name,rig),sheet=buildSheet(p.sets.battle);entry.currentBattleExport={width:sheet.canvas.width,height:sheet.canvas.height,rgbaBytes:sheet.canvas.width*sheet.canvas.height*4,anchor:sheet.meta.anchor};
 result.presets.push(entry);
}
for(const target of [{x:0,y:100},{x:0,y:0},{x:0,y:.2},{x:4,y:12}]){
 const r=legIK({x:0,y:0},target),a=Math.hypot(r.knee.x,r.knee.y),b=Math.hypot(r.knee.x-target.x,r.knee.y-target.y);
 result.ikReachProbes.push({target,expectedLengths:[r.l1,r.l2],measuredLengths:[a,b],maxLengthError:Math.max(Math.abs(a-r.l1),Math.abs(b-r.l2))});
}
if(process.argv[3])writeFileSync(process.argv[3],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({commit:result.commit,renderCases:result.renderCases,repeatMismatches:result.repeatMismatches,presets:result.presets.map(p=>({name:p.name,authoredViews:p.authoredViews,overscanFlags:p.overscan.length,maxLoopEndpointDifference:Math.max(...p.loopEndpointPixelDifferences.map(x=>x.pixels)),battleSheet:p.currentBattleExport})),ikReachProbes:result.ikReachProbes},null,2));
