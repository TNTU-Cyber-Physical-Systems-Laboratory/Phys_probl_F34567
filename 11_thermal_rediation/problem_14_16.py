import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

sigma = 5.67e-8
b = 2.898e-3

T1 = float(input("T1 (K): "))
T2 = float(input("T2 (K): "))

M_ratio = (T2 / T1) ** 4

lam1 = b / T1
lam2 = b / T2

delta_lam = lam1 - lam2

M_max_ratio = (T2 / T1) ** 5

print("Problem 14.16")
print(f"  T1 = {T1:.0f} K, T2 = {T2:.0f} K")

print(f"  M2/M1 = (T2/T1)^4 = {M_ratio:.0f}")

print(f"  lambda_max(T1) = {lam1*1e6:.2f} um")
print(f"  lambda_max(T2) = {lam2*1e6:.3f} um")
print(f"  delta lambda = {delta_lam*1e6:.4f} um ({delta_lam*1e9:.1f} nm)")

print(f"  M_max ∝ T^5 => ratio = {M_max_ratio:.0f}")