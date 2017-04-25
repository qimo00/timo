def base(*param,base=3):
    if param[-1]==5:
        base=5

    result=0
    for each in param:
        result+=each
    if base==3:
        result=result*base

    return result


print(base(1,2,5,4,1,3))