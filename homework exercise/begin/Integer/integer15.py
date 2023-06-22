A= int(input("Give \"A\" a number:"))
hundred_digits= A // 100
tens_digits= (A // 10) % 10
ones_digits= A % 10
New_number= ((hundred_digits * 100) +(ones_digits * 10) + tens_digits)
print("Changed number:", New_number)