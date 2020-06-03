from math import *
import math
import pandas as pd
import numpy as np

def run_sharp(calcData) :

    fVector=calcData['filterVector']
    nint=calcData['lossFactor']
    m=calcData['sd']
    Fc=calcData['Fc']
    p0=calcData['p0']
    c=calcData['c']


    R = [None] * len(fVector)

    for i in range(len(fVector)):
        
        f = fVector[i]
        Ntot=nint + (m/(485*sqrt(f)))
        if f<(0.5*Fc):
            R[i]=10*log10(1+((pi*m*f)/(p0*c))**2) - 5.5
        if f>=Fc:
            R1=10*log10(1+((pi*m*f)/(p0*c))**2) + 10*log10((Ntot*2*f)/(pi*Fc))
            R2=10*log10(1+((pi*m*f)/(p0*c))**2) - 5.5

            if R1<R2:
                R[i]=R1
            if R2<R1:
                R[i]=R2
            if R2==R1:
                R[i]=R1          
    
    #Interpolacion linear / Auxiliares
    if Fc>20:
        xStart=round((Fc/2),0)
        xEnd=(round(Fc,0))
        Ntot=nint + (m/(485*sqrt(xStart)))
        yEndA=10*log10(1+((pi*m*xEnd)/(p0*c))**2) + 10*log10((Ntot*2*xEnd)/(pi*Fc))
        yEndB=10*log10(1+((pi*m*xEnd)/(p0*c))**2) - 5.5
        if yEndA<=yEndB:
            yEnd=yEndA
        if yEndA>yEndB:
            yEnd=yEndB
        yStart=10*log10(1+((pi*m*xStart)/(p0*c))**2) - 5.5
        auxL=int((xEnd-xStart)*1)

        fAux=[None] * (auxL+1)
        rAux=[None] * (auxL+1)

        fAux[0]=xStart*1
        for i in range(1,len(fAux)):
            fAux[i]=fAux[i-1]+1
        rAux[0]=yStart
        rAux[auxL]=yEnd

        s=pd.Series(rAux)
        sharpNew=s.interpolate(method='linear')
        sList=sharpNew.values.tolist()

        for i in range(len(R)):
            if not R[i]:
                fPos=int(fVector[i])*1
                for o in range(len(fAux)):
                    if fAux[o]==fPos:
                        R[i]=sList[o]
  
    
    return R        