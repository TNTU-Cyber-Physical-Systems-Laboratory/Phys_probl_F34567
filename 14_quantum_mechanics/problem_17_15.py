import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

hbar = 1.0546e-34
h = 6.626e-34
e = 1.6e-19
m_e = 9.11e-31
c = 3e8
k_B = 1.38e-23

t = float(input("lifetime t (ns): ")) * 1e-9
lam = float(input("wavelength λ (nm): ")) * 1e-9

dE = hbar / t
dnu = dE / h
dlam = (lam**2 / c) * dnu

print("Problem 17.15")
print(f"  τ = {t:.2e} s")
print(f"  ΔE = ħ/τ = {dE:.4e} J")
print(f"  Δν = ΔE/h = {dnu:.4e} Hz")
print(f"  Δλ = {dlam:.4e} m ({dlam*1e12:.4f} pm)")