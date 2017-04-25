def bin_1(x):
    temp=x
    result=[]
    ans=''
    while temp!=1:
        yushu=temp%2
        temp = temp // 2
        result.insert(0,yushu)
    result.insert(0,temp)
    for each in result:
        ans+=str(each)
    print(type(ans))
    return ans

print(bin_1(19))
