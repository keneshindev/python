b=int(input())
total=0
for i in range(1, b):
    if b % i == 0:
        total+=i
print("Да" if total==0 else "Нет")
#Числа для проверки
#6
#28
#496
#8128
