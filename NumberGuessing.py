import random
tar = random.randint(0,100)
ans = 101

while ans != tar:
    ans = input('Guess the integer: ')
    ans = int(ans)
    if ans == tar:
        print('Your answer is correct!')
        break
    elif ans > tar:
        print('Your answer is too large.')
    else:
        print('Your answer is too small.')
