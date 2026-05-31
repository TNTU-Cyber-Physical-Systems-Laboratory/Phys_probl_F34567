import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
m_p = 1.67e-27
e = 1.6e-19

energies_input = input("Enter proton kinetic energies in eV, separated by spaces (e.g. 1 1000): ")

energies = [float(value) for value in energies_input.split()]


print("Problem 17.5")
print("λ = h / sqrt(2mE)\n")

for E_eV in energies:
    E = E_eV * e
    print(f"  E = {E_eV:g} eV: λ = {lam:.4e} m ({lam*1e12:.2f} pm)")

    print(f"  E = {value:.0f} {unit}: λ = {lam:.4e} m ({lam*1e12:.2f} pm)")