import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
m_e = 9.11e-31
e = 1.6e-19

V = float(input("Accelerating voltage V (V): "))
a = float(input("Lattice constant a (nm): ")) * 1e-9

lam = h / math.sqrt(2 * m_e * e * V)
m_max = int(2 * a / lam)

print("Problem 6.41")
print(f"  V = {V:.1f} V")
print(f"  a = {a*1e9:.3f} nm")
print(f"  λ = {lam:.4e} m ({lam*1e9:.4f} nm)")
print(f"  m_max = {m_max}")