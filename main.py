import random
# www.practicepython.org

# exercise 4
def divisors(x):
    div = []
    for i in range(1, x + 1):
        if x % i == 0:
            div.append(i)
    return div

# exercise 4 with list comprehension:
def divisors2(x):
    return [i for i in range(1, x + 1) if x % i == 0]

# exercise 7
def listComp():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even = [i for i in a if i % 2 == 0]
    return even


# exercise 9
def randomNumberGame():
    guessNumber = 0
    c = 0
    r = random.randint(1, 9)

    while guessNumber != r and guessNumber != 'exit':
        guessNumber = input('Guess a number between 1 and 9:')

        if guessNumber == 'exit':
            break

        guessNumber = int(guessNumber)
        c += 1

        if guessNumber == r:
            print('You are right')
            print('you took only', c, 'tries!')
        elif guessNumber > r:
            print('You guessed too high')
        elif guessNumber < r:
            print('You guessed too low')
        elif guessNumber == '':
            print('you have to enter a number')


# randomNumberGame()

# exercise 10
def listOverlapComp():
    a = [random.randrange(1, 50, 1) for i in range(7)]
    b = [random.randrange(1, 50, 1) for i in range(10)]

    return [i for i in set(a) if i in b]
    # structure of list comprehension: [EXPRESSION FOR_LOOPS CONDITIONALS]


# print(listOverlapComp())

# exercise 11
def prime(x):
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            print(x, 'is not a prime number')
            break
    else:
        print(x, 'is a prime number')


# prime(15)

# exercise 13
def Fibonacci():
    x = int(input('Enter amount of numbers in sequence: '))

    a = 0
    b = 1

    fib = [1]

    for i in range(x - 1):
        c = a + b
        fib.append(c)
        a = b
        b = c

    print(fib)


# Fibonacci()

def backwards(x):
    return x.split()[::-1]


