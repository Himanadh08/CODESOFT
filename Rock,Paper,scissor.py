import random
choice = ("rock","paper","scissors")
user_score =0
comp_score = 0
while True:

   user_choice = input("select rock or paper or scissors: ")
   comp_Choice = random.choice(choice)
   print("Comp choice = ",comp_Choice)
   

   if user_choice== "rock" and comp_Choice == "scissors" or user_choice == "paper" and comp_Choice == "rock" or user_choice == 'scissors' and comp_Choice == 'paper' :
    print("Win")
    user_score+=1
   elif user_choice == comp_Choice:
     print("Tie")
   else:
    print("lose")
    comp_score+=1

   print("user score = ",user_score)
   print("Computer score = ", comp_score)
   play_again = input("Do you want to play again yes or no:  ")
   if play_again != "yes":
      break
print("THANKS FOR PLAYING")



