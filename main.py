#WRITE YOUR CODE IN THIS FILE
#ok

def close10(x,y):
    if abs(x - 10) < abs(y - 10):
        return x
    if abs(x - 10) > abs(y - 10):
        return y


    else:
        return y

print(close10(7,15))

