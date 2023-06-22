A= int(input("Give 'A' a number"))
Hundred_digits= A // 100
Tens_digits= (A // 10) % 10
Ones_digits= A % 10
Changed= ((Hundred_digits * 100) + (Ones_digits * 10) + Tens_digits)
print(Changed)

