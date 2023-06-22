A= int(input("Give 'A' a number"))
Hundred_digits= A // 100
Tens_digits= (A // 10) % 10
Ones_digits= A % 10
Sum=(Hundred_digits + Tens_digits + Ones_digits)
product=(Hundred_digits * Tens_digits * Ones_digits)
print(f"The sum is {Sum} and product is {product}")