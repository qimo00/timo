temp=input('guess a number:')
while not temp.isdigit():
    print("input is not a number")
    temp=input("input another number:")

guess=int(temp)


if guess==8:
    print("gooooooooooooood~~~~~~~~~!!!!!!!")
else:
    print("worng..........")

