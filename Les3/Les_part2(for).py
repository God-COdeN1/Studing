# for number in range(1, 10, 2):
#     print(number)

#Знайшов пеший символ в змінній
your_name = input("Print your name: ")
for name in your_name:
    if name.split("\n")[0] == "A":
        print("Your name start in letter A")
        # exit()
    else:
        print("Your name start in different letter")
        # exit()

count = 0
srt_in = "Hello world"
for world in srt_in:
    if world == "l":
        count += 1
print("Count:", count)