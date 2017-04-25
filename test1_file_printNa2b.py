def file_p(file1,lines_num):
    f=open(file1)
    if lines_num.strip()==':':
        begin=1
        end=-1
    else:
        (begin,end)=lines_num.split(':')
    if begin=='':
        begin=1
    if end=='':
        end=-1

    begin=int(begin)-1
    end=int(end)
    lines=end-begin

    for i in range(begin):
        f.readline()
    if lines<0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline(),end='')

    f.close()

file1=input("input the file name:")
lines=input ('input the lines:')
file_p(file1=file1,lines_num=lines)
