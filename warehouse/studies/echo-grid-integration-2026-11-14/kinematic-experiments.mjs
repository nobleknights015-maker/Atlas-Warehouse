// Independent research probes. Not imported by the generator; not production art.
import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
export function solveTwoBone(hip,target,l1,l2,bend=1){
 if(![hip.x,hip.y,target.x,target.y,l1,l2].every(Number.isFinite)||l1<=0||l2<=0)throw Error('Invalid chain');
 const dx=target.x-hip.x,dy=target.y-hip.y,d=Math.hypot(dx,dy),ux=d>1e-12?dx/d:0,uy=d>1e-12?dy/d:1;
 const r=Math.max(Math.abs(l1-l2)+1e-8,Math.min(l1+l2-1e-8,d));
 const end={x:hip.x+ux*r,y:hip.y+uy*r},a=(l1*l1-l2*l2+r*r)/(2*r),h=Math.sqrt(Math.max(0,l1*l1-a*a));
 const knee={x:hip.x+ux*a+uy*h*bend,y:hip.y+uy*a-ux*h*bend};
 return {hip,knee,end,requested:target,clamped:Math.abs(r-d)>1e-7};
}
// Body-relative foot: stance moves backward while the root advances.
// Hermite swing tangents match stance velocity. Height and its derivative are zero at contacts.
export function footPath(phase,stride=8,duty=.5,height=3){
 const p=((phase%1)+1)%1;
 if(p<duty)return {x:stride/2-stride*p/duty,z:0,stance:true};
 const u=(p-duty)/(1-duty),u2=u*u,u3=u2*u,m=-stride*(1-duty)/duty;
 return {x:(2*u3-3*u2+1)*(-stride/2)+(u3-2*u2+u)*m+(-2*u3+3*u2)*(stride/2)+(u3-u2)*m,z:16*height*u2*(1-u)*(1-u),stance:false};
}
const len=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
let ikCases=0,maxLengthError=0,maxStanceDrift=0,maxJoinGap=0;const counts=[];
for(const [l1,l2] of [[8,8.5],[8,8],[1,20],[20,1]])for(const bend of [-1,1])for(let i=0;i<400;i++){
 const hip={x:3,y:-2},angle=i*.71,d=[0,.001,.2,4,16.49,30,100][i%7],target={x:hip.x+Math.cos(angle)*d,y:hip.y+Math.sin(angle)*d};
 const s=solveTwoBone(hip,target,l1,l2,bend),err=Math.max(Math.abs(len(s.hip,s.knee)-l1),Math.abs(len(s.knee,s.end)-l2));assert(err<1e-6);maxLengthError=Math.max(maxLengthError,err);ikCases++;
}
for(const [name,duty,offsets,expected] of [['tripod',.5,[0,0,0,.5,.5,.5],3],['ripple',2/3,[0,0,1/3,1/3,2/3,2/3],4],['wave',5/6,[0,1/6,2/6,3/6,4/6,5/6],5]]){
 let samples=0;for(let tick=0;tick<1200;tick++){
  const t=(tick+.1234)/1200,count=offsets.filter(o=>footPath(t+o,8,duty).stance).length;assert.equal(count,expected);samples++;
 }
 let prev=null;for(let i=0;i<100;i++){const t=duty*i/100,f=footPath(t,8,duty),world=8/duty*t+f.x;if(prev!==null)maxStanceDrift=Math.max(maxStanceDrift,Math.abs(world-prev));prev=world;}
 for(const joint of [duty,1]){const a=footPath(joint-1e-7,8,duty),b=footPath(joint+1e-7,8,duty);maxJoinGap=Math.max(maxJoinGap,Math.hypot(a.x-b.x,a.z-b.z));}
 counts.push({name,duty,expectedStance:expected,samples});
}
assert(maxStanceDrift<1e-10);assert(maxJoinGap<1e-4);
// Integer revolution closure with panel identity attached to material angle.
let ringChecks=0;for(const N of [8,12,18,24])for(let panel=0;panel<N;panel++)for(const turns of [-2,-1,0,1,2]){
 const a=2*Math.PI*panel/N,b=a+2*Math.PI*turns;assert(Math.hypot(Math.cos(a)-Math.cos(b),Math.sin(a)-Math.sin(b))<1e-12);ringChecks++;
}
const results={status:'PASS',scope:'Independent mathematical experiments; not integrated and not visual proof',ikCases,maxLengthError,maxStanceDrift,maxJoinGap,gaits:counts,ringChecks,limitations:['No joint-angle limits or collision solver','Static support counts do not prove center-of-mass stability','World-lock check assumes constant root velocity on flat ground','No raster, cloth, silhouette or device-performance acceptance']};
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(results,null,2)+'\n');console.log(JSON.stringify(results,null,2));
