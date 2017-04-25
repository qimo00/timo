def findstr(target,sorce):
    len_s=len(sorce)
    times=0
    for i in range(len_s-1):
        if sorce[i]==target[0]:
            if sorce[i+1]==target[1]:
                times+=1
    print(target,'出现',times,'次')
    return times

target=input('input the target')
sorce=input ('input the sorce')
findstr(target=target,sorce=sorce)
