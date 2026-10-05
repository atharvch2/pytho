import random
a=random.randint(1,100)
tries=0
while True:
    tries= tries+1
    b=int(input("input your guess:-"))
    if b==a:
        print(f"Congratulations! you won the game in {tries} tries.")
        break
    elif b<a:
        print("Sorry you are wrong, go higher!")
    elif b>a:
        print("Sorry you are wrong, go lower!")
