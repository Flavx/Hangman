import random

print("H A N G M A N")

secret_words = ['python', 'java', 'kotlin', 'javascript']
discovered_letters = list()
sr_letter = None

while sr_letter != "exit":

    print()
    cp_word = random.choice(secret_words)
    guessed_word = list(len(cp_word) * "-")
    print_guessed_word = "".join(guessed_word)
    trials = 0
    discovered_letters.clear()
    sr_letter = input('Type "play" to play the game, "exit" to quit: > ')

    if sr_letter == "play":

while True:
    print()
    print("".join(guessed_word))

    sr_letter = input(f"Input a letter: > ")

    if sr_letter == "exit":
        break

    elif len(sr_letter) != 1:
        print("You should input a single letter")

    elif sr_letter in discovered_letters:
        print("You already typed this letter")

    elif sr_letter.isascii() and \
            not sr_letter.isalpha():
        print("It is not an ASCII lowercase")

    elif sr_letter.isupper():
        print("It is not an ASCII lowercase")

    elif sr_letter in set(cp_word):
        indices = [i for i, x in enumerate(list(cp_word)) if x == sr_letter]
        for i in indices:
            guessed_word[i] = sr_letter
        if "-" not in set(guessed_word):
            print("You guessed the word!\n"
                  "You survived!")
            break

    elif sr_letter not in set(cp_word):
        print("No such letter in the word")
        trials += 1

    if trials == 8:
        print("You are hanged!")
        break

    discovered_letters.append(sr_letter)
