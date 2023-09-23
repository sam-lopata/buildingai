# Write a program that prints "I love" followed by one word: the additional word should be 'dogs' 
# with 80% probability, 'cats' with 10% probability, and 'bats' with 10% probability.
# Here's an example output:
# I love bats

import random

def main():
    prob_dogs = 0.80
    prob_cats = 0.10
    prob_bats = 0.10

    probability = random.random()
    
    if probability < prob_dogs:
        favourite = "dogs"
    elif probability < prob_dogs + prob_cats:
        favourite = "cats"
    else:
        favourite = "bats"
    
    print("I love " + favourite) 

main()
