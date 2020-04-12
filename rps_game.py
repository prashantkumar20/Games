print("ROCK PAPER AND SCISSOR GAME")
print("Winning Rules of the Rock Paper Scissor Game are as follows => \n"
      +"\tRock vs Paper    -> Paper Wins \n"
      +"\tPaper vs Scissor -> Scissor Wins \n"
      +"\tScissor vs Rock  -> Rock Wins \n")
while True:
    print("Enter Choice\n 1. Rock\n 2. Paper\n 3. Scissor\n")
    while True:
        user_choice = input("User Turn =>")
        user_choice = user_choice.lower()
        if user_choice not in ['rock','paper','scissor']:
            print("Wrong input,Please enter valid input:")
        else:
            break
    print("User has chosen :" + user_choice + "\n")
    import random
    comp_choice = random.choice(['rock','paper','scissor'])
    print("comp_choice is :" +comp_choice +"\n")
    print("\t" + user_choice + "\n vs \n" + "\t" + comp_choice)
    result = None
    if((user_choice=="rock" and comp_choice=="paper")or(user_choice=="paper"and
                                                    comp_choice=="rock")):
        result="paper"
    elif((user_choice=="paper" and comp_choice=="scissor")or(user_choice=="scissor"
                                                and comp_choice=="paper")):
        result="scissor"
    else:
        result="rock"
    if(user_choice==comp_choice):
        print("<== Draw ==>")
        print("SCORECARD:> \n User:- 1 \n Computer:- 1")
    elif(result == user_choice):
        print("<== User Wins ==>")
        print("SCORECARD:> \n User:- 1 \n Computer:- 0")
    else:
        print("<== Computer Wins ==>")
        print("SCORECARD:> \n User:- 0 \n Computer:- 1")
    answer = input("Do you want to play again? (Y/N)=>")
    if(answer=="n" or answer=="N"):
        break
print("\nThanks for playing ROCK PAPER SCISSOR GAME \n")
        
        
        