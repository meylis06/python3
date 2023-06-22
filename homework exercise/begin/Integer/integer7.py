A= int(input("Give 'A' a number"))
Tens_digit= A // 10
Ones_digit= A % 10
B= Tens_digit + Ones_digit
C= Tens_digit * Ones_digit
print("Sum of digits is:", B)
print("Product of digits is:", C)