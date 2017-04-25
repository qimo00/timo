# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（
#       仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符
#       （仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位



symbols='~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
strs='abcdefghijklmnopqrstuvwxyz'
num='0123456789'
flag_len=0
passward=str(input("input your passward:"))
len_pw=len(passward)
if len_pw<=8:
    flag_len=1
elif 8<len_pw<16:
    flag_len=2
elif len_pw>=16:
    flag_len=3

symbol_num=0
str_num=0
num_num=0
for each in passward:
    if symbols.find(each):
        symbol_num=1
    elif strs.find(each):
        str_num=1
    elif num.find(each):
        num_num=1
    else:
        print("input is error!!!!!!!!!")
        break

if flag_len==1 or symbol_num ==0:
    print("安全级别低~~~~~~!!!!!!!!!!")
elif flag_len==2 or symbol_num+str_num+num_num==2:
    print("安全级别中！！！！！！！！")
elif flag_len ==3 or symbol_num+str_num+num_num==3:
    if passward[0].isalpha():
        print("安全级别高！！！！！")
    else:
        print("不是以字母开头。。。")



























