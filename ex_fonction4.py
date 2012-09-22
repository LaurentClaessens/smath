import math

def ma_fonction(a):
    if a >= 0 :
        return 1
    return -1

def evaluation(f,x):
    return f(x)


print(evaluation(ma_fonction,10))
print(evaluation(math.cos,0))
print(evaluation(lambda x:x**2,2))
