user_Happy = int(input("Якщо ви щасливий нажміть 1 "))
if user_Happy == 1:
    print("Користувач щасливий")
elif user_Happy == 2:
    print("Pres to one")
else:
    user_Happy = True
print(type(user_Happy))
print("---\n---\n---\n---\n")
# if user_Happy == True:
#     print("Чому?")
#     print(user_Happy)


its_num = True if user_Happy == 1 else False
print(its_num)

