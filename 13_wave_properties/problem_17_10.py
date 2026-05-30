import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
m_e = 9.11e-31
e = 1.6e-19

V = float(input("Voltage V (V): "))
d = float(input("Slit spacing d (µm): ")) * 1e-6
L = float(input("Screen distance L (m): "))

lam = h / math.sqrt(2 * m_e * e * V)

delta_y = lam * L / d

print("Problem 17.10")
print(f"  V = {V:.1f} V")
print(f"  λ = {lam:.4e} m")
print(f"  Δy = {delta_y:.4e} m ({delta_y*1e6:.2f} µm)")