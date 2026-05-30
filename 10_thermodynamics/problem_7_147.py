import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

R = 8.314

nu = float(input("nu (mol): "))
T1 = float(input("T1 (K): "))
T2 = float(input("T2 (K): "))
V_ratio = float(input("Vmax/Vmin: "))
gamma = float(input("gamma: "))

eta = 1 - T2 / T1

adiabatic_ratio = (T1 / T2) ** (1 / (gamma - 1))

x = V_ratio / adiabatic_ratio

Q1 = nu * R * T1 * math.log(x)

W = eta * Q1

print("Problem 7.147")
print(f"  T1 = {T1:.1f} K, T2 = {T2:.1f} K")
print(f"  Vmax/Vmin = {V_ratio}")
print(f"  gamma = {gamma}")

print(f"  Adiabatic ratio = {adiabatic_ratio:.3f}")
print(f"  Isothermal x = {x:.4f}")

print(f"  Q1 = nu*R*T1*ln(x) = {Q1:.1f} J ({Q1/1e3:.3f} kJ)")
print(f"  W  = eta*Q1 = {W:.1f} J ({W/1e3:.3f} kJ)")
print(f"  eta = {eta:.2f} ({eta*100:.1f}%)")