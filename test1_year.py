year=int(input("input a year:"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            temp=1
        else:
            temp=0
    else:
        temp=1
else:
    temp=0

if temp==0:
    print("is notttt")
else:
    print("is trueeee")