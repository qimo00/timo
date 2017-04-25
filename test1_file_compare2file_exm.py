def com_file(file1,file2):
    f1=open(file1)
    f2=open(file2)
    line=0
    errorN=[]
    for line1 in f1:
        line2=f2.readline()
        line+=1
        if line1!=line2:
            errorN.append(line)
    f1.close()
    f2.close()
    return errorN

file1=input('input the 1st file name:')
file2=input('input the 2nd file name:')
err=com_file(file1,file2)
if len(err)!=0:
    for each in err:
        print('%d行有错误'%each)
else:
    print('完全相同')