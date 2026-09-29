import random
words=["red","yellow","blue","green","pink"]

word=random.choice(words)

guessed_letters=[]

incorrect_guesses=0
max_guesses=6

print("welcome to Hangmane !")

print("Guess the word one letter at a time")

while incorrect_guesses < max_guesses:
    display =""
    for l in word:
        if l in guessed_letters:
            display += l+" "
        else:
            display +="_"
    print("\n word:",display) 

    if "_" not in display:
        print("Congratulation ! You guessed the word ")
        break

    guess=input("Enter a letter:").lower()

    if guess in guessed_letters:
        print(" You already guess the letter")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess !")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses :" ,incorrect_guesses,"/",max_guesses)  

else:
    print("\n Game Over")
    print("The word was:",word)
        



