# Убираємо пробіл
print(3, 23, 24, "Hello")
print(3, 23, 24, "Hello", sep="///")

# Одна строка
print(3, 23, 24, "Hello", sep="-", end="! \n")
print(3, 23, 24, "Hello", sep="-", end="-")
print(3, 23, 24, "Hello")

# Спец символи
print('Hello, i\'am Bynny and\nnew storoke')
print("Тут нема\tпробілу", "\n1\\")

# Степінь, остаток при діленні і ділення
print(5 // 3, 3 ** 2, 28 % 5)
x = 1
y = -2
z = 235
print(min(x, y, z, -234, ), max(23, 123, z, x, y))
# Доп фун
print("Модуль", abs(-5), "\nстепінь", pow(5, 2, ), "\nБез остачі", round(5 / 3))
