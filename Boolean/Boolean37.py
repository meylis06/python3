x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))
c=(abs(x1-x2)==1 and abs(y1-y2)==1)\
    or (x1==x2 and abs(y1-y2)==1)\
    or (y1==y2 and abs(x1-x2)==1)
print(c)