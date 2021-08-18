# Exercise 16: create a random password generator
import random


def password_generator():
    length = int(input("How many digits do you want your password to be?: "))

    password = []

    for i in range(length):
        password.append(random.choice('abcdefghijklmnopqrstuvwxyz'
                                          'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                          '1234567890!@#$$%^&*()'))
    print(''.join(password))


password_generator()
