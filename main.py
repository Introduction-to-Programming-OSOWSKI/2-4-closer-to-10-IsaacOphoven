#WRITE YOUR CODE IN THIS FILE
#ok

def close10(x,y):
    if abs(x) < abs(y):
        if x < 10:
            x + 10
        if y < 10:
            y + 10
        if x < y:
            return x
    else:
        return y

print(close10(11,8))

