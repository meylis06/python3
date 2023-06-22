A=int(input("Give a value:"))
a1=int(A/100)
a0=A-a1*100
b1=int(a0/10)
b0=a0-b1*10
d=(a1==(b0*10 + b1))
print(d)