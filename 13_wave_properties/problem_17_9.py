import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
e = 1.6e-19

r = float(input("Radius r (mm): ")) * 1e-3
B = float(input("Magnetic field B (mT): ")) * 1e-3

q = 2 * e

p = q * B * r
lam = h / p

print("Problem 17.9")
print(f"  r = {r*1e3:.1f} mm, B = {B*1e3:.2f} mT")
print(f"  p = {p:.4e} kg·m/s")
print(f"  λ = {lam:.4e} m ({lam*1e10:.3f} Å, {lam*1e9:.4f} nm)")