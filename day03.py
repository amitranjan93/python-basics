import random

guess = 0

while True:
    attempt = 0
    secret_number = random.randint(1, 100)
    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempt+=1
        if guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too Low!")
        else:
            break
    if attempt==1:
        print(f"{guess} is correct!🏆 Genius!")
    elif  2 <= attempt <= 5:
        print(f"{guess} is correct! 👏 Great job!")
    else:
        print(f"{guess} is correct! 🙂 You got there eventually!")
    ask = input("Do you want to play again? (y/n):")
    if ask == 'n':
        break
    else:
        guess = 0
        continue    