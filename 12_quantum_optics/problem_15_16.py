import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
e = 1.6e-19

nu0 = float(input("nu0 (Hz): "))
V0 = float(input("V0 (V): "))

A = h * nu0
nu = nu0 + (e * V0) / h

A_eV = A / e
E_eV = h * nu / e

print("Problem 15.16")
print(f"  V0 = {V0:.2f} V")
print(f"  nu0 = {nu0:.2e} Hz")

print(f"  A = h*nu0 = {A:.4e} J ({A_eV:.3f} eV)")
print(f"  nu = {nu:.4e} Hz")
print(f"  E = h*nu = {h*nu:.4e} J ({E_eV:.2f} eV)")