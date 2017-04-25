
while True:
    number = input('input a number:(输入z时退出程序)')
    if number!='z':
        number=int(number)
        print("%d to %#x" % (number,number))
        print('%d to %#o' % (number,number))
        print('%d to ' % number , bin(number))
    else :
        break

