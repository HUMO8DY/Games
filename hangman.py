import random                                   #Libs
#We import random lib to make the programe chose the word randomly from a list.

#Function of hangman
def hangman():
    #create a list 'word' and make a random choice method to chose a random word from this list
    word = random.choice(['experience','government','second','technology','weapon','worker','arrangement','coalition','tiger','lion','pen','pugger','accompany','superman','bat','meow'])

    #Rules
    #create a variable that contain the letters that the user can use while playing the game
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    #create a variable contains the number of tryes
    turns = 10
    #create a variable that will have the guess made of the word
    guessmade = ''
    
    #Game loop
    while len(word) > 0:
        main = "_"*len(word)                    # the _ that will apear to the user to guess the word
        missed = 0                              # number of user's missing
        
        for letter in word:                     #loop edit the question with right letters
            if letter in guessmade:
                main = main + letter
            else:
                main = main + '_' + ''
        
        if main == word:
            print(main)
            print('You win!')
            break
        
        print('Guess the word!:' , main )
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            # A random list of messageses
            print(random.choice(['Wrong, try again','Ag Oh , try anouther one.','oh no!. well, try again.','you lost another try, try to guess again']))
            guess = input()
        if guess is not word:
            turns = turns - 1                   #decrease one try from user's trys
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

#User interface
name = input('Enter your name: \n')
print(f'Welcome to hangman game, {name}')
print('+-'*30)
print('TRY TO SURVIVE AND GUESS THE ANONYMOS WORD')
print('YOU ONLY HAVE 10 TRYS')
print('+-'*30)
hangman()
print()