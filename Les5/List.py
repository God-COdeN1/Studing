# your_list = [2, 8, False, None, 'Hi', 7.2, [input("Yor like number"), 5]]
# print(your_list)
# print(your_list[-1][1])
# print(type(your_list))

# number = input("Name")
# print(number.split(" "))
#
x = [3, 3, 4, 4]
x.append(3) #Добавляємо значення в  список
x.insert(2, 2222) #Добавляємо обєкт в вказаний індекс
x[3] = 2123 #змінюємо обєкт листа за індексом
x.extend([2, 23, 23,323]) #Добавляємо(розширюємо список)
# x.sort() # Сортруємо
# x.reverse() # Перевиртаємо
for el in x:
    el /= 2
    print(el)
print(x.count(3)) #Рахуємо обєкт який вказали в джуках
print(len(x)) #Елементи списка
print(x)
x.pop(3) #Удаляємо за індексом
print(x)
x.remove(2) #Удаляємо значення або об'єкт
print(x)
x.clear() #Чисте список
print(x)
print(len(x))

