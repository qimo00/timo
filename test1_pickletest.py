import pickle

def split_file(file_name):
    f = open(file_name,'r')
    boy = 1
    girl = 1


    for each_line in f:
        if each_line[:6] != '======':
            word = each_line.split(':')
            if word[0] == '小甲鱼':
                file_b = open('boy_'+str(boy)+'.pkl','ab')
                pickle.dump(str(word[1]),file_b)
                file_b.close()
            elif word[0] == '小客服':
                file_g = open('girl_'+str(girl)+'.pkl','ab')
                pickle.dump(str(word[1]),file_g)
                file_g.close()
        else:
            boy += 1
            girl +=1

    f.close()

file_name = input('input the file name:')
split_file(file_name)




