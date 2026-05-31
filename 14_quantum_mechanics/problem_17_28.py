import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

hbar = 1.0546e-34
h = 6.626e-34
e = 1.6e-19
m_e = 9.11e-31
c = 3e8
k_B = 1.38e-23

n1 = int(input("n1: "))
n2 = int(input("n2: "))

def gap(n):
    return 2*n + 1

g1 = gap(n1)
g2 = gap(n2)

print("Problem 17.28")
print(f"  ΔE_n = (2n+1)E1")
print(f"  ratio = {g1/g2:.4f}")