# args is a tuple.
def testA(*args):
    result = 0
    for i in args:
        result = result + i
    return result


print(testA(1, 2, 3, 4, 5))


# kwargs is a diationary.
def testB(**kwargs):
    print(kwargs)


print(testB(k=1))

print(testB(a=1, b="strings"))

# to change a
a = 1
print(a)


def changeA(arg):
    arg = arg + 1
    return arg


a = changeA(a)
print(a)
# end of changing a

# to change b
b = 1
print(b)


def changeB():
    global b
    b = b + 1


changeB()
print(b)
# end of changing b


# lambda
# PEP 8: E731 do not assign a lambda expression, use a def
# why?
# >> lambda is a anonymous func. if there is a name for anonymous func, it is same as def.
# then, how to use this func correctly?
tLambda = lambda c, d: c - d
print(tLambda(3, 4))
