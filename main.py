import random
user_guess = ""
n = 5
word_list = ["eevee", "addie", "jenna", "clone", "games", "lists", "codes"]
random_word = list(random.choice(word_list))
def word_checker(user_guess, n):
    if n == 0:
        return
    user_guess = list(input("Type in a five-letter word:"))
    while user_guess != random_word:
        for i in user_guess:
            if i in random_word and user_guess.index == random_word.index:
                print("\033[0;32m" + i + "\033[0m")

            elif i in random_word:
                print("\033[34m" + i + "\033[0m")
            else:
                print(i)
        break
    print(word_checker(user_guess, n))
    word_checker(user_guess, n - 1)         
    return
word_checker(user_guess, n)


