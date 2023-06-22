A= int(input("Give 'A' a number"))
Tens_digit= A // 10
Ones_digit= A % 10
The_number= ((Ones_digit * 10) + Tens_digit)
print("The new number is: ", The_number)