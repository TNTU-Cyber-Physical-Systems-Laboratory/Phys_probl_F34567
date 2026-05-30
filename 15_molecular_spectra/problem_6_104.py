import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Problem 6.104\n")

l = int(input("Enter l (e.g. 1 for p-orbital): "))
s = 0.5

# Спектроскопічні літери
spectroscopic_letters = {
    0: "S",
    1: "P",
    2: "D",
    3: "F",
    4: "G",
    5: "H",
    6: "I",
    7: "K"
}

letter = spectroscopic_letters.get(l, "?")

j_values = sorted({abs(l - s), l + s})

print("\nTotal angular momentum j values:")
for j in j_values:
    print(f"  j = {j}")

print("\nSpectroscopic notation:")
for j in j_values:
    print(f"  ^2{letter}_(j={j})")

n_min = int(input("\nEnter minimum n: "))
n_max = int(input("Enter maximum n: "))

print("\nStates:")
for n in range(n_min, n_max + 1):
    for j in j_values:
        print(f"  n={n}, l={l}, j={j} -> {n}{letter}_{j}")