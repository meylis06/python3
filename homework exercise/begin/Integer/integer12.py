A= int(input("Give 'A' a number"))
Hundred_digits= A // 100
Tens_digits= (A // 10) % 10
Ones_digits= A % 10
Changed= ((Ones_digits * 100) + (Tens_digits * 10) + Hundred_digits)
print(Changed)