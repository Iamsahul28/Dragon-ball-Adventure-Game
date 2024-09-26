import random

game = input("Type 'start' to start the game: ").lower()
total_formats = ["rock1", "paper1", "scissor1"]
cpu = random.randint(0, 2)

if game == 'start':
    control = int(input('"1" for rock, "2" for paper, and "3" for scissor: ')) - 1

    if control == 0:
        print('''  
            _______
        ---'   ____)  
              (_____)  
              (_____)  
              (____)
        ---.__(___)  
        ''')
    elif control == 1:
        print('''  
           _______
       ---'   ____)____  
                 ______)  
                 _______)  
                _______)
       ---.__________)  
       ''')
    elif control == 2:
        print('''  
           _______
       ---'   ____)____  
                 ______)  
              __________)  
             (____)
       ---.__(___)  
       ''')
    else:
        print("Invalid choice!")
        exit()

    if cpu == 0:
        print('''  
           _______
       ---'   ____)  
             (_____)  
             (_____)  
             (____)
       ---.__(___)  
       ''')
    elif cpu == 1:
        print('''  
           _______
       ---'   ____)____  
                 ______)  
                 _______)  
                _______)
       ---.__________)  
       ''')
    elif cpu == 2:
        print('''  
           _______
       ---'   ____)____  
                 ______)  
              __________)  
             (____)
       ---.__(___)  
       ''')

    print(f"CPU choice: {cpu + 1}")

    if control == cpu:
        print("Draw")
    elif (control == 0 and cpu == 2) or (control == 1 and cpu == 0) or (control == 2 and cpu == 1):
        print('You won!')
    else:
        print('Computer won!')
