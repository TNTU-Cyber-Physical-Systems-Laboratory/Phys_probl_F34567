import sys
sys.stdout.reconfigure(encoding='utf-8')

import math

a0 = 0.0529e-9
E_ion = 13.6

print("Problem 16.25\n")

r = float(input("Radius r (in mm): ")) * 1e-3

n = math.sqrt(r / a0)
E_n = -E_ion / n**2

print(f"n = {n:.2f}")
print(f"E_n = {E_n:.4f} eV")