from math import *
import math
f=80
Fc=128
L=sqrt(f/Fc)
delta1=(((1-L**2)*log((1+L)/(1-L)))+2*L)/(4*(pi**2)*((1-L**2)**1.5))

print((1-L**2))