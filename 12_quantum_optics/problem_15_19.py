import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
c = 3e8
e = 1.6e-19

lam = float(input("lambda (nm): ")) * 1e-9
lam_red = float(input("lambda_red (nm): ")) * 1e-9

if lam >= lam_red:
    E_kin_J = 0.0
    E_kin_eV = 0.0
else:
    E_kin_J = h * c * (1/lam - 1/lam_red)
    E_kin_eV = E_kin_J / e

print("Problem 15.19")
print(f"  lambda_red = {lam_red*1e9:.0f} nm")
print(f"  lambda = {lam*1e9:.0f} nm")

print(f"  Ek = {E_kin_J:.4e} J = {E_kin_eV:.2f} eV")