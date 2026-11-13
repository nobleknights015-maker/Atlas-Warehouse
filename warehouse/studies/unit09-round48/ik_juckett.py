"""Python adaptation of Ryan Juckett's analytic two-bone sample.
Altered version: returns angles and reach validity; positive lengths required.
Source https://www.ryanjuckett.com/analytic-two-bone-ik-in-2d/

Copyright (c) 2008-2009 Ryan Juckett
http://www.ryanjuckett.com/
This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.
Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:
1. The origin of this software must not be misrepresented; you must not
claim that you wrote the original software. If you use this software
in a product, an acknowledgment in the product documentation would be
appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
misrepresented as being the original software.
3. This notice may not be removed or altered from any source
distribution.
"""
import math
def solve(length1,length2,target_x,target_y,positive=True):
    assert length1>0 and length2>0
    c=(target_x**2+target_y**2-length1**2-length2**2)/(2*length1*length2)
    valid=-1<=c<=1
    c=max(-1.,min(1.,c));a2=math.acos(c)*(1 if positive else -1)
    s=math.sin(a2);adj=length1+length2*c;opp=length2*s
    a1=math.atan2(target_y*adj-target_x*opp,target_x*adj+target_y*opp)
    return a1,a2,valid
