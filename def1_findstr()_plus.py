#使用for语句进行字符串识别
def findstr(target,sorce):
    len_s=len(sorce)
    len_t=len(target)
    times=0
    for i in range(len_s-len_t):
        ans=0
        for j in range(len_t):
            if sorce[i]==target[j]:
                i+=1
                ans+=1
            else:
                break
        if ans==len_t:
            times+=1




    print(target,'出现',times,'次')
    return times

target=input('input the target')
sorce=input ('input the sorce')
findstr(target=target,sorce=sorce)
