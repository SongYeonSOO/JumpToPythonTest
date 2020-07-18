s1 = "hello"
s2 = 'hello'
s3 = """hello"""
s4 = '''hello'''
print(s1, s2, s3, s4)

s5 = "he'l'lo"
print(s5)

s6 = 'he"llo'
print(s6)

s7 = 'he\'llo'
s8 = "he\"llo"
s9 = 'he\"llo'
print(s7, s8, s9)

s10 = "he\nllo"
s11 = """
he
llo"""
s12 = '''
he
llo
'''
print(s10, s11, s12)

# there is no blank between s5, s6.
print(s5 + s6)
# there is a blank between s5, s6.
print(s5, s6)

print("Hello" * 10)

print(len("hello"))
s13 = "hello"
print(s13[1])
print(s13[-1])

# out of index.
# print(s13[5])

# 1 <= string < 3
print(s13[1:3])
print(s13[:3])
print(s13[2:])
print(s13[:])
print(s13[1:5])

# why there is no out of index ? ello
print("1:8", s13[1:8])

# why there is no out of index ? o
print("-1:8", s13[-1:8])

# why there is no out of index ? hello
print("-10:8", s13[-10:8])

# why there is no out of index ? "" (Empty)
print("-10:0", s13[-10:0])

# why there is no out of index ? "" (Empty)
print("-1:1", s13[-1:1])


# why there is no out of index ? ell
print("-1:1", s13[1:-1])

# string is immutable.
# s13[3] = 'k' will throw TypeError exception. ('str' object does not support item assignment)

# string format
print("add int %d" % 3)
print("add string %s" % "like this.")
print("add char %c" % 'A')
# %d, %o, %x, %%
print("%% is used with %d,", "like this: %d%%" % 98)

# %s changes every types to string.
print("add string %s" % "like this.")
print("add string %s" % 1000)

# alignment
print("%10s" % "hello")
print("%-10s" % "hello")
# 3.1416
print("%0.4f" % 3.141592)
print("%10.4f" % 3.141592)
print("{0:0.4f}".format(3.141592))
print("{0:10.4f}".format(3.141592))

print("he {0} l {1} lo".format(0, 19.5))
print("he {num} l {name} lo".format(num="num?", name="true"))

print("{0:<10}".format("hello"))
print("{0:>10}".format("hello"))
print("{0:^10}".format("hello"))
print("{0:10}".format("hello"), "is same as first one..")
print("{0:k^10}".format("hello"))

print("{{, }}".format())
print("{, }")
print("{{, }}")

# f-format. (later version than python 3.6)
name = 0
name2 = 1
print(f'hel {name} lo {name2}')
print(f'{"hello":<10}')
print(f'{"hello":>10}')
print(f'{3.141592:10.4f}')
print(f'{{, }}')

#remove blanks.
print("     hello    ".lstrip())
print("     hello    ".rstrip())
print("     hello    ".strip())

