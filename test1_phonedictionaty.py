print('|--- 欢迎进入通讯录 ---|')
print('|---1.查询联系人资料---|')
print('|---2.插入新的联系人---|')
print('|---3.删除已有联系人---|')
print('|---4.退出通讯录程序---|')
phonedic={}
while True:
    command=input('请输入相关的指令代码：')
    if command.isdigit():
        command=int(command)
    else:
        print('输入命令有误，请重新输入---')
        continue
    if command==1:
       name=input('请输入联系人姓名：')
       if phonedic.get(name)==None:
           print('查询的联系人不存在！')
           continue
       else:
           print(name,'-->',phonedic.get(name))
           continue

    elif command==2:
        name=input('请输入增加联系人姓名：')
        phone=int(input('请输入联系人电话：'))
        if name in phonedic:
            print('联系人已存在！')
            continue
        else:
            phonedic.update({name:phone})
            continue

    elif command==3:
        name=input('请输入删除联系人姓名:')
        if phonedic.get(name)==None:
            print('不存在此联系人！')
        else:
            print(name, end='')
            print('删除的联系人为：')
            phonedic.pop(name)
    elif command==4:
        print('|---感谢使用通讯录---|')
        break
    else:
        print('输入命令有误，请重新输入。')
        continue