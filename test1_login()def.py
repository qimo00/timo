user_data={}

def logIn():
    while True:
        print('|---新建用户：N/n---|')
        print('|---登录账号：E/e---|')
        print('|---退出账号：Q/q---|')
        print('请输入命令代码：')
        command=input()
        if command=='N' or command=='n':
            newC()
            # continue
        elif command=='E' or command=='e':
            enterC()
            # continue
        elif command=='Q' or command =='q':
            break
        else:
            print('输入命令有误，请重新输入：\n')
    print('退出成功~')

def newC():

    while True:
        name = input('请输入用户名：')
        if name in user_data:
            print('该用户名已存在，请重新输入')
            continue
        else:
            code=input('请输入密码：')
            user_data[name]=code
            print('创建用户成功！')
            break
    return


def enterC():
    name=input('请输入用户名:')
    if name in user_data:
        code=input('请输入密码：')
        if code==user_data[name]:
            print("登录成功！")
        else:
            print('密码错误~')
    else:
        print('该用户不存在！')
    return


logIn()
