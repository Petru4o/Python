# 1 program-privet
def privet(x):
    if x == 0:
        return
    else:
        print('Hello')
        privet(x - 1)


privet(10)


# 2 sum
def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x - 1)


z = sum(5)
print(z)


# 3 Factorial

def fact(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))


# 4 Fibonacci

def Fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return Fibo(x - 1) + Fibo(x - 2)


print(Fibo(7))
