import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

hbar = 1.0546e-34
h = 6.626e-34
e = 1.6e-19
m_e = 9.11e-31
c = 3e8
k_B = 1.38e-23

dx = float(input("Delta x (nm): ")) * 1e-9

dp = hbar / dx
E_min = dp**2 / (2 * m_e)

print("Problem 17.13")
print(f"  Δx = {dx*1e9:.2f} nm")
print(f"  Δp_min = ħ/Δx = {dp:.4e} kg·m/s")
print(f"  E_min = Δp²/(2m) = {E_min:.4e} J ({E_min/e:.2f} eV)")