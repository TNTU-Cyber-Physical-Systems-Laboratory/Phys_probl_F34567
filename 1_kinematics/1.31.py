import math as m


al = float(input('Кут альфа:')) * m.pi / 180
bet = float(input('Кут бета:')) * m.pi / 180

while bet == 0:
    bet = float(input('Кут бета не може дорівнювати нулю введіть ще раз.')) * m.pi / 180

g = 9.8
v0 = float(input('Початкова швидкість:'))

t1 = round((v0 * m.sin(al) - m.tan(bet) * v0 * m.cos(al)) / g, 4)
t2 = round((v0 * m.sin(al) + m.tan(bet) * v0 * m.cos(al)) / g, 4)

if t1 == t2:
    print(t1)
else:
    print(f"t1={t1}c, t2={t2}c.")
