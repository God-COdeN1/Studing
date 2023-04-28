inp = input("Your num: ")
for num in inp:
    print(type(num), num)
    if num == "6":
        print("Num 6 founded")
        break
    elif num == "3":
        print("Num 3 skip")
        continue
# break для тогго щоб остановити, continue для того щоб пропустити