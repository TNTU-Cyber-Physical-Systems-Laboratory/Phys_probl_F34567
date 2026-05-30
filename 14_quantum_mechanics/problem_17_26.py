import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

hbar = 1.0546e-34
h = 6.626e-34
e = 1.6e-19
m_e = 9.11e-31
c = 3e8
k_B = 1.38e-23

L = float(input("Box length L (nm): ")) * 1e-9
T1 = float(input("T1 (K): "))
T2 = float(input("T2 (K): "))

E1 = (math.pi**2 * hbar**2) / (2 * m_e * L**2)

def n_from_T(T):
    return math.sqrt(k_B * T / E1)

n1 = round(n_from_T(T1))
n2 = round(n_from_T(T2))

def psi_center(n, L):
    return (2 / L) * math.sin(n * math.pi / 2)**2

P1 = psi_center(n1, L)
P2 = psi_center(n2, L)

print("Problem 17.26")
print(f"  L = {L*1e9:.2f} nm")
print(f"  n1 ≈ {n1}, n2 ≈ {n2}")
print(f"  P(L/2): {P1:.3e}, {P2:.3e}")