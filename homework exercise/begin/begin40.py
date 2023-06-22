A1= int(input("Give 'A1' a number:"))
A2= int(input("Give 'A2' a number:"))
B1= int(input("Give 'B1' a number:"))
B2= int(input("Give 'B2' a number:"))
C1= int(input("Give 'C1' a number:"))
C2= int(input("Give 'C2' a number:"))
#A1*x + B1*y = C1
#A2*x + B2*y = C2
D = A1*B2 - A2*B1
x = (C1*B2 - C2*B1)/D
y = (A1*C2 - A2*C1)/D
print("x is", x)
print("y is", y)
