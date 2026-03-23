import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# displays instructions

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

- Choose Rock / Paper / Scissors
- Try to beat the computer

Good Luck

    """)

# checks for integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)


        # check for infinite mode
        if to_check == "":
            return"infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# compares user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    # If the user and the computer choice is the same, it's a tie
    if user == comp:
        var_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        var_result = "win"
    elif user == "scissors" and comp == "paper":
        var_result = "win"
    elif user == "rock" and comp == "scissors":
        var_result = 'win'

    # if it's not a win / tie, then it's a loss
    else:
        var_result = "lose"

    return var_result


# Main Routine Starts Here

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📃✂️ Rock / Paper / Scissors Game 💎📃✂️")
print()

# ask the user if they want instructions (check they say yes / no)
# them if requested
want_instructions = string_checker("Do you want to see the instructions ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Display round heading based on the mode
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\n💿 Round {rounds_played + 1} of {num_rounds} 💿"

    print(rounds_heading)
    print()

    # get user choice, check it's R/P/S or 'xxx'
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    # make computer randomly choose from the rps list (excluding the exit codes)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area