import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

c = 3e8

E = float(input("E (J): "))
tau = float(input("tau (ms): ")) * 1e-3
d = float(input("d (m): "))
R = float(input("R: "))

P = E / tau

A = math.pi * (d/2)**2

I = P / A

pressure = (1 + R) * I / c

print("Problem 15.28")
print(f"  P = {P:.2f} W")
print(f"  A = {A:.4e} m^2")
print(f"  I = {I:.3e} W/m^2")
print(f"  p = {pressure:.3e} Pa")