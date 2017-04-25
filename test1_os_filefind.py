import  os
def search_file(start_dir,target):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if each_file==target:
            print(os.getcwd()+os.sep+each_file)
            global find
            find=1
        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.pardir)
    if find==0:
        print('no that file~')
find=0
start_dir=input("input the start path:")
target=input("input the target file name:")
search_file(start_dir=start_dir,target=target)