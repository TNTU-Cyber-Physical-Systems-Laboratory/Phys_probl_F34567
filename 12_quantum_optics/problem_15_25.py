import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
c = 3e8
m_e = 9.11e-31
e = 1.6e-19

lam_C = h/(m_e*c)

lam0 = float(input("lambda0 (pm): ")) * 1e-12

theta = math.pi/2

delta_lam = lam_C*(1 - math.cos(theta))
lam1 = lam0 + delta_lam

E0 = h*c/lam0
E1 = h*c/lam1

Ek = E0 - E1

p0 = h/lam0
p1 = h/lam1

p_e = math.sqrt(p0**2 + p1**2 - 2*p0*p1*math.cos(theta))

print("Problem 15.25")
print(f"  lambda0 = {lam0*1e12:.1f} pm")
print(f"  theta = 90 deg")

print(f"  lambda_C = {lam_C*1e12:.3f} pm")
print(f"  delta lambda = {delta_lam*1e12:.3f} pm")
print(f"  lambda' = {lam1*1e12:.3f} pm")

print(f"  Ek = {Ek:.4e} J ({Ek/e:.2f} eV)")
print(f"  p_e = {p_e:.4e} kg*m/s")