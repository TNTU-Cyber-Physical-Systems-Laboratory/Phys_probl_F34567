import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

sigma = 5.67e-8
b = 2.898e-3

P = float(input("P (W): "))
lam_max = float(input("lambda_max (nm): ")) * 1e-9

T = b / lam_max

A = P / (sigma * T**4)

print("Problem 14.12")
print(f"  lambda_max = {lam_max*1e9:.0f} nm")
print(f"  T = b/lambda_max = {T:.1f} K")
print(f"  P = {P/1e3:.2f} kW")
print(f"  A = {A:.4e} m^2 ({A*1e4:.2f} cm^2)")