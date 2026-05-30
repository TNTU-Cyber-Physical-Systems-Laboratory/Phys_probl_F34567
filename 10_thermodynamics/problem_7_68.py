import sys
sys.stdout.reconfigure(encoding='utf-8')

R = 8.314

m = float(input("Enter mass m (g): ")) * 1e-3
M = float(input("Enter molar mass M (g/mol): ")) * 1e-3
T = float(input("Enter temperature T (K): "))
i = int(input("Enter degrees of freedom i: "))

nu = m / M
U = (i / 2) * nu * R * T

print("Problem 7.68")
print(f"  Mass m = {m * 1e3:.0f} g, Molar mass M = {M * 1e3:.0f} g/mol")
print(f"  nu = m/M = {nu:.3f} mol")
print(f"  Degrees of freedom i = {i}")
print(f"  T = {T:.0f} K")
print(f"  U = (i/2)*nu*R*T = {U:.1f} J ({U / 1e3:.3f} kJ)")