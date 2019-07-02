import random

# A list of words that 
potential_words = ["example", "words", "someone", "can", "guess"]

# Randomly pick a word out of the potential_words list.
word = random.choice(potential_words)
# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
# This line makes current_word the same length as word.
current_word = ["_"]*len(word) 

# Some useful variables
guesses = []
maxfails = 7
fails = 0

#Since we initialized fails to 0 and maxfails to 7,
#we will only allowed to fail 7 times before the while
#loop stops.
while fails < maxfails:

    #Ask the user to input a letter, which we will store in a variable we named guess.
    guess = input("Guess a letter: ")

    # This checks for the case where the user typed in a character that they've already guessed before.
    if guess in guesses:
        print("You already guessed that letter! Try again.")
        # We want the user to immediately type in another guess, so we use the continue operater
        # to make the code jump back up to the start of the while loop. (line 27)
        continue

    # This checks for the case where the letter is not in the word.
    elif guess not in word:
        # Only update the number of fails if we guess wrong.
        fails = fails+1
        print("Letter %s is not in the word!" % guess)

    # This checks for the case where the character is in the word.
    else:
        letter_index = 0
        # We use a while loop to check for duplicates of the character in the word.
        while letter_index < len(word):
            # We check to see if guess is in the rest of the word. Notice that
            # we are checking a *spliced* version of word in the if conditional.
            # For example, if word == "banana", and guess == "a", initially
            # letter_index == 0. Then after line 65, we find our first
            # occurrence of "a" at index 1, so letter_index is set to 1.
            # At line 75, we update letter_index by 1 to look at the rest of the string.
            # The next time we run this code, we will be looking at word[2:], which means
            # we are looking at "nana" now, instead of "banana". 
            print("This is the letter_index value: %s" % letter_index)
            if guess in word[letter_index:]:
                # Update the letter_index variable because the list.index() function
                # can be adjusted to start searching from different indices.
                # list.index(element, start_index) will return the smallest index where
                # element occurs, starting from start_index. Google for examples,
                # or play around with the function in the Python interpreter.
                letter_index = word.index(guess, letter_index)

                # Change the "_" in current_word to guess. For example, if
                # current_word looked like ["_", "_", "_"] before, and
                # guess == "a", and word == "cat", current_word would be updated to
                # ["_", "a", "_"].
                current_word[letter_index] = guess

                # In the next loop, we want to start searching the rest of the string
                # for the letter, so update letter_index by 1.
                letter_index += 1
            else:
                # There are no more duplicates, so we break out of the loop
                # that was initialized at line 49.
                break

        # We have already replaced all instances of "_" in current_word,
        # which means the user has guessed all the letters.
        if "_" not in current_word:
            print("You win!")
            print("The word was %s." % word)

            # Use the break operator to break out of the while loop (line 27)
            # and end the game.
            break

    # Add the user's guess to the guesses list.
    guesses.append(guess)

    # Print out the current_word and the number of tries the user has left
    # after every guess.
    print(current_word)
    print("You have " + str(maxfails - fails) + " tries left!")