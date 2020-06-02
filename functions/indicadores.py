from math import *
import math

def get_rw(ReportVector,Ralt,filtro): 

    R=[]

    RefCurve=[33,36,39,42,45,48,51,52,53,54,55,56,56,56,56,56]        
    for i in range(len(RefCurve)):
        R.append(Ralt[i+3])

    R=[round(num, 1) for num in R] 
    
    #Adaptación curva
    difference=[]
    for i in range (len(RefCurve)):
        localDiff=RefCurve[i]-R[i]
        if localDiff>0:
            difference.append(localDiff)
        else:
            difference.append(0)

    success=0

    
        
    if sum(difference)<32:
        while success==0:
            for i in range (len(RefCurve)):
                RefCurve[i]=RefCurve[i]+1
            difference=[]
            for i in range (len(RefCurve)):
                localDiff=RefCurve[i]-R[i]
                if localDiff>0:
                    difference.append(localDiff)
                else:
                    difference.append(0)
            if sum(difference)>32:
                for i in range (len(RefCurve)):
                    RefCurve[i]=RefCurve[i]-1
                success=1
    if sum(difference)>32:
        while success==0:
            for i in range (len(RefCurve)):
                RefCurve[i]=RefCurve[i]-1
            difference=[]
            for i in range (len(RefCurve)):
                localDiff=RefCurve[i]-R[i]
                if localDiff>0:
                    difference.append(localDiff)
                else:
                    difference.append(0)
                if sum(difference)<32:
                    success=1
    
    difference=[]
    for i in range (len(RefCurve)):
        localDiff=RefCurve[i]-R[i]
        if localDiff>0:
            difference.append(localDiff)
        else:
            difference.append(0)

    
    rw=RefCurve[7]
    
    return RefCurve,rw


def get_stc(ReportVector,Ralt,filtro): 

    R=[]
    if filtro=='octava':
        RefCurve=[36,45,52,55,56]
        for i in range(len(RefCurve)):
            R.append(Ralt[i+1])
    else:
        RefCurve=[36,39,42,45,48,51,52,53,54,55,56,56,56,56,56,56]        
        for i in range(len(RefCurve)):
            R.append(Ralt[i+4])

    R=[round(num, 0) for num in R] 
    

    #Adaptación curva
    difference=[]
    for i in range (len(RefCurve)):
        localDiff=RefCurve[i]-R[i]
        if localDiff>0:
            difference.append(localDiff)
        else:
            difference.append(0)
    success=0

    if filtro=='octava':
        if sum(difference)<10 and max(difference)<8:
            while success==0:
                for i in range (len(RefCurve)):
                    RefCurve[i]=RefCurve[i]+1
                difference=[]
                for i in range (len(RefCurve)):
                    localDiff=RefCurve[i]-R[i]
                    if localDiff>0:
                        difference.append(localDiff)
                    else:
                        difference.append(0)
                if sum(difference)>10 or max(difference)>8:
                    for i in range (len(RefCurve)):
                        RefCurve[i]=RefCurve[i]-1
                    success=1
        else:
            while success==0:
                for i in range (len(RefCurve)):
                    RefCurve[i]=RefCurve[i]-1
                difference=[]
                for i in range (len(RefCurve)):
                    localDiff=RefCurve[i]-R[i]
                    if localDiff>0:
                        difference.append(localDiff)
                    else:
                        difference.append(0)
                if sum(difference)<10 and max(difference)<8:
                    success=1
    else:    
        if sum(difference)<32 and max(difference)<=8:
            while success==0:
                for i in range (len(RefCurve)):
                    RefCurve[i]=RefCurve[i]+1
                difference=[]
                for i in range (len(RefCurve)):
                    localDiff=RefCurve[i]-R[i]
                    if localDiff>0:
                        difference.append(localDiff)
                    else:
                        difference.append(0)
                if sum(difference)>32 or max(difference)>8:
                    for i in range (len(RefCurve)):
                        RefCurve[i]=RefCurve[i]-1
                    success=1
        else:
            while success==0:
                for i in range (len(RefCurve)):
                    RefCurve[i]=RefCurve[i]-1
                difference=[]
                for i in range (len(RefCurve)):
                    localDiff=RefCurve[i]-R[i]
                    if localDiff>0:
                        difference.append(localDiff)
                    else:
                        difference.append(0)
                if sum(difference)<32 and max(difference)<8:
                    success=1

    difference=[]
    for i in range (len(RefCurve)):
        localDiff=RefCurve[i]-R[i]
        if localDiff>0:
            difference.append(localDiff)
        else:
            difference.append(0)


    if filtro=='octava':
        stc=RefCurve[2]
    else:    
        stc=RefCurve[7]
    
    return RefCurve,stc

def get_C(Ralt,filtro,rw): 
    R=[]
    if filtro=='octava':

        #Caso octavcas

        #Calculo C   
        R=[Ralt[1],Ralt[2],Ralt[3],Ralt[4],Ralt[5]] 
        R=[round(num, 2) for num in R] 
        RefC=[-21,-14,-8,-5,-4]

        RefCaux=[]
        for i in range(len(RefC)):
            RefCaux.append(10**((RefC[i]-R[i])/10))
        XC=-10*log10(sum(RefCaux))
        C=round(XC-rw,0)
        #Calculo Ctr  
        RefCtr=[-14,-10,-7,-4,-6]
        RefCtraux=[]
        for i in range(len(RefCtr)):
            RefCtraux.append(10**((RefCtr[i]-R[i])/10))
        XCtr=-10*log10(sum(RefCtraux))
        Ctr=round(XCtr-rw,0)
        #Calculo C 50-3150  
        R=[Ralt[0],Ralt[1],Ralt[2],Ralt[3],Ralt[4],Ralt[5]] 
        R=[round(num, 2) for num in R] 
        RefC503150=[-31,-21,-14,-8,-5,-4]
        RefC503150aux=[]
        for i in range(len(RefC503150)):
            RefC503150aux.append(10**((RefC503150[i]-R[i])/10))
        XC503150=-10*log10(sum(RefC503150aux))
        C503150=round(XC503150-rw,0)  
        #Calculo C 50-5000 y 100-5000
        R=[Ralt[0],Ralt[1],Ralt[2],Ralt[3],Ralt[4],Ralt[5],Ralt[6]] 
        R=[round(num, 2) for num in R] 
        RefC505000=[-32,-22,-15,-9,-6,-5,-5]
        RefC505000aux=[]
        for i in range(len(RefC505000)):
            RefC505000aux.append(10**((RefC505000[i]-R[i])/10))
        50-5000    
        XC505000=-10*log10(sum(RefC505000aux))
        C505000=round(XC505000-rw,0)
        100-5000   
        XC1005000=-10*log10(sum(RefC505000aux)-RefC505000aux[0])
        C1005000=round(XC1005000-rw,0)        
    
        #Calculo Ctr 50-1350  Ctr 50-5000 Ctr 100-5000

        RefCtrAny=[-18,-14,-10,-7,-4,-6,-11]
        RefCtrAnyaux=[]
        for i in range(len(RefC505000)):
            RefCtrAnyaux.append(10**((RefCtrAny[i]-R[i])/10))

        #Ctr 50-1350    
        XCTR501350=-10*log10(sum(RefCtrAnyaux)-RefCtrAnyaux[5]-RefCtrAnyaux[6])
        CTR501350=round(XCTR501350-rw,0)
        #Ctr 50-5000  
        XCTR505000=-10*log10(sum(RefCtrAnyaux))
        CTR505000=round(XCTR505000-rw,0)  
        #Ctr 100-5000 
        XCTR105000=-10*log10(sum(RefCtrAnyaux)-RefCtrAnyaux[0])
        CTR105000=round(XCTR105000-rw,0)  

    else:   

        #Caso tercios de octava

        #Calculo C   
        for i in range(16):
            R.append(Ralt[i+3]) 
        R=[round(num, 1) for num in R] 
        RefC=[-29,-26,-23,-21,-19,-17,-15,-13,-12,-11,-10,-9,-9,-9,-9,-9]
        RefCaux=[]
        for i in range(len(RefC)):
            RefCaux.append(10**((RefC[i]-R[i])/10))
        XC=-10*log10(sum(RefCaux))
        C=round(XC-rw,0)
        #Calculo Ctr  
        RefCtr=[-20,-20,-18,-16,-15,-14,-13,-12,-11,-9,-8,-9,-10,-11,-13,-15]
        RefCtraux=[]
        for i in range(len(RefCtr)):
            RefCtraux.append(10**((RefCtr[i]-R[i])/10))
        XCtr=-10*log10(sum(RefCtraux))
        Ctr=round(XCtr-rw,0)
        #Calculo C 50-3150  
        R=[]
        for i in range(19):
            R.append(Ralt[i])
        RefC503150=[-40,-36,-33,-29,-26,-23,-21,-19,-17,-15,-13,-12,-11,-10,-9,-9,-9,-9,-9]
        RefC503150aux=[]
        for i in range(len(RefC503150)):
            RefC503150aux.append(10**((RefC503150[i]-R[i])/10))
        XC503150=-10*log10(sum(RefC503150aux))
        C503150=round(XC503150-rw,0)  
        #Calculo C 50-5000 y 100-5000
        R=[]
        for i in range(21):
            R.append(Ralt[i])
        RefC505000=[-41,-37,-34,-30,-27,-24,-22,-20,-18,-16,-14,-13,-12,-11,-10,-10,-10,-10,-10,-10,-10]
        RefC505000aux=[]
        for i in range(len(RefC505000)):
            RefC505000aux.append(10**((RefC505000[i]-R[i])/10))
        50-5000    
        XC505000=-10*log10(sum(RefC505000aux))
        C505000=round(XC505000-rw,0)
        100-5000   
        XC1005000=-10*log10(sum(RefC505000aux)-RefC505000aux[0]-RefC505000aux[1]-RefC505000aux[2])
        C1005000=round(XC1005000-rw,0)        
    
        #Calculo Ctr 50-1350  Ctr 50-5000 Ctr 100-5000
        R=[]
        for i in range(21):
            R.append(Ralt[i])
        RefCtrAny=[-25,-23,-21,-20,-20,-18,-16,-15,-14,-13,-12,-11,-9,-8,-9,-10,-11,-13,-15,-16,-18]
        RefCtrAnyaux=[]
        for i in range(len(RefC505000)):
            RefCtrAnyaux.append(10**((RefCtrAny[i]-R[i])/10))

        #Ctr 50-1350    
        XCTR501350=-10*log10(sum(RefCtrAnyaux)-RefCtrAnyaux[20]-RefCtrAnyaux[19])
        CTR501350=round(XCTR501350-rw,0)
        #Ctr 50-5000  
        XCTR505000=-10*log10(sum(RefCtrAnyaux))
        CTR505000=round(XCTR505000-rw,0)  
        #Ctr 100-5000 
        XCTR105000=-10*log10(sum(RefCtrAnyaux)-RefCtrAnyaux[0]-RefCtrAnyaux[1]-RefCtrAnyaux[2])
        CTR105000=round(XCTR105000-rw,0)    

    return C,Ctr,C503150,C505000,C1005000,CTR501350,CTR505000,CTR105000



def get_indicadores(calcData,RiI):
    if len(calcData['filterVector'])>10:
        filtro='tercios'
        ReportVector=[]
        Ralt=[]
        for i in range(0,21):
            Ralt.append(RiI[i+4])
            ReportVector.append(calcData['filterVector'][i+4])   
    else:    
        filtro='octava'
        ReportVector=[]
        Ralt=[]
        for i in range(0,7):
            Ralt.append(RiI[i+1])
            ReportVector.append(calcData['filterVector'][i+1])  

    rwCurve,rw=get_rw(ReportVector,Ralt,filtro)
    StcCurve,stc=get_stc(ReportVector,Ralt,filtro)
    C,Ctr,C503150,C505000,C1005000,CTR501350,CTR505000,CTR1005000=get_C(Ralt,filtro,rw)

    calcData['ralt']=Ralt
    calcData['rwCurve']=rwCurve
    calcData['StcCurve']=StcCurve
    calcData['Rw']=rw
    calcData['STC']=stc
    calcData['C']=C
    calcData['Ctr']=Ctr
    calcData['C503150']=C503150
    calcData['C505000']=C505000
    calcData['C1005000']=C1005000
    calcData['CTR501350']=CTR501350
    calcData['CTR505000']=CTR505000
    calcData['CTR1005000']=CTR1005000



