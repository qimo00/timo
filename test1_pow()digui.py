def power(x,y):
    result=1
    if y==0:
        return 1
    else:
        result=x*power(x,y-1)
    return result

print(power(3,3))