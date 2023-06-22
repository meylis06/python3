V= int(input("Give a velocity:"))
U= int(input("Give a river flow velocity"))
T1= int(input("Give a time in lake:"))
T2= int(input("Give a time in river:"))
S1= V * T1
S2= (V - U) * T2
S3= S1- S2
print("Distance in lake:", S1)
print("Distance in river:",S2)
print("Then total distance covered by boat is:", S3)