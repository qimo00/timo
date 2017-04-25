def flowers():
    for i in range(100,1000):
        sum=0
        num=i
        while num!=0:
            sum+=(num%10)**3
            num=num//10
        if sum==i:
            print(i,'is a flower')
    return

flowers()