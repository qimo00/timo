import os
def search_file(start_dir,target):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd()+os.sep+os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.pardir)

    start_dir=input('input the start path:')
    program_dir=os.getcwd()

    target=['.mp4','.avi','.rmvb']
    vedio_list=[]

    search_file(start_dir,target)

    f=open(program_dir+os.sep+'vediolist.txt','w')
    f.writelines(vedio_list)
    f.close()