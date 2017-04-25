def bin(x):
    ans=''
    str1=''
    if x>=2:
        str1 = bin(x // 2)
        str1 = str1 + str(x % 2)
        return str1
    else:
        str1=str1+str(x)
        return str1

print(bin(13))