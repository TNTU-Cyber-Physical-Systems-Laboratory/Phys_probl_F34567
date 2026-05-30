import sys
sys.stdout.reconfigure(encoding='utf-8')

h = 6.626e-34
c = 3e8
e = 1.6e-19

print("Problem 16.14\n")

lam_nm = float(input("Wavelength (nm): "))
n_i = int(input("Initial level n_i: "))
n_f = int(input("Final level n_f: "))

lam = lam_nm * 1e-9

E_J = h * c / lam
E_eV = E_J / e

KE_i = 13.6 / n_i**2
KE_f = 13.6 / n_f**2

dKE = KE_f - KE_i

print(f"\nPhoton energy = {E_eV:.3f} eV")
print(f"KE(n={n_i}) = {KE_i:.4f} eV")
print(f"KE(n={n_f}) = {KE_f:.4f} eV")
print(f"ΔKE = {dKE:.4f} eV")