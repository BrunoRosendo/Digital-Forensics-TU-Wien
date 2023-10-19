from matplotlib import pyplot as plt


def get_duration_string(total_seconds):
    years, remainder = divmod(total_seconds, 60 * 60 * 24 * 365)
    days, remainder = divmod(remainder, 60 * 60 * 24)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)
    seconds = round(seconds)
    return f"{int(years)}y {int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"


CHAR_OPTIONS = 79
GUESSES_PER_SECOND = 2771
MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 15

xPoints = []
yPoints = []

for i in range(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH + 1):
    xPoints.append(i)
    combinations = CHAR_OPTIONS**i
    total_seconds = combinations / GUESSES_PER_SECOND
    years = total_seconds / (60 * 60 * 24 * 365)
    yPoints.append(years)
    print(f"Password Length: {i} | Time to Crack: {get_duration_string(total_seconds)}")

plt.plot(xPoints, yPoints)
plt.xlabel("Password Length")
plt.ylabel("Time to Crack (years)")
plt.title("Password Length vs Time to Crack")
plt.show()
