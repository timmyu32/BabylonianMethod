raticand = input("What number do you want to find the square root of? ")

try:
    raticand = int(raticand)
except:
    raticand = float(raticand)

guess1 = input("What do you think the square root is?(Guess)    ")

try:
    guess1 = int(guess1)
except:
    guess1 = float(guess1)

resultOfGuess = 0
counter = 0

while guess1 != resultOfGuess:

    resultOfGuess = raticand / guess1
    print("{} divided by {} = {}".format(raticand, guess1, resultOfGuess))
    #result of the guess is just the product of the raticand divided by the guess

    average  = (resultOfGuess + guess1)/2
    print("Average of guess and (raticand/guess) = {}".format(average))

    guess1 = average
    print("\n")
    counter += 1
    if counter > 100:
        print("The answer is irrational")
        break

print("{} = the square root of {}".format(guess1, raticand))
print("it took {} iterations of the loop to get the right answer".format(counter))
