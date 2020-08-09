primes = []

num = 2
div = 2
max = int(input("Maximum possible integer: "))

while num < max:
    if num > div:
        if num % div == 0: # if num is divisible by div
            num += 1
            div = 2
        else:
            div += 1
    else:
        primes.append(num)
        num += 1
        div = 2
        
print(primes)
