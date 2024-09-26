print("Yo! As you see on the screen, I am Goku! Welcome to the Dragon Ball game designed by SaHuL.")
print("Your mission is to find the Dragon Balls and summon Shenron for your wish.")
choice1 = input('Type "start" if you are ready: ').lower()

if choice1 == "start":
    print("That's a brave move! All the best to finish this gameplay!")
    
    dragon_balls = 0  # Initialize Dragon Balls counter
    
    # Encounter 1: Vegeta
    q1 = input('You meet Vegeta! Do you want to "Fight", "Run", or "Call for help"? ').lower()
    
    if q1 == "fight":
        print("Wow! You defeated Vegeta! Here is your first Dragon Ball!")
        dragon_balls += 1
    elif q1 == "run":
        print("You escaped from Vegeta! You'll need to face him later.")
    elif q1 == "call for help":
        print("Goku helped you defeat Vegeta! You got your first Dragon Ball!")
        dragon_balls += 1
    else:
        print("You didn't choose wisely. Vegeta escaped!")
    
    # Encounter 2: Freeza
    q2 = input('Now you face Freeza! "Fight", "Run", or "Call for help"? ').lower()
    
    if q2 == "fight":
        print("Incredible! You defeated Freeza! Here’s your second Dragon Ball!")
        dragon_balls += 1
    elif q2 == "run":
        print("You managed to escape Freeza! Be ready to fight him later.")
    elif q2 == "call for help":
        print("Goku came to the rescue! You got the second Dragon Ball!")
        dragon_balls += 1
    else:
        print("You hesitated, and Freeza is gone.")
    
    # Encounter 3: Majin Buu
    q3 = input('Majin Buu appears! Do you "Fight", "Run", or "Call for help"? ').lower()
    
    if q3 == "fight":
        print("You defeated Majin Buu! Take your third Dragon Ball!")
        dragon_balls += 1
    elif q3 == "run":
        print("You got away from Majin Buu. Be careful!")
    elif q3 == "call for help":
        print("Goku helped you again! You earned the third Dragon Ball!")
        dragon_balls += 1
    else:
        print("Majin Buu escaped.")
    
    # Encounter 4: Cell
    q4 = input('Now you face Cell! "Fight", "Run", or "Call for help"? ').lower()
    
    if q4 == "fight":
        print("Great job! You defeated Cell! Here is your fourth Dragon Ball!")
        dragon_balls += 1
    elif q4 == "run":
        print("You escaped Cell. Be ready to fight him later.")
    elif q4 == "call for help":
        print("Gohan helped you defeat Cell! You earned the fourth Dragon Ball!")
        dragon_balls += 1
    else:
        print("Cell escaped!")
    
    # Encounter 5: Piccolo
    q5 = input('Piccolo is blocking your way! "Fight", "Run", or "Call for help"? ').lower()
    
    if q5 == "fight":
        print("You managed to defeat Piccolo! Fifth Dragon Ball is yours!")
        dragon_balls += 1
    elif q5 == "run":
        print("You chose to run from Piccolo. Be careful!")
    elif q5 == "call for help":
        print("Trunks came to help! You earned your fifth Dragon Ball!")
        dragon_balls += 1
    else:
        print("Piccolo escaped.")
    
    # Encounter 6: Android 18
    q6 = input('Now you face Android 18! "Fight", "Run", or "Call for help"? ').lower()
    
    if q6 == "fight":
        print("Well done! You defeated Android 18! Sixth Dragon Ball is yours!")
        dragon_balls += 1
    elif q6 == "run":
        print("You escaped from Android 18. She will be back.")
    elif q6 == "call for help":
        print("Krillin helped you! You earned the sixth Dragon Ball!")
        dragon_balls += 1
    else:
        print("Android 18 is gone!")
    
    # Encounter 7: Broly
    q7 = input('Broly is approaching! Your final challenge! "Fight", "Run", or "Call for help"? ').lower()
    
    if q7 == "fight":
        print("Unbelievable! You defeated Broly! You have the final Dragon Ball!")
        dragon_balls += 1
    elif q7 == "run":
        print("You escaped Broly. But you need that final Dragon Ball!")
    elif q7 == "call for help":
        print("Vegeta helped you defeat Broly! You have the final Dragon Ball!")
        dragon_balls += 1
    else:
        print("Broly escaped!")
    
    # Check if the player has collected all 7 Dragon Balls
    if dragon_balls == 7:
        print("Congratulations! You've collected all 7 Dragon Balls!")
        q8 = input('Type "summon" to call Shenron: ').lower()
        
        if q8 == "summon":
            print("Shenron has been summoned! Make your wish!")
        else:
            print("You hesitated... Shenron has disappeared.")
    else:
        print(f"You only collected {dragon_balls} Dragon Balls. Keep going!")
else:
    print("You chose not to start the game. Goodbye!")
