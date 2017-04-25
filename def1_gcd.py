#欧几里得算法，即辗转相除法：
#两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数
def gcd(x,y):
    t=x%y
    x=y
    y=t
    if y!=0:
        x=gcd(x,y)
    return x

print(gcd(15,35))