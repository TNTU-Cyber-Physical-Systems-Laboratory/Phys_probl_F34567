import sys
sys.stdout.reconfigure(encoding='utf-8')

kappa = float(input("Thermal conductivity kappa (W/m*K): "))
A = float(input("Area A (m^2): "))
d = float(input("Thickness d (m): "))
T_in = float(input("T_in (K): "))
T_out = float(input("T_out (K): "))
t = float(input("Time t (s): "))

delta_T = T_in - T_out

Q = kappa * A * (delta_T / d) * t

print("Problem 7.139")
print(f"  Thickness d = {d:.3f} m")
print(f"  T_in = {T_in:.1f} K, T_out = {T_out:.1f} K, DeltaT = {delta_T:.1f} K")
print(f"  kappa = {kappa:.3f} W/(m*K), A = {A:.3f} m^2, t = {t:.0f} s")
print("  Q = kappa * A * (DeltaT / d) * t")
print(f"  Q = {Q:.0f} J ({Q/1e3:.1f} kJ) ({Q/1e6:.3f} MJ)")