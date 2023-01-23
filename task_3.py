# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial

def comb(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n = 144
p = 1 / 2
k = 70
q = 1 - p

P = comb(n, k) * p**k * q**(n-k)
print(f'Вероятность, что орел выпадет ровно 70 раз равна: {round(P, 3)} или {round(P, 3)*100}%')
