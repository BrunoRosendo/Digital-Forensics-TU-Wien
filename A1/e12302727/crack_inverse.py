import math

print("Let's see how long your password needs to be to be secure for 10 years!")
print()

GUESSES_PER_SECOND = int(input("Enter the number of guesses per second: "))
CHAR_OPTIONS = int(input("Enter the number of possible characters: "))

TOTAL_SECONDS = 315569260
NUM_COMBINATION = TOTAL_SECONDS * GUESSES_PER_SECOND

password_length = math.log(NUM_COMBINATION) / math.log(CHAR_OPTIONS)
real_password_length = math.ceil(password_length)

print(
    f"Your password needs to be {real_password_length} characters long to be secure for 10 years!"
)
