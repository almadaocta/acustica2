from math import *
import math
from davy import Single_leaf_Davy

def run_iso(calcData) :

    fVector=calcData['filterVector']
    nint=calcData['lossFactor']
    m=calcData['sd']
    Fc=calcData['Fc']
    octave=calcData['octave']
    averages=3
    p=calcData['density']
    l2=calcData['height']
    l1=calcData['length']
    p0=calcData['p0']
    c=calcData['c']
    f11=calcData['f11']
    R = [None] * len(fVector)

    for i in range(len(fVector)):
        
        f = fVector[i]
        Ntot=nint + (m/(485*sqrt(f)))  
        
        
        if f11<=(Fc/2):
            
            if f>=Fc:
                
                O=1/(sqrt(1-(Fc/f)))
                if O>2:
                    O=2

            if f<Fc:
                L=sqrt(f/Fc)

                delta1=(((1-L**2)*log((1+L)/(1-L)))+2*L)/(4*(pi**2)*((1-L**2)**1.5))
         
                if f>(Fc/2):
                    delta2=0   
                else:

                    a=8*c**2*(1-2*L**2)
                    b=Fc**2*pi**4*l1*l2*L*sqrt(1-L**2)
                    delta2=a/b
                  
                O=(((2*(l1+l2))/(l1*l2))*(c/Fc)*(delta1))+delta2


                if f<f11<(Fc/2):
                    O2=4*l1*l2*(f/c)**2
                    if O>O2:
                        O=O2
                    
        
        if f11>(Fc/2):
            if f>Fc:
                O1=1/(sqrt(1-(Fc/f)))
            O2=4*l1*l2*((f/c)**2)
            O3=sqrt((2*pi*f*(l1+l2))/(16*c))

            if f<Fc and O2<O3:
                O=O2
                
            elif f>Fc and O1<O3:
                O=O1
            else:
                O=O3  
        
        if O>2:
            O=2
          
        if f>Fc:
            t=(((2*p0*c)/(2*pi*f*m))**2)*((pi*Fc*(O**2))/(2*f*Ntot))
            R[i]=-10*log10(t)
        if f==Fc:
            t=(((2*p0*c)/(2*pi*f*m))**2)*((pi*(O**2))/(2*Ntot))
            R[i]=-10*log10(t)
        if f<Fc:        
            k=(2*pi*f)/c
            V=-1*0.964-(0.5+l2/(pi*l1))*log(l2/l1)+(5*l2)/(2*pi*l1)-1/(4*pi*l1*l2*k**2)
            Of=0.5*(log(k*sqrt(l1*l2))-V) 
            
            if Of>2:
                Of=2   
            t1=(((2*p0*c)/(2*pi*f*m))**2)
            t2=((2*Of)+((l1+l2)**2/(l1**2+l2**2))*(sqrt(Fc/f))*(O**2/Ntot))
            #t2=(2*(Of**2))+(((l1+l2)**2)/(l1**2+l2**2))*(sqrt(Fc/f))*(O**2/Ntot)
            t=t1*t2
            R[i]=-10*log10(t)

    return R        