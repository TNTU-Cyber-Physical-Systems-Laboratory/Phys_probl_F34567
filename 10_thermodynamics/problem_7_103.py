import sys
sys.stdout.reconfigure(encoding='utf-8')

R = 8.314

m = float(input("Enter mass m (g): ")) * 1e-3
M_Ar = float(input("Enter molar mass M (g/mol): ")) * 1e-3
T1 = float(input("Enter initial temperature T1 (K): "))
p1 = float(input("Enter initial pressure p1 (Pa): "))
p2 = float(input("Enter final pressure p2 (Pa): "))
i = int(input("Degrees of freedom i: "))

gamma = (i + 2) / i
nu = m / M_Ar

pressure_ratio = p2 / p1

T2 = T1 * pressure_ratio ** ((gamma - 1) / gamma)
V1_over_V2 = pressure_ratio ** (1 / gamma)

W = (nu * R * (T1 - T2)) / (gamma - 1)

print("\nProblem 7.103")
print(f"  m = {m * 1e3:.0f} g, nu = {nu:.2f} mol")
print(f"  gamma = {gamma:.4f} (i = {i})")
print(f"  T1 = {T1:.1f} K, p1 = {p1:.2e}, p2 = {p2:.2e}")
print(f"  p2/p1 = {pressure_ratio:.2e}")
print()
print(f"  T2 = {T2:.1f} K")
print(f"  V1/V2 = {V1_over_V2:.2f}")
print(f"  W = {W:.1f} J ({W / 1e3:.2f} kJ)")