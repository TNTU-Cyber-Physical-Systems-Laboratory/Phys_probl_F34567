import sys
sys.stdout.reconfigure(encoding='utf-8')

import math

h = 6.626e-34
c = 3e8
k = 1.38e-23
e = 1.6e-19

print("Problem 17.46\n")

lam_nm = float(input("Wavelength (nm): "))
T = float(input("Temperature (K): "))

lam = lam_nm * 1e-9

dE = h * c / lam
exponent = -dE / (k * T)
ratio = math.exp(exponent)

print(f"ΔE = {dE:.3e} J")
print(f"Exponent = {exponent:.2f}")
print(f"N2/N1 = {ratio:.3e}")