def file_print(n,file1):
    f=open(file1)
    line_num=int(n)
    while line_num:
        print(f.readline(),end='')
        line_num-=1
    f.close()

filename=input("input the file name:")
line_num=input('input the number of lines:')
file_print(n=line_num,file1=filename)
