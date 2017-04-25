def newFile(file_name):
    f=open(file_name,'w')
    print('input your words,stop by \':w\' a new line:')
    while True:
        write_some=input()
        if write_some!=':w':
            f.write('%s  \n' % write_some)
        else:
            break
    f.close()

file_name=input ("please input the filename")
newFile(file_name)