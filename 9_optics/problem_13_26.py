import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

slits_per_mm = float(input("Enter slits per mm: "))
m = int(input("Diffraction order m (non-zero integer): "))
total_angle_deg = float(input("Total angle (deg): "))

if m == 0:
    print("Error: diffraction order m cannot be 0.")
    sys.exit(1)
m = abs(m)

d = 1e-3 / slits_per_mm
theta_deg = total_angle_deg / 2
theta_rad = math.radians(theta_deg)

lam = d * math.sin(theta_rad) / m

print("Problem 13.26")
print(f"  Grating period d = {d * 1e6:.1f} um")
print(f"  Diffraction order m = {m}")
print(f"  Total rotation angle = {total_angle_deg:.0f} deg => theta = {theta_deg:.0f} deg")
print("  Grating equation: d * sin(theta) = m * lambda")
print(f"  lambda = d * sin(theta) / m = {lam * 1e9:.1f} nm")