import math
import sys
sys.stdout.reconfigure(encoding='utf-8')


lam = float(input("Enter wavelength lambda (nm): ")) * 1e-9
D = float(input("Enter aperture diameter D (mm): ")) * 1e-3
b = float(input("Enter screen distance b (m): "))

r = D / 2
m = r**2 / (lam * b)

print("Problem 13.18")
print(f"  Wavelength lambda = {lam * 1e9:.0f} nm")
print(f"  Aperture diameter D = {D * 1e3:.0f} mm (radius r = {r * 1e3:.1f} mm)")
print(f"  Screen distance b = {b:.0f} m")
print(f"  Number of Fresnel zones: m = r^2 / (lambda * b) = {m:.1f}")
print()

m_int = round(m)

if m_int % 2 == 1:
    centre = "BRIGHT (odd number of zones - amplitudes add up)"
else:
    centre = "DARK (even number of zones - amplitudes partially cancel)"

print(f"  m ~= {m_int} ({'odd' if m_int % 2 else 'even'}) => centre is {centre}")