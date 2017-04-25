def Palindrome(str_in):
    list1=list(str_in)
    list2=list(reversed(list1))
    if list1==list2:
        flag=1
    else:
        flag=0
    return flag

string=input('input a string')
flag=Palindrome(string)
if flag==1:
    print("it is a Palindrome")
else:
    print("it is not a Palindrome")