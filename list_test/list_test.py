list = [0, 1, 2, 3, 4, 5]
print(list)
print(list[0])
print(list[-1])

listInList = [0, 1, 2, 3, 4, ['a', 'b', 'c']]
print(listInList[-1])
print(listInList[-1][2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + a)
print(a + b)

print(len(a))
print(str(a[0]) + " add strings.")

a1 = [1, 2, 3]
a1[1] = 4
print(a1)

del a1[1]
print(a1)

a1.append(5)
print(a1)

a1.extend([6,7,8])
print(a1)