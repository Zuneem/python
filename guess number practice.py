import random

print ('whats your name')
name = input()

print (' hello ' + name + ' guess a number between 1 and 10.')

number = random.randint (1, 10)

for guess in range (1, 5):
    print ('take a guess')
    guess= int(input())
    if guess < number:
        print ('your guess is too low')
    elif guess > number:
        print ('your guess is too high')
    else:
        break

if guess == number:
    print (' you got it')
else:
    print ( 'none of your guesses are correct. The right number was ' + str(number))
