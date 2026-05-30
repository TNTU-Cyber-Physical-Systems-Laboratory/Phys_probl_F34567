import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

hbar = 1.0546e-34
h = 6.626e-34
e = 1.6e-19
m_e = 9.11e-31

E = float(input("E (eV): "))
U0 = float(input("U0 (eV): "))

if U0 <= E:
    print("No tunneling barrier: particle is not in classically forbidden region.")
    sys.exit(0)

# decay constant in barrier
kappa = math.sqrt(2 * m_e * (U0 - E) * e) / hbar

rhs = 2 * math.sqrt(E * (U0 - E)) / U0

kL = math.asinh(rhs)
L = kL / kappa

print("Problem 17.30")
print(f"  E = {E:.2f} eV")
print(f"  U0 = {U0:.2f} eV")
print(f"  κ = {kappa:.4e} m⁻¹")
print(f"  L = {L:.4e} m")