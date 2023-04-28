#Version for
list1 = input("Введіть кількість обєктів списка ")
ls = []
y = 0
for i in range(int(list1)):
    num = input("Число для списка №" + str(y + 1) + ": ")
    ls.append(num)
    y += 1
print(ls)

# Version while
list2 = int(input("Введіть кількість обєктів списка "))
ls1 = []
y1 = 0
while True:
    if list2 > y1:
        num1 = input("Число для списка №" + str(y1 + 1) + ": ")
        ls1.append(num1)
        y1 += 1
    else:
        break
print(ls1)
