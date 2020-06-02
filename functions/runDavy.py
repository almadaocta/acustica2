from math import *
import math
from davy import Single_leaf_Davy

def run_davy(calcData) :

    fVector=calcData['filterVector']
    nint=calcData['lossFactor']
    m=calcData['sd']
    Fc=calcData['Fc']
    octave=calcData['octave']
    averages=3
    p=calcData['density']
    E=calcData['young']
    o=calcData['poisson']
    t=calcData['thickness']
    l2=calcData['height']
    l1=calcData['length']


    R = [None] * len(fVector)

    for i in range(len(fVector)):
        
        f = fVector[i]
        Ntot=nint + (m/(485*sqrt(f)))
        ratio = f/Fc
        limit = 2**(1/(2*octave))

        if (ratio < 1 / limit) or (ratio > limit) :

            TLost = Single_leaf_Davy(calcData,f,p,E,o,t,Ntot,l2,l1)
        
        else:
        
            Avsingle_leaf = 0

            for j in range(1, averages+1):

                factor = 2 ** ((2*j-1-averages)/(2*averages*octave))
                fFactor = f*factor
                aux=10**((-1*Single_leaf_Davy(calcData,fFactor,p,E,o,t,Ntot,l2,l1))/10)
                Avsingle_leaf = Avsingle_leaf + aux
              
            TLost = -10*log10(Avsingle_leaf/averages)
       
        R[i]= TLost
            
    return R



    
