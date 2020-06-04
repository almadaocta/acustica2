from scipy import interpolate
import pandas as pd
import numpy as np
from setExport import set_export
from variableCollector import get_variables
from variableSet import set_variables
from runDavy import run_davy
from runCremer import run_cremer
from runSharp import run_sharp
from runIso import run_iso
from layer import set_layer
from preIndicadores import preIndicadores

def run_Calc(f,l,h,t,m,ly,t2,m2):

    

    calcData = get_variables(f,l,h,t,m)
    set_variables(calcData)


    ly=int(ly)
    if ly==1:
        set_layer(calcData,t2,m2)

    Rd=[]* len(calcData['filterVector'])
    Rs=[]* len(calcData['filterVector'])
    Rc=[]* len(calcData['filterVector'])
    Ri=[]* len(calcData['filterVector'])

    davyR = run_davy(calcData)
    Rd=[round(num, 2) for num in davyR]   

    sharpR = run_sharp(calcData)
    Rs=[round(num, 2) for num in sharpR]

    cremerR = run_cremer(calcData)
    Rc=[round(num, 2) for num in cremerR]   
  
    isoR = run_iso(calcData)
    Ri=[round(num, 2) for num in isoR]   
    
    if ly==1:
        Rd2=[]* len(calcData['filterVector'])
        Rs2=[]* len(calcData['filterVector'])
        Rc2=[]* len(calcData['filterVector'])
        Ri2=[]* len(calcData['filterVector'])

        calcData['thickness']=calcData['thickness2']
        calcData['density']=calcData['density2']
        calcData['poisson']=calcData['poisson2']
        calcData['young']=calcData['young2']
        calcData['lossFactor']=calcData['lossFactor2']

        davyR2 = run_davy(calcData)
        Rd2=[round(num, 2) for num in davyR2]   

        sharpR2 = run_sharp(calcData)
        Rs2=[round(num, 2) for num in sharpR2]

        cremerR2 = run_cremer(calcData)
        Rc2=[round(num, 2) for num in cremerR2]   
    
        isoR2 = run_iso(calcData)
        Ri2=[round(num, 2) for num in isoR2]   

        Rc=np.add(Rc,Rc2).tolist()
        Rd=np.add(Rd,Rd2).tolist()
        Ri=np.add(Ri,Ri2).tolist()
        Rs=np.add(Rs,Rc2).tolist()

    

    RcI,RdI,RiI,RsI=preIndicadores(calcData,ly,t2,m2)
    
    name=set_export(calcData,RdI,RsI,RcI,RiI,ly)

    

    return Rc,Rd,Rs,Ri, calcData,name
    
