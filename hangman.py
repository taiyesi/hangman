import random

hangman_logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
   +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
   +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
   +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["ardvark", "baboon", "camel", "caramel", "corn", "stranger", "violet", "curtain", "jurassic", "president"]
chosen_word = random.choice(word_list)
lives = 6
print(hangman_logo)

display = []
for letter in chosen_word:
    display += '_'
print(display)

end_of_game = False 

while not end_of_game: 
    guess = input("Choose a random letter: ").lower()
    
    if guess in display:
        print("You already guessed that!")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("You guessed something that isn't in the word\nYou lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")
            
    if "_" not in display:
        end_of_game == True
        print("You win")

    print(stages[lives])