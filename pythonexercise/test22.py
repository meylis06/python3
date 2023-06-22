print("""Welcome to my first game dude, I hope there will be no errors in game. And don't worry
      I will explain rules, after you choose the room.""")
print("Now you have to choose room. And there are rooms,\n ROOM 1 \n ROOM 2\n ROOM 3")
Beginning= input("-->   ")
if Beginning == "ROOM 1" or "Room 1" or "room 1":
    print("""Well, you've chosen ROOM 1. OK, now you will write a number below and
    computer will select a random number. If your number and randomly selected number
     are same you will win. But if your number won't be same with selected number, GAME OVER.""")
    print("First select difficulty: \n Easy(1-10) \n Medium(1-35) \n Hard(1-120) \n Impossible(1-100000)")
    Difficulty= input("-->  ").lower()
    if Difficulty == "Easy" :
        print("Really?? Ok no problem, you are new.")
        Your_num= int(input("Choose a number:   "))
        if Your_num > 10 :
            print("Bruuhhh, nice work joker. GAME OVER")
            exit(0)
        import random
        X= (random.randrange (1,10))

        print("Selected number:", X)
        if X == Your_num :
            print("Nice, you' ve won.(In Easy Difficulty x) ))")
        else:
            print("Hahaha you've lost in Easy Difficulty. No problem try again, just luck wasn't on your side.")
    elif Difficulty == "Medium" :
        print("Nice, you're a real gamer.")
        Your_num2= int(input("Choose a number:   "))
        if Your_num2 > 35 :
            print("Bruuhhh, nice work joker. GAME OVER")
            exit(0)
        import random
        X1= (random.randrange (1, 35))
        print("Selected number:",X1)
        if X1 == Your_num2 :
            print("Oho you've won in Medium Difficulty. Congrats!!!")
        else:
            print("Dundundun you've lost but no problem, nobody always wins. Try again.")
    elif Difficulty == "Hard" :
        print("Wow, somebody is brave today, Ha?")
        Your_num3= int(input("Choose a number:   "))
        if Your_num3 > 120 :
            print("Bruuhhh, nice work joker. GAME OVER")
            exit(0)
        import random
        X2= (random.randrange (1, 120))
        print("Selected number:",X2)
        if X2 == Your_num3 :
            print("What the- you just won in Hard Mode???? Dude you are the luckiest person in the world.")
        else:
            print("Ooowww you've lost. Don't be sad Hard Mode doesn't meant to be easy. Don't give up and TRY AGAIN!!!")
    elif Difficulty == "Impossible" :
        print("Dude are U OK?? Really you think you will win??? Haha ok let's see.")
        Your_num4= int(input("Choose a number:   "))
        if Your_num4 > 100000 :
            print("Bruuhhh, nice work joker. GAME OVER")
            exit(0)
        import random
        X3= (random.randrange (1, 100000))
        print("Selected number:",X3)
        if X3 == Your_num4 :
            print("""Wait a minute, WHAAATTTTT?!?!?! You are cheater, Right? Please quit from my game, there is no place
            for cheaters.""")
        else:
            print("What? You thought you'd win?? Man, wake up to reality.")
    else:
        print("""Dude you know it ain't funny, IT IS NOT EASY FOR ME TO WRITE THIS CODES so write normal things. OK??""")        
                   



        

