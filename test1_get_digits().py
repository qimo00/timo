def get_Digits(n):
    result=[]
    if n>9:
        result=get_Digits(n//10)
        result.append(n%10)
        return result
    else:
        result.append(n)
        return result

print(get_Digits(12300))
