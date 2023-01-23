# 4. В первом ящике 1() находится 10 мячей, из которых 7 - белые, 3 - черные.
# Во втором ящике 2() - 11 мячей, из которых 9 белых и 2 черных.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# а) Какова вероятность того, что все мячи белые?
# б) Какова вероятность того, что ровно два мяча белые?
# в) Какова вероятность того, что хотя бы один мяч белый?


first = 7 / 10 * 6 / 9
second = 9 / 11 * 8 / 10
p = first * second
print(f'Вероятность того, что все мячи белые: {round(p, 3)} или {round(p, 3)*100}%')

p = (7 / 10 * 3 / 9 + 3 / 10 * 7 / 9) * (9 / 11 * 2 / 10 + 2 / 11 * 9 / 10) \
          + 3 / 10 * 2 / 9 * 9 / 11 * 8 / 10 + 7 / 10 * 6 / 9 * 2 / 11 * 1 / 10
print(f'Вероятность того, что ровно два мяча белые: {round(p, 3)} или {round(p, 3)*100}%')

first = 3 / 10 * 2 / 9
second = 2 / 11 * 1 / 10
p = 1 - first * second
print(f'Вероятность того, что хотя бы один мяч белый: {round(p, 3)} или {round(p, 3)*100}%')
