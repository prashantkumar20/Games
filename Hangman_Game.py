print("HANGMAN lETTER GAME")
import random
words=['orange','lime','lemon','melon','grape','mango','apple']
while True:
    start=input("Press enter/return to start, or enter Q to quit")
    if start.lower()=='q':
        break
    secret_word=random.choice(words)
    bad_guesses=[]
    good_guesses=[]
    while len(bad_guesses)<7 and len(good_guesses)!= len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter,end=' ')
            else:
                print('_',end=' ')
        print('\nstrike:{}/7'.format(len(bad_guesses)))
        print('')  
        guess=input("Guess a letter:").lower()
        if len(guess)!=1:
            print("You can only guess a single letter")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        if guess in secret_word:
            good_guesses.append(guess)
        if len(good_guesses)==len((secret_word)):
            print("You win : The word was {}".format(secret_word))
            break
        else:
            bad_guesses.append(guess)
print("You didn't guess it : My secret word was {}".format(secret_word))
            
              
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    