from math import *
import math

def shear(frequency, density, Young, Poisson, thickness):

    omega = 2 * pi * frequency
    chi = (1 + Poisson) / (0.87 + 1.12 * Poisson)
    chi = chi * chi
    X = thickness * thickness / 12
    QP = Young / (1 - Poisson * Poisson)
    C = -omega * omega
    B = C * (1 + 2 * chi / (1 - Poisson)) * X
    A = X * QP / density
    kbcor2 = (-B + sqrt(B * B - 4 * A * C)) / (2 * A)
    kb2 = sqrt(-C / A)
    G = Young / (2 * (1 + Poisson))
    kT2 = -C * density * chi / G
    kL2 = -C * density / QP
    kS2 = kT2 + kL2
    ASI = 1 + X * (kbcor2 * kT2 / kL2 - kT2)
    ASI = ASI * ASI
    BSI = 1 - X * kT2 + kbcor2 * kS2 / (kb2 * kb2)
    CSI = sqrt(1 - X * kT2 + kS2 * kS2 / (4 * kb2 * kb2))
    out = ASI / (BSI * CSI)
    return out