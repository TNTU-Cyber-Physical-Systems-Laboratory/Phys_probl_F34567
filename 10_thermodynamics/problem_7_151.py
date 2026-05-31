import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

T_min = float(input("Enter T_min (K): "))
T_max = float(input("Enter T_max (K): "))

eta = 1 - T_min * math.log(T_max / T_min) / (T_max - T_min)

print("Problem 7.151")
print(f"  T_min = {T_min:.1f} K, T_max = {T_max:.1f} K")
print("  Cycle: 1->2 isochoric, 2->3 adiabatic, 3->1 isothermal")
print("  eta = 1 - T_min * ln(T_max/T_min) / (T_max - T_min)")
print(f"  eta = {eta:.4f} ({eta*100:.2f} %)")