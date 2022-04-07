import random

def ask_number(num_min, num_max):
    number_int = 0

    while number_int == 0:
        number_str = input(f"What is the magic number (between {num_min} and {num_max}) ?")
        try:
            number_int = int(number_str)
        except:
            print("ERROR: Invalid input. Try again.")
        else:
            if number_int < num_min or number_int > num_max:
                print(f"ERROR: You must enter the number between ({num_min} and {num_max})")
                number_int = 0
    return number_int

MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NUM_LIVES = 4

#LOGIC USING WHILE LOOP
"""number = 0
lives = NUM_LIVES
while not number == MAGIC_NUMBER and lives > 0:
    print(f"You have {lives} lives")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("You Won!")
    elif number > MAGIC_NUMBER:
        print("The Magic Number is Lower")
        lives -= 1
    else:
        print("The Magic Number is Greater")
        lives -= 1

if lives == 0:
    print(f"You lost! The magic number was: {MAGIC_NUMBER}") """

#LOGIC USING FOR LOOP
win = False
for i in range(0,NUM_LIVES):
    lives = NUM_LIVES - i
    print(f"You have {lives} lives")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("You Won!")
        win = True
        break
    elif number > MAGIC_NUMBER:
        print("The Magic Number is Lower")
        lives -= 1
    else:
        print("The Magic Number is Greater")
        lives -= 1

if not win:
    print(f"You lost! The magic number was: {MAGIC_NUMBER}")