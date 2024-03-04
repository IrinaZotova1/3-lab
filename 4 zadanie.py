import random

otv = 0
flag = 0
while flag != 3:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    aa = str(a)
    bb = str(b)
    primer = aa + "+" + bb + "="
    c = int(input(primer))
    if a + b == c:
        print("Правильно!")
        flag = 0
        otv = otv + 1
    else:
        print("Ответ неверный!")
        flag = flag + 1
print("Игра окончена. Правильных ответов:", otv)
