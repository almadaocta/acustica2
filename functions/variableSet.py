
from math import *
import math

def set_variables(calcData):

    c = 343 #Velocidad del sonido en el aire
    p0 = 1.18 #Densidad del aire
    p =  calcData['density'] #Densidad del material
    t = calcData['thickness'] #Espesor material
    ly = calcData['height'] #Alto
    lx = calcData['length'] #Ancho
    sd = p*t #Densidad superficial
    o = calcData['poisson'] #Módulo Poisson
    E = calcData['young'] #Módulo young
    s = lx*ly # Superficie
    B = (E/(1-o**2))*((t**3)/12) # Rigidez a la flexión 
    Fc = (c**2/(2*math.pi))*(sqrt(sd/B)) #Frecuencia crítica
    Fc= round(Fc,1)
    Fd = (E/(2*math.pi*p))*(sqrt(sd/B)) # Frecuencia de densidad
    f11 = (c**2/(4*Fc))*((1/lx**2)+(1/ly**2)) #Modo (1,1) de placa del elemento


    #Asigno variables al diccionario
    calcData['c'] = c #Velocidad del sonido en el aire
    calcData['p0'] = p0 #Densidad del aire
    calcData['sd'] = sd #Densidad superficial
    calcData['s'] = s #Superficie
    calcData['B'] = B #Rigidez a la flexión 
    calcData['Fc'] = Fc #Frecuencia crítica
    calcData['Fd'] = Fd #Frecuencia de densidad
    calcData['f11'] = f11 #Modo (1,1) de placa del elemento

    
    print(Fc)
