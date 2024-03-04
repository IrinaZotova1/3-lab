n = int(input("ведиет количество слов: "))
rez = ""
for i in range(n):
    sl = input("ведиет слова:")
    rez = rez + sl + " "
print(rez)