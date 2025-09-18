secret_word="girraffe"
choices=3
guess = input(f"Enter guess: ") #3
while True:
    if choices>1:
        if guess==secret_word:
            print("you win!")
            break
        else:
            choices-=1
            guess = input(f"You have left with {choices} choices,  Enter guess: ") #2
            continue
    break