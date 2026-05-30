import sys
sys.stdout.reconfigure(encoding='utf-8')

sigma = 5.67e-8

T = float(input("T (K): "))
M_grey_kJ_per_m2_per_h = float(input("M (kJ/m^2*h): "))

M_grey = M_grey_kJ_per_m2_per_h * 1e3 / 3600

epsilon = M_grey / (sigma * T**4)

print("Problem 14.35")
print(f"  T = {T:.1f} K")
print(f"  M = {M_grey:.2f} W/m^2")
print(f"  sigma*T^4 = {sigma*T**4:.2f} W/m^2")
print(f"  epsilon = {epsilon:.3f}")