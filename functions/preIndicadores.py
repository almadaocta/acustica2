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
from indicadores import get_indicadores


def preIndicadores(calcData,ly,t2,m2):

    calcData['filterVector'] = [20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500,16000,20000]
    calcData['db'] = 0.236
    calcData['octave'] = 3      

    ly=int(ly)
    if ly==1:
        set_layer(calcData,t2,m2)

    RdI=[]* len(calcData['filterVector'])
    RsI=[]* len(calcData['filterVector'])
    RcI=[]* len(calcData['filterVector'])
    RiI=[]* len(calcData['filterVector'])

    davyR = run_davy(calcData)
    RdI=[round(num, 2) for num in davyR]   

    sharpR = run_sharp(calcData)
    RsI=[round(num, 2) for num in sharpR]

    cremerR = run_cremer(calcData)
    RcI=[round(num, 2) for num in cremerR]   
  
    isoR = run_iso(calcData)
    RiI=[round(num, 2) for num in isoR]   
    
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

        RcI=np.add(RcI,Rc2).tolist()
        RdI=np.add(RdI,Rd2).tolist()
        RiI=np.add(RiI,Ri2).tolist()
        RsI=np.add(RsI,Rc2).tolist()


    
    get_indicadores(calcData,RiI)

    return RcI,RdI,RiI,RsI
    #SET EXPORT INDICADORES
