passward='xiaojizhi'
count=3
while count>0:
    passwardin=input("input the passward:")

    if passwardin==passward:
        print("great!!~~~~~~~~~~~")
        break
    elif '*' in passwardin:
        print("there is '*' ,input again \n %d times left"%count)
        continue
    else:
        print("input is wrong,%d times left"%(count-1))
    count -= 1







    # temp=0
    # lengthpass=len(passwardin)
    # if '*' in passwardin:
    #     print("there is '*' ,input again ,%d times left" % count)
    # for i in range(lengthpass):
    #     if passwardin[i]==passward[i]:
    #         i+=1
    #         temp+=1
    #     else:
    #         print("passward is wrong")
    #         break
    # if temp==lengthpass:
    #     print("great!!!!!!!!!")
    #     break
    # else:
    #     print("you have another %d times" % count)

