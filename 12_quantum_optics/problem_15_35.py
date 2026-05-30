import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
c = 3e8
e = 1.6e-19

lam = float(input("lambda (m): "))

E = h*c/lam
m = E/c**2
p = h/lam

print("Problem 15.35")
print(f"  lambda = {lam:.3e} m")
print(f"  E = {E:.4e} J")
print(f"  m = {m:.4e} kg")
print(f"  p = {p:.4e} kg*m/s")