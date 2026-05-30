import sys
sys.stdout.reconfigure(encoding='utf-8')

R = 8.314

m = float(input("Mass m (g): ")) * 1e-3
T1 = float(input("T1 (K): "))
T2 = float(input("T2 (K): "))
Q = float(input("Q (J): "))

delta_T = T2 - T1

c = Q / (m * delta_T)

C_mol = 3 * R

M = C_mol / c

metals = {
    "Aluminium (Al)": 27e-3,
    "Iron (Fe)": 56e-3,
    "Copper (Cu)": 63.5e-3,
    "Zinc (Zn)": 65.4e-3,
    "Silver (Ag)": 108e-3,
    "Lead (Pb)": 207e-3,
}

print("Problem 7.216")
print(f"  m = {m*1e3:.0f} g, T1 = {T1:.1f}, T2 = {T2:.1f}, Q = {Q:.1f}")
print(f"  c = Q / (m*DeltaT) = {c:.2f} J/(kg*K)")
print(f"  C_mol = 3R = {C_mol:.2f}")
print(f"  M = {M*1e3:.1f} g/mol")

best = None
best_diff = 1e9

print("\nClosest match:")

for name, M_ref in metals.items():
    diff = abs(M - M_ref) / M_ref * 100
    if diff < best_diff:
        best_diff = diff
        best = name
    print(f"  {name}: {M_ref*1e3:.1f} g/mol ({diff:.1f}%)")

print(f"\nBest match: {best}")