import sys
sys.stdout.reconfigure(encoding='utf-8')

import math

print("Problem 17.43\n")

a0 = float(input("Bohr radius (m): "))
v1 = float(input("Electron velocity (m/s): "))
e = 1.6e-19

T = 2 * math.pi * a0 / v1
I = e / T

print(f"T = {T:.4e} s")
print(f"I = {I:.4e} A")