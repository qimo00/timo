def Palindrome(str_in):
    len_s=len(str_in)
    i=0
    flag=1
    while i<len_s/2:
        if str_in[i]==str_in[len_s-1-i]:
            i+=1
        else:
            flag=0
            break
    if flag==1:
        print("it is a Palindrome")
    else:
        print("it is not a Palindrome")

string=input("input a string:")
Palindrome(string)