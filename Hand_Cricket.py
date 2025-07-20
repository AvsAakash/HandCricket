import random
poss=[1,2,3,4,5,6]
# poss=[1,2,3,4,5,6,7,8,9,10,15,20]
print("Possible Runs are: ",poss)
# def toss():
to=input("You are player one. Odd or Even: ")
while to != "Stop":
    p1=int(input("Enter a number: "))
    p2= random.choice(poss)
    print("Opponent Choice is : ",p2)
    if (((p1+p2)%2==0) and (to == "Even")):
        print("You WON!! BAT or BALL...")
        choice1 = input("Enter Bat or Ball: ")
        choice2="None"
        print("Your choice is : ",choice1)
    elif (((p1+p2)%2!=0) and (to == "Odd")):
        print("You WON!! BAT or BALL...")
        choice1 = input("Enter Bat or Ball: ")
        choice2="None"
        print("Your choice is : ",choice1)
    else:
        options=["Ball","Bat"]
        choice2 = random.choice(options)
        choice1="None"
        print("Opponent won the Toss")
        # print("Opponent chooice is: ",choice2)
        print("And choose to ",choice2)
    # toss()
    sum1=0
    sum2=0
    while(1):
        if ((choice1== "Bat") or (choice2 == 'Ball')):
            p1= int(input('Enter Number: '))
            if p1 not in poss:
                print("Invalid")
                print("Player-1: ",sum1)
                continue
            p2= random.choice(poss)
            if p1==p2:
                print("You are OUT ;(")
                print("Player-1 Total : ",sum1)
                break
            sum1 +=p1
            print("Player-1 Total: ",sum1)
        # elif choice1== "Ball" or choice2 == 'Bat':
        else:
            p1= int(input('Enter Number: '))
            if p1 not in poss:
                print("Invalid")
                print("Player-2 Total: ",sum2)
                continue
            p2= random.choice(poss)
            if p1==p2:
                print("You are OUT ;(")
                print("Player-2 Total: ",sum2)
                break
            sum2 +=p2
            print("Player-2 Total: ",sum2)
            # sum2 +=p2
    print()
    print("The scores are: ",sum1,", ",sum2)
    print("Its opponent's time")
    print()
    if ((sum1==0) and ((choice2 == "Bat") or (choice1=="Ball"))): # choice1 == "ball" endhuku rasa ante, ippudu player one toss gelichadu anuko player two ki choice radu kada and appudu sum1=0 avutundi kani "if condition fail becasue choice2 emi undadu kabbati",so adi sum2 ke add chestundi 
        while 1:
            p1= int(input('Enter Number: '))
            if p1 not in poss:
                print("Invalid")
                print("Player-1: ",sum1)
                continue
            p2= random.choice(poss)
            sum1 +=p1
            if sum1>sum2:
                print('Player-1 won: ',sum1,', ',sum2)
                break
            elif p1==p2:
                print("You are OUT ;(")
                sum1 -=p1
                print("Player-1 Total : ",sum1)
                print("Player-2 WON!!")
                break
            print("Player-1 Total: ",sum1)
    else:
        while 1:
            p1= int(input('Enter Number: '))
            if p1 not in poss:
                print("Invalid")
                print("Player-2 Total: ",sum2)
                continue
            p2= random.choice(poss)
            sum2 +=p2
            if sum2 >sum1:
                print('Player-2 won: ',sum1,', ',sum2)
                break
            elif p1==p2:
                print("You are Out;(")
                sum2 -=p2
                print("Player-2 Total: ",sum2)
                print("Player-1 WON!!")
                break
            
            print("Player-2 Total: ",sum2)       
    print("Scores are: ",sum1,', ',sum2)
    print()
    print()
    print("NEW GAME!!")
    print("If You wish to stop the game, Type 'Stop' in the following input")
    to=input("You are player one. Odd or Even: ")
    # if sum1> sum2:
    #     print('player one won')
    # else:
    #     print('player one won')
print("User chose not to play")






#Including your Hand Cricket game in your resume can be a great idea, especially if you're applying for roles that value programming skills. Here are some tips on how to present it:

    # Project Title: Name it something like "Hand Cricket Game in Python".

    # Description: Briefly explain what the game is and its purpose. You could mention that it simulates a cricket game with user interaction through the console.

    # Technologies Used: List Python as the primary language.

    # Key Features:
    #     Randomized opponent choices.
    #     Odd/even toss mechanic.
    #     Player input for scoring.
    #     Loop for multiple games.

    # Link to Code: If you have it hosted on a platform like GitHub, include the link.

    # Skills Demonstrated: Highlight skills such as:
    #     Control flow (loops, conditionals).
    #     Random number generation.
    #     Input validation.

# This showcases your coding abilities and creativity. Would you like help crafting a specific section for your resume?