import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_pictures = [rock, paper, scissors] 

print('''Welcome to the Game World! Develop By: Zubair Awan''')

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors.\n"))

if user_choice >= 3 and user_choice  <0 :
    
   print("You type an invalid number. You Lose.") 
   
else:
    
    print(game_pictures[user_choice])
    
    computer_choice = random.randint(0, 2)
    
    print("Computer choose:")
    
    print(game_pictures[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        
        print("You Wins.")
        
    elif computer_choice == 0 and user_choice == 2:
        
        print("You Lose.")  
      
    elif computer_choice > user_choice:
        
        print("You Lose.")
        
    elif user_choice > computer_choice:
        
        print("You Lose.")
    
    elif computer_choice == user_choice:
        
        print("It's a draw.")              
       