print("Let's see how secure your password is!")
print()

PASSWORD_LENGTH = int(input("Enter the length of the password: "))
CHAR_OPTIONS = int(input("Enter the number of possible characters: "))
GUESSES_PER_SECOND = int(input("Enter the number of guesses per second: "))

combinations = CHAR_OPTIONS**PASSWORD_LENGTH
total_seconds = combinations / GUESSES_PER_SECOND

years, remainder = divmod(total_seconds, 60 * 60 * 24 * 365)
days, remainder = divmod(remainder, 60 * 60 * 24)
hours, remainder = divmod(remainder, 60 * 60)
minutes, seconds = divmod(remainder, 60)
seconds = round(seconds)

print(
    f"The worst case scenario for the crack is: {int(years)}y {int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"
)
