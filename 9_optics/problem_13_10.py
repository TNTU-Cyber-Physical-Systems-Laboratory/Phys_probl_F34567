import sys
sys.stdout.reconfigure(encoding='utf-8')

lambda_nm = float(input("Enter wavelength lambda (nm): ")) * 1e-9
n_film = float(input("Enter film refractive index: "))
n_glass = float(input("Enter glass refractive index: "))

d_min = lambda_nm / (4 * n_film)

print("Problem 13.10")
print(f"  n_film  = {n_film}")
print(f"  n_glass = {n_glass}")
print(f"  lambda  = {lambda_nm * 1e9:.0f} nm")
print("  Both reflections have pi phase shift -> condition: 2*n*d = (m+1/2)*lambda")
print("  Minimum thickness (m = 0): d = lambda / (4 * n_film)")
print(f"  d_min = {d_min * 1e9:.2f} nm")