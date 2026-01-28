import math as m
n1 = float(input('Введіть кількість коливань в досліді №1:'))
n2 = float(input('Введіть кількість коливань в досліді №2:'))
n3 = float(input('Введіть кількість коливань в досліді №3:'))

t1 = float(input('Введіть час коливань в досліді №1(в с):'))
t2 = float(input('Введіть час коливань в досліді №2(в с):'))
t3 = float(input('Введіть час коливань в досліді №3(в с):'))

a11 = float(input('Введіть початковий кут відхилення від положення рівноваги в досліді №1(в градусах):'))
a12 = float(input('Введіть початковий кут відхилення від положення рівноваги в досліді №2(в градусах):'))
a13 = float(input('Введіть початковий кут відхилення від положення рівноваги в досліді №3(в градусах):'))

a21 = float(input('Введіть кінцевий кут відхилення від положення рівноваги в досліді №1(в градусах):'))
a22 = float(input('Введіть кінцевий кут відхилення від положення рівноваги в досліді №2(в градусах):'))
a23 = float(input('Введіть кінцевий кут відхилення від положення рівноваги в досліді №3(в градусах):'))

ns = (n1 + n2 + n3) / 3
ts = (t1 + t2 + t3) / 3
as1 = (a11 + a12 + a13) / 3
as2 = (a21 + a22 + a23) / 3


dt3 = abs(ts-t3)
dt2 = abs(ts-t2)
dt1 = abs(ts-t1)

da13 = abs(as1-a13)
da12 = abs(as1-a12)
da11 = abs(as1-a11)

da23 = abs(as2-a23)
da22 = abs(as2-a22)
da21 = abs(as2-a21)


dts = (dt1 + dt2 + dt3) / 3

da1s = (da11 + da12 + da13) / 3
da2s = (da21 + da22 + da23) / 3

beta1 = (1 / t1) * m.log(a11 / a21)
beta2 = (1 / t2) * m.log(a12 / a22)
beta3 = (1 / t3) * m.log(a13 / a23)
betas = (beta1 + beta2 + beta3) / 3

dbeta1 = abs(betas - beta1)
dbeta2 = abs(betas - beta2)
dbeta3 = abs(betas - beta3)
dbetas = (dbeta1 + dbeta2 + dbeta3) / 3

lambda1 = (1 / n1) * m.log(a11 / a21)
lambda2 = (1 / n2) * m.log(a12 / a22)
lambda3 = (1 / n3) * m.log(a13 / a23)
lambdas = (lambda1 + lambda2 + lambda3) / 3

dlambda1 = abs(lambdas - lambda1)
dlambda2 = abs(lambdas - lambda2)
dlambda3 = abs(lambdas - lambda3)
dlambdas = (dlambda1 + dlambda2 + dlambda3) / 3

elambdas = dlambdas / lambdas * 100
ebetas = dbetas / betas * 100

print(f"Середній час коливань у дослідах {ts} с")
print(f"Середня кількість коливань у дослідах {ns}")
print(f"Δt1 = {dt1} с, Δt2 = {dt2} с, Δt3 = {dt3} с.")
print(f"ΔA11 = {da11} с, ΔA12 = {da12} с, ΔtA13 = {da13} с, ΔtA1с = {da1s} с.")
print(f"ΔA22 = {da21} с, ΔA22 = {da22} с, ΔtA23 = {da23} с, ΔtA2с = {da2s} с.")

print(f'Логарифмічний декремент {lambdas} ')
print(f'Коефіцієнт згасання коливань {betas} с^-1')
print(f'Похибка логарифмічного декремента {dlambdas} ')
print(f'Похибка коефіцієнта згасання коливань {dbetas} с^-1')
print(f'Відносна похибка логарифмічного декремента: {elambdas} %')
print(f'Відносна похибка коефіцієнта згасання коливань: {ebetas} %')
