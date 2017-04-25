def funx():
    x=5
    def funY():
        nonlocal x
        x+=1
        return x
    return funY

a=funx()
print(a())
print(a())
print(a())