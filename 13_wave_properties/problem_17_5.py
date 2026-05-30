import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
m_p = 1.67e-27
e = 1.6e-19

energies = [1.0, 1e3]  # eV, keV

print("Problem 17.5")
print("λ = h / sqrt(2mE)\n")

for E_eV in energies:
    E = E_eV * e
    lam = h / math.sqrt(2 * m_p * E)

    value = E_eV/1000 if E_eV >= 1000 else E_eV
    unit = "keV" if E_eV >= 1000 else "eV"

    print(f"  E = {value:.0f} {unit}: λ = {lam:.4e} m ({lam*1e12:.2f} pm)")