def count(*str_in):
    len_num=len(str_in)
    for i in range(len_num):
        letter=0
        number=0
        space=0
        others=0
        for each in str_in[i]:
            if each.isdigit():
                number+=1
            elif each.isalpha():
                letter+=1
            elif each==' ':
                space+=1
            else:
                others+=1
        print('in',str_in[i],'there is ',\
              '%d letters,%d numbers,%d spaces,%d others' \
              % (letter,number,space,others))

count('asdfasdf36513.21','asdfds51')