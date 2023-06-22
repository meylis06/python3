V1= int(input("Give first car's velocity:"))
V2= int(input("Give second car's velocity:"))
S= int(input("Give a distance:"))
T= int(input("Give a time:"))
S2= T * (V1 + V2)
S3= S - S2
print(f"Distance between cars after {T} hours is: {S3}")