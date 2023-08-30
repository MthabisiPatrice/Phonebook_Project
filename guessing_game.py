import random

word_list = ['make','market','mercedes','ghost','nike']
# Have a secret word stored in the program.
secret_word = random.choice(word_list)
print()

print('Welcome to my word guessing game')
# Prompt the user for a guess.
for i in secret_word:
    # print(f'_{i}', end='')
    print('_',end=" ") 
print()
guess = input('What is your guess ? ').lower()
guess_count = 1

# Continue looping as long as that guess is not correct.
while guess != secret_word:
    if len(guess) != len(secret_word):
        print('Sorry wrong length!! ')
    else:
        for index,letter in enumerate(guess):
            if letter.lower() == secret_word[index]:
                print(letter.upper(),end=" ")
            elif letter.lower() in secret_word:
                print(letter.lower(),end=" ")
            else:
                print('_',end=" ")
        print()
    guess = input('What is your guess ? ').lower()
    guess_count += 1
# Calculate the number of guesses and display it at the end.
print('Congrats You guessed it right champ!! ')
print(f'You made {guess_count} number of guesses champ! ')
# You do not need to have any hints at this point.