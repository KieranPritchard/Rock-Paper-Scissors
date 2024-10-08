import random

#varibles

user_score = 0

cpu_score = 0

#Match Deciding

while True:
    user_choice = input("Please input from list Rock, Paper, or Scissors. (If you want to exit input Quit): ")
    if user_choice == "Quit":
        break

    cpu_choices = ["Rock", "Paper","Scissors"]
    cpu_action = random.choice(cpu_choices)

    if cpu_action == user_choice:
        print("It's a draw")

        cpu_score += 1
        user_score += 1

        print("Computer Score: " + str(cpu_score))

        print("User Score: " + str(user_score))
    elif cpu_action == "Rock" and user_choice == "Scissors" or cpu_action == "Paper" and user_choice == "Rock" or cpu_action == "Scissors" and user_choice == "Paper":
        print("You Lost")

        cpu_score += 1

        print("Computer Score: " + str(cpu_score))

        print("User Score: " + str(user_score))
    else:
        print("You Win")

        user_score += 1

        print("Computer Score: " + str(cpu_score))

        print("User Score: " + str(user_score))

    if user_choice == cpu_action:
        print("Invaild Input")

#Final Score

print("Final Scores")

print("Final Computer Score: " + str(cpu_score))

print("Final User Score: " + str(user_score))