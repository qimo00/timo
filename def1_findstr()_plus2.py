#使用while语句进行多位字符串识别
def findstr(target,sorce):
    len_s=len(sorce)
    len_t=len(target)
    times=0
    i=0
    while i<=len_s-len_t:
        k=i
        ans=0
        for j in range(len_t):
            if sorce[k]==target[j]:
                k+=1
                ans+=1
            else:
                break
        if ans==len_t:
            times+=1
            i=i+len_t
        else:
            i+=1

    print(target,'出现',times,'次')
    return times

target=input('input the target')
sorce=input ('input the sorce')
findstr(target=target,sorce=sorce)
