#WRITE YOUR CODE IN THIS FILE
#ok

def close10(x,y):
    if abs(x - 10) < abs(y - 10):
        return x
    elif abs(x - 10) > abs(y - 10):
        return y
    else:
        return both

print(close10(5 , 14))

