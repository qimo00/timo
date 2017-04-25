a=[1,3,2.2,51.3,',','g',True]
sum=0
length=len(a)
for each in a:
    if type(each)==int or type(each)==float:
        sum+=each
    else:
        continue
print(sum)