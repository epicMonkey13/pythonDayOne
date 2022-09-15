# 1
a = "Hello World"
print(a)

# 2

x = ["red", "black"]
y = ["red", "black"]
z = x
print(x is z)

# 3
x = 5
print(not(x > 3 and x < 10))

# 4
n = 5

for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        print(' ', end='')

    C = 1
    for j in range(1, i + 1):
        print(' ', C, sep='', end='')

        C = C * (i - j) // j
    print()

    # 5
start, end = 1, 50

for num in range(start, end + 1):

    if num % 2 != 1:
        print(num, end=" ")

# 6
txt = "Python is fun"[::-1]
print(txt)

# 7
a = "Hello, World!"
print(len(a))

# 8
txt = "Hello my Python trainer Salma"

x = txt.upper()

print(x)

# 9
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

x = float(1)
y = int(2.8)
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# 10
# this is how we use comments in a program

# 11 Indentation errors example
# site = 'edu'
# if site == 'edu':
# print('Logging in to EduCBA!')
# else:
#      print('Please type the URL again.')
# print('You are ready to go!')
#     print('Logging in to EduCBA!')
#     ^
# IndentationError: expected an indented block after 'if' statement on line 79

#12 Python allows a certain level of flexibility with quotes around strings, however, they should be present at least in some form as canve seen from the examples below.
a = "Wiley Edge"
b = "Wiley Edge loremmmmmm sdfjsk."""
c = "Python"
d = '''loem odd even la list'''
print(a)
print(b)
print(c)
print(d)

#13 result is 7
text = 'Python is fun'
result = text.index('is')
print(result)

#14
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#15 capitalize method applies to the first char, and the upper method applies uppercase to all chars
txt = "hello, and welcome to my world."

x = txt.capitalize()
y = txt.upper()
print(x)
print(y)

#16
print('Enter your name:')
x = input()
print('Hello, ' + x)

#17
int_number = 25
float_number = float(int_number)
print(float_number)

float_number_two = 25.36
int_number_two = int(float_number_two)
print(int_number_two)

#18
value = 5
value **= 3
print(value)












