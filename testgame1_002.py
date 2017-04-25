#初始化
import random
ans=random.randint(1,10)
times=3

while times>0 :

    # 输入数字
    temp = input('guess a number:')
    while not temp.isdigit():
        print("input is not a number")
        temp = input("input another number:")
    guess=int(temp)
    times -= 1  #输入一次，可用次数-1

    # 检测：...
    if guess==ans:
        print("you are right!!!!!")
        break
    else:
        if guess>ans:
            print("your number is big")
        elif guess<ans:
            print("your number is small")
        print("you are worng,you have %d times now" % times)

print("game is over")



