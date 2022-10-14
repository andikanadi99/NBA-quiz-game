#A quick mini game that ask the user 5 nba type questions, keeps a score and displays the final score to the screen

#Intro message
print("\nWelcome the NBA quiz!\nThis quiz will ask you 10 nba questions to test your knowledge of the professional League.\n")

#Ask user if they want to play the game
user_input = input("To play the game, type yes. Anything else inputted will cause the game to quit.\nDo you want to play? ")
if user_input.lower() != 'yes':
  exit()
print('\n')

#10 questions with answers
score = 0
#1.
answer = input("How many championships does Bill Russell have? ")
if answer == str(11):
  score += 1

#2.
answer = input("Who won the 2018 NBA MVP? ")
if answer.lower() == 'james harden':
  score += 1

#3.
answer = input("How many scoring titles does Michael Jordan have? ")
if answer == str(9):
  score += 1

#4.
answer = input("Who is the all time scoring leader of the NBA? ")
if answer.lower() == 'kareem abdul jabaar':
  score += 1

#5.
answer = input("Who is the only player to win NBA Finals MVP on the losing finals team? ")
if answer.lower() == 'jerry west':
  score += 1

#Print final game score:
print('\n')
print("You scored " + str(score) + " / 5")


