#比较两个文件的内容，并返回不同的位置以及相应内容
def compareFile(file1,file2):
    f1=open(file1,'r')
    f2=open(file2,'r')
    line=1
    error=0
    end1=f1.seek(0,2) #定位两个文件的结束位置
    end2=f2.seek(0,2)
    f1.seek(0,0)    #将两个指针指向首位
    f2.seek(0,0)
    while True:
        f1_line=f1.readline()
        f2_line=f2.readline()
        if f1.tell()==end1 and f2.tell()==end2 and f1_line=='' and f2_line=='':
            #判断两个文件是否结束，指向末尾指针并且均为空。若结束则跳出比较循环
            break
        elif f1_line==f2_line:
            line+=1
        elif f1_line!=f2_line:#当两行不同时比较字符串
            str1=f1_line
            str2=f2_line
            len_1=len(str1)
            len_2=len(str2)
            if len_1>=len_2:    #判断字符串较短的长度，防止调用溢出
                len_s=len_2
                long=1
            else:
                len_s=len_1
                long=2
            for i in range(len_s):  #循环判断两字符串的每个字符
                if str1[i]!=str2[i]:
                    print('%d行第%d个位置字符不同,分别为:%s--%s'%(line,i+1,str1[i],str2[i]))
                    error+=1
            if long==1: #补写两行多余不同的部分
                print('第一个文件第%d行多%s'%(line,str1[len_s:]))
                error+=1
            elif long==2:
                print('第二个文件第%d行多%s'%(line,str2[len_s:]))
                error+=1
            line+=1     #结束相应两行比较，进行下一循环
    if error==0:
        print("完全相同")
    else:
        print('总共有%d个不同'%error)
    print("---比较结束---")
    f1.close()
    f2.close()
filename1=input("请输入第一个文件名：")
filename2=input("请输入第二个文件名：")
compareFile(filename1,filename2)