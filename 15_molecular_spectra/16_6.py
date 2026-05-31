import sys
sys.stdout.reconfigure(encoding='utf-8')

R_H = 1.097e7

visible_min = 380e-9
visible_max = 700e-9

print("=" * 50)
print("Задача 16.6")
print("=" * 50)

n_start = int(input("Enter n start (>=3): "))
n_end = int(input("Enter n end: "))

if n_start < 3:
    n_start = 3

count = 0

for n in range(n_start, n_end + 1):  # включаємо n_end
    inv_lam = R_H * (1 / 4 - 1 / n**2)
    lam = 1 / inv_lam

    if visible_min <= lam <= visible_max:
        count += 1
        print(f"n={n}  →  λ = {lam * 1e9:.1f} нм  (видима)")
    elif lam < visible_min:
        break

print(f"\nКількість ліній серії Бальмера у видимій області: {count}")