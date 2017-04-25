def dircount(pathin):
    import os

    txt_n=0
    png_n=0
    py_n=0
    docx_n=0
    wjj_n=0
    other_n=0
    list_path=os.listdir(pathin)
    for each in list_path:
        if '.' in each:
            (name,suf)=each.split('.')
            if suf=='txt':
                txt_n+=1
            elif suf=='png':
                png_n+=1
            elif suf=='py':
                py_n+=1
            elif suf=='docx':
                docx_n+=1
            elif suf=='':
                wjj_n+=1
            else:
                other_n+=1
        else:
            wjj_n += 1
    print('[.txt]文件有%d个'%txt_n)
    print('[.png]文件有%d个' % png_n)
    print('[.py]文件有%d个' % py_n)
    print('[.docx]文件有%d个' % docx_n)
    print('[文件夹]文件有%d个' % wjj_n)
    print('[其他]文件有%d个' % other_n)

path_in=input('input the path to count:')
dircount(path_in)