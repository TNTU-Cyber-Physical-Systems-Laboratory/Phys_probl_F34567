import sys, math
sys.stdout.reconfigure(encoding='utf-8')

print("Problem 18.13\n")

hbar = 1.0546e-34
m_e = 9.11e-31
e = 1.6e-19
N_A = 6.022e23

rho = float(input("Density ρ (kg/m^3): "))
M = float(input("Molar mass M (kg/mol): "))

n = rho * N_A / M

E_F = (hbar**2 / (2*m_e)) * (3*math.pi**2*n)**(2/3)
E_avg = (3/5) * E_F
P = (2/3) * n * E_avg

print(f"\nn = {n:.4e} m^-3")
print(f"E_F = {E_F:.4e} J ({E_F/e:.2f} eV)")
print(f"P = {P:.4e} Pa")