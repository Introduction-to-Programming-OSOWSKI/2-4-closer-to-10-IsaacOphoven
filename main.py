#WRITE YOUR CODE IN THIS FILE
#ok

def close10(x,y):
    if x - 10 < y - 10:
        return x
    elif x - 10 > y - 10:
        return y
    else:
        return 0
        
print(close10(12,9))
