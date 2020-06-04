from math import *
import math
from sigma import sigma
from shear import shear


def Single_leaf_Davy(calcData, frequency, density, Young, Poisson, thickness,lossfactor, length, width) :

    po = calcData['p0'] #Densidad del aire [Kg/m3]
    c = calcData['c'] #Velocidad sonido [m/s]
    cos21Max = 0.9 # Ángulo limite definido en el trabajo de Davy 

    surface_density = calcData['sd']
    #critical_frequency = sqrt(12 * density * (1 - (Poisson**2)) / Young) * (c**2) / (2 * thickness * pi)
    critical_frequency=calcData['Fc']
    normal = po * c / (pi * frequency * surface_density)
    normal2 = normal * normal
    e = 2 * length * width / (length + width)
    cos2l = c / (2 * pi * frequency * e)

    if cos2l > cos21Max :
        cos2l = cos21Max

    tau1 = normal2 * log((normal2 + 1) / (normal2 + cos2l))
    ratio = frequency / critical_frequency
    r = 1 - (1 / ratio)
    if r < 0 :
        r = 0
    G = sqrt(r)
    rad = sigma(calcData, G, frequency, length, width)
    rad2 = rad * rad
    netatotal = lossfactor + (rad * normal)
    z = 2 / netatotal
    y = atan(z) - atan(z * (1 - ratio))
    tau2 = (normal2 * rad2 * y) / (netatotal * 2 * ratio)
    tau2 = tau2 * shear(frequency, density, Young, Poisson, thickness)
    if frequency < critical_frequency:
        tau = tau1 + tau2
    else:
        tau = tau2

    single_leaf = -10 * log10(tau)

    return single_leaf