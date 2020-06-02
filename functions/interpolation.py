from math import *
import math
import pandas as pd
import numpy as np

def run_interpolation(calcData) :

    fVector=calcData['filterVector']
    nint=calcData['lossFactor']
    m=calcData['sd']
    Fc=calcData['Fc']
    p0=calcData['p0']
    c=calcData['c']


    R = [None] * len(fVector)

    for i in range(len(fVector)):
            xStart=round((Fc/2),1)
            xEnd=(Fc)
            Ntot=nint + (m/(485*sqrt(xStart)))
            yEndA=10*log10(1+((pi*m*xEnd)/(p0*c))**2) + 10*log10((Ntot*2*xEnd)/(pi*Fc))
            yEndB=10*log10(1+((pi*m*xEnd)/(p0*c))**2) - 5.5
            if yEndA<=yEndB:
                yEnd=yEndA
            if yEndA>yEndB:
                yEnd=yEndB
            yStart=10*log10(1+((pi*m*xStart)/(p0*c))**2) - 5.5
            auxL=(xEnd-xStart)*10

            fAux=[None] * (auxL+1)
            rAux=[None] * (auxL+1)

            fAux[0]=xStart*10
            for i in range(1,len(fAux)):
                fAux[i]=fAux[i-1]+1
            rAux[0]=yStart
            rAux[auxL+1]=yEnd

            s=pd.Series(rAux)
            sharpNew=s.interpolate(method='linear')
            sList=sharpNew.values.tolist()

            for i in range(len(R)):
                if not R[i]:
                    fPos=int(fVector[i])*10
                    for o in range(len(fAux)):
                        if fAux[o]==fPos:
                            R[i]=sList[o]
    
    return R        