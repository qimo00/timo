#占用一个外部变量i
for i in range(100,1000):
    a=i//100
    b=(i//10)%10
    c=i%10
    if i==a**3+b**3+c**3:
        print(i,'is the number')
    i+=1
#i只在循环内部定义。所有运算都在循环内部
for i in range(100,1000):
    sum=0
    temp=i
    while temp:
        sum=sum+(temp%10)**3
        temp=temp//10
    if sum==i:
        print(i)
