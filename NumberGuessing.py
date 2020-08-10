import random
ans = random.randint(0, 100)
guess = int()
count = 1

while guess != ans:
    guess = int(input("Guess the integer: "))
    
    if guess == ans:
        print("Your answer is correct!")
        print("You made " + str(count) + " guesses.")
        break
    elif guess > ans:
        print("Your answer is too large. Try again.")
        count += 1
    else:
        print("Your answer is too small. Try again.")
        count += 1
