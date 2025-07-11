'''We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.'''

from random import randint
n = randint(1, 100)  
a = -1
guesses = 1
while (a != n):
    a = int(input("Guess the Number: "))
    if (a < n):
        print("Higher number please")
        guesses += 1 
    elif (a > n):
        print("Lower number please")
        guesses += 1 # here putting guesses += 1 outside will increments guesses even when the guess is correct, i.e., when a == n. So you'd get 1 extra count at the end.
    
print(f"Congratulations! You guessed the correct number {n} in {guesses} attempts.")
    
    
