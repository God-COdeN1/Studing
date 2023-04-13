import re

while True:
    number1 = input('Введіть число №1: ')
    number2 = input('Введіть число №2: ')

    def contains_only_digits_and_dot(text):
        pattern = r'^\d+(\.\d+)?$'
        return bool(re.match(pattern, text))

    if contains_only_digits_and_dot(number1) and contains_only_digits_and_dot(number2):
        num1 = float(number1)
        num2 = float(number2)
        result_add = "{:.3f}".format(num1 + num2).rstrip('0').rstrip('.')
        result_sub = "{:.3f}".format(num1 - num2).rstrip('0').rstrip('.')
        result_mul = "{:.3f}".format(num1 * num2).rstrip('0').rstrip('.')
        if num2 == 0:
            result_div = "На нуль ділити не можна"
        else:
            result_div = "{:.3f}".format(num1 / num2).rstrip('0').rstrip('.')
        print("Додавання: {}".format(result_add))
        print("Віднімання: {}".format(result_sub))
        print("Множення: {}".format(result_mul))
        print("Ділення: {}".format(result_div))
        while True:
            num = input("Введіть q для виходу або 'r' для перезапуску: ")
            if num.lower() == "q":
                exit()
            elif num.lower() == "r":
                break
            try:
                num = int(num)
                print(num ** 2)
            except ValueError:
                print("Будь ласка, введіть 'q' для виходу або 'r' для перезапуску.")
        continue

