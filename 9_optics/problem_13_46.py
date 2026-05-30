import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

phi_deg = float(input("Enter angle phi (deg): "))
absorption = float(input("Enter absorption (0-1): "))

if not (0 <= absorption <= 1):
    raise ValueError("Absorption must be between 0 and 1.")

phi_rad = math.radians(phi_deg)
cos2 = math.cos(phi_rad) ** 2

I1_over_I0 = 0.5 * (1 - absorption)
I2_over_I1 = cos2 * (1 - absorption)
I2_over_I0 = I1_over_I0 * I2_over_I1

print("Problem 13.46")
print(f"  Angle between principal planes: phi = {phi_deg:.0f} deg")
print(f"  Absorption in each Nicol: {absorption * 100:.0f} %")
print(f"  cos^2(phi) = {cos2:.4f}")
print(f"  After 1st Nicol: I1/I0 = {I1_over_I0:.4f}")
print(f"  After 2nd Nicol: I2/I0 = {I2_over_I0:.5f}")

if I2_over_I0 == 0:
    print("  Attenuation factor I0/I2 = infinity (no transmitted light)")
else:
    attenuation = 1.0 / I2_over_I0
    print(f"  Attenuation factor I0/I2 = {attenuation:.1f}")