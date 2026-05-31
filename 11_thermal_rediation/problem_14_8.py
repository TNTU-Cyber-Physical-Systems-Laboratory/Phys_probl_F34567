import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

sigma = 5.67e-8

T_sun = float(input("T_sun (K): "))
R_sun = float(input("R_sun (m): "))
d_SE = float(input("d_SE (m): "))

exitance = sigma * T_sun**4

solar_constant = exitance * (R_sun / d_SE) ** 2

print("Problem 14.8")
print(f"  T_sun = {T_sun:.0f} K")
print(f"  R_sun = {R_sun:.3e} m")
print(f"  d_SE = {d_SE:.3e} m")
print(f"  M = sigma*T^4 = {exitance:.3e} W/m^2")
print(f"  S = M*(R/d)^2 = {solar_constant:.1f} W/m^2")