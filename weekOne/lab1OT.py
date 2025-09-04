# Lab 1 Ousman Touray

# using python as a calculator

4+9
print("An example of addition -->",4+9)
0-8
print("An example of subtraction",0-8)
print(4-6)
print("An example of multiplication",6*7)
x = 9
y = 20
print("An example with variables",x*y)
print("An example of integer division",9//12)
print("An example of division",8/2)
print("An example of modulo in use",15%4)
print("An example of square root functionality",2**10)
# Using variable names
c = x * y
print(c)
# converting data types while processing
print(int(10/3))
print(int(8/2))
print(10/3, ",", int(10/3))
print(3*7, ',', float(3*7))
#second argument after the comma controls to what point the program recognizes
print(round(10/3, 2))
#big numbers
a = 1_000_000
print(3*a)
#complex numbers
c = 3 + 4
d = 3 + 4j
print(type(c), type(d))
print(c,d)
print("real part", d.real)
print("imag part", d.imag)
print("conjugate", d.conjugate())