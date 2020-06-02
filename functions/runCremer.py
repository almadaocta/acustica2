from math import *
import math

def run_cremer(calcData) :

    fVector=calcData['filterVector']
    nint=calcData['lossFactor']
    m=calcData['sd']
    Fc=calcData['Fc']
    Fd=calcData['Fd']

    R = [None] * len(fVector)

    for i in range(len(fVector)):
        
        f = fVector[i]
        Ntot= nint + (m/(485*sqrt(f)))
        if f<Fc:
            R[i]=20*log10(m*f)-47
        if Fd>f>Fc:
            R[i]=20*log10(m*f) - 10*log10(pi/(4*Ntot)) - 10*log10(Fc/(f-Fc)) -47
        if f>Fd:
            R[i]=20*log10(m*f)-47
            
   
    return R        