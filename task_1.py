# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
import math
from math import factorial
import numpy as np


n = 100
k = 85
p = 0.8

def comb(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

c = comb(n, k)

P = (c * p**k * 0.2**15)

print(f'Вероятность того, что стрелок попадет 85 раз равна: {round(P, 3)} или {round(P, 3)*100}%')
