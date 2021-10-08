

def draw(movie_str, guess_letter, guess_str):
    i = 0
    while i < movie_str.__len__():
        if movie_str[i] == guess_letter:
            guess_str = guess_str[:i] + guess_letter + guess_str[i+1:]
        i += 1
    return guess_str


tries = 5
movie = input("Name of the Movie: ")
guess_string = "*" * movie.__len__()
print(f"${guess_string}$")
roll = 0
while roll < tries:
    guess = input("Guess a letter: ")
    guess_string = draw(movie, guess, guess_string)
    print(guess_string)
    roll += 1

print("Max tries over")










