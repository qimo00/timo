def changewords(file_name,old_words,new_words):
    f_read=open(file_name)
    content=[]
    count=0

    for eachline in f_read:
        if old_words in eachline:
            count=eachline.count(old_words)
            eachline=eachline.replace(old_words,new_words)
        content.append(eachline)

    decide=input('\n文件%s中有%s个【%s】\n确定将【%s】替换为【%s】？\n(Yes/no)' \
                 % (file_name,count,old_words,old_words,new_words))

    if decide in ['yes','Yes','YES']:
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()
        print('替换完成~')

    f_read.close()

file_name=input('input the file name:')
old_word=input("input the old word:")
new_word=input('input the new word:')
changewords(old_words=old_word,new_words=new_word,file_name=file_name)
