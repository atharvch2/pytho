tries=0
while True:
    tries+=1
    import random
    comp=random.randint(1,3)

    if comp==1:
     comp_move="rock"
    elif comp==2:
     comp_move="paper"
    elif comp==3:
     comp_move="scissor"





    a=(input("Your move:-"))
    if comp_move=="rock" and a=="rock":
        print("tie")
    elif comp_move=="paper" and a=="rock":
        print("lost! try again")
    elif comp_move=="scissor" and a=="rock":
        print(f"You won in {tries} tries." )
        break
    elif comp_move=="rock" and a=="paper":
        print(f"You won in {tries} tries.")
        break
    elif comp_move=="paper" and a=="paper":
        print("tie")
    elif comp_move=="scissor" and a=="paper":
        print("lost! try again")
    elif comp_move=="rock" and a=="scissor":
            print("lost! try again")
    elif comp_move=="paper" and a=="scissor":
            print(f"You won in {tries} tries.")
            break
    elif comp_move=="scissor" and a=="scissor":
            print("tie")
