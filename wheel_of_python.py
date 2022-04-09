import random

def generate_wheel():   #Choose from a "normal" wheel list or an "evil" one with four bankrupts
    wheel_lst = []      #output list
    wheel_choice = input("Would you like to play with the (n)ormal wheel, or the (e)vil wheel? ")
    if wheel_choice == 'e':
        wheelf = open("evil_wheel.txt", "rt")
        wheel_lst = wheelf.readlines()
        wheelf.close()
    else:
        wheelf = open("basic_wheel.txt", "rt")
        wheel_lst = wheelf.readlines()
        wheelf.close()

    for i in range(len(wheel_lst)):     #remove newline chars from each string in the list
        wheel_lst[i] = wheel_lst[i].strip()
    
    return wheel_lst
    
def generate_puzz_list():               #generate a list of puzzles from a file
    puzzf = open("puzzles.txt", "rt")   #open file
    puzz_list = puzzf.readlines()       #read file into a list by lines
    puzzf.close                         #close the file
    for i in range(len(puzz_list)):     #strip newlines and set all text to UPPERCASE
        puzz_list[i] = puzz_list[i].strip()
        puzz_list[i] = puzz_list[i].upper()
    return puzz_list
    
def spin_wheel(wheel):                  #"spin" the "wheel" to get a random result from the wheel list
    return random.choice(wheel)
    
def txt_to_displaylist(stringin):       #convert immutable string to mutable character list of _s
    out = []                #output list
    for i in stringin:      #for each character in the input string:
        if i == ' ':        #if the character is a space
            out += ' '      #append a space
        else:               #otherwise
            out += '_'      #append an underscore
    return out

def main():
    titlef = open("title.txt", "rt")        #title text from a file (generated from https://patorjk.com/software/taag/)
    titletext = titlef.read()
    titlef.close()
    print(titletext)
    print("Welcome to Wheel of Python!")
    print("To begin, please enter the names of the players:")   #enter player names
    p1name = input("Player 1's name: ")
    p2name = input("Player 2's name: ")
    p3name = input("Player 3's name: ")
    
    players = [p1name, p2name, p3name]      #iterable list of player names
    
    playerscores = {        #dictionary to store player round scores
        p1name : 0,
        p2name : 0,
        p3name : 0
    }
    
    playerbanks = {         #dictionary to store player banked scores
        p1name : 0,
        p2name : 0,
        p3name : 0
    }
    
    play_wheel = generate_wheel()   #generate the wheel to be used
    
    puzzles_list = generate_puzz_list()     #generate the list of puzzles to pick from
    
    cur_puzz = random.choice(puzzles_list).upper()      #pick a random puzzle from the list
    puzz_display = txt_to_displaylist(cur_puzz)         #create its blank display
    rem_cons = list("BCDFGHJKLMNPQRSTVWXYZ")            #list of available consonants
    rem_vows = list("AEIOU")                            #list of available vowels
    currentplayer = 1           #current player tracker
    
    #round 1
    print("ROUND 1\n")
    puzzle_not_solved = True
    while puzzle_not_solved:        #while the puzzle hasn't been solved:
        print('\n'+''.join(puzz_display)+'\n')      #display the puzzle's current state
        print(''.join(rem_cons))                    #display available consonants
        print(''.join(rem_vows)+'\n')               #display available vowels
        input(f"Press Enter to spin the wheel, {players[currentplayer-1]}!")    #prompt to spin the wheel
        spin_result = spin_wheel(play_wheel)        #"spin" the "wheel"
        print(spin_result)                          #display wheel result
        if spin_result != "BANKRUPT" and spin_result != "LOSE A TURN":      #if not bankrupt or lose a turn
            letterselect = True
            while letterselect:
                ui = input("Choose a consonant: ").upper()  #ask user for a consonant
                if len(ui) == 1 and ui in rem_cons:         #if it's valid
                    rem_cons[rem_cons.index(ui)] = '_'      #remove it from the available consonants
                    letterselect = False
                else:                                               #else
                    print("That isn't a valid letter. Try again.")  #let the user try again
            if ui in cur_puzz:                          #if the letter is in the puzzle
                for i in range(len(puzz_display)):      #fill the display with each instance of the letter
                    if cur_puzz[i] == ui:
                        playerscores[players[currentplayer-1]] += int(spin_result)  #and increment player's score for each instance
                        puzz_display[i] = ui
                main_turn = True        #enter post-spin segment of turn
                while main_turn:
                    print(''.join(puzz_display))    #print puzzle status and player's score
                    print(''.join(rem_cons))
                    print(''.join(rem_vows))
                    print(f"{players[currentplayer-1]}: ${playerscores[players[currentplayer-1]]}")
                    ui = input("Would you like to (s)pin again, (b)uy a vowel, or s(o)lve the puzzle? ").lower()    #ask the player what they want to do
                    if ui == "s":   #spin again
                        main_turn = False
                    elif ui == "b": #buy a vowel
                        if playerscores[players[currentplayer-1]] >= 250:   #if they have enough to buy
                            playerscores[players[currentplayer-1]] -= 250   #deduct cost
                            vowel_choice = True
                            while vowel_choice:
                                ui = input("Choose a vowel: ").upper()      #choose a vowel
                                if ui in rem_vows:                          #if it's valid
                                    rem_vows[rem_vows.index(ui)] = '_'      #remove it from the list
                                    vowel_choice = False
                                else:
                                    print("That isn't a valid letter. Try again.")  #try again on invalid input
                            if ui in cur_puzz:                      #if the vowel is in the puzzle
                                for i in range(len(puzz_display)):  #fill display with each instance of the vowel
                                    if cur_puzz[i] == ui:
                                        puzz_display[i] = ui
                            else:           #if the vowel is not in the puzzle:
                                print("Sorry, that letter isn't in the puzzle.")
                                main_turn = False   #end turn
                                currentplayer += 1  #increment player tracker
                                if currentplayer > 3:   #go from player 3 to player 1
                                    currentplayer -= 3
                        else:
                            print("Sorry, you don't have enough to buy a vowel.") #if not enough to buy, don't penalize for trying
                    elif ui == "o":     #solve puzzle
                        guess = input("Enter your guess: ").upper()     #ask for guess
                        if guess == cur_puzz:       #if the guess is correct
                            playerbanks[players[currentplayer-1]] += playerscores[players[currentplayer-1]]  #bank the player's score
                            main_turn = False       #end the turn
                            puzzle_not_solved = False   #end the round
                        else:   #if guess is not correct
                            print("Sorry, that isn't the correct answer.")
                            main_turn = False   #end the turn
                            currentplayer += 1  #increment player tracker
                            if currentplayer > 3:
                                currentplayer -= 3
                    else:   #invalid input, try again
                        print("Sorry, we didn't catch that. Please try again.")
            else:   #the consonant is not in the puzzle
                print("Sorry, that letter isn't in the puzzle.")
                currentplayer += 1  #increment player tracker
                if currentplayer > 3:
                    currentplayer -= 3
        elif spin_result == "BANKRUPT":     #if bankrupt:
            print(f"Oh no! {players[currentplayer-1]} has gone bankrupt!")
            playerscores[players[currentplayer-1]] = 0      #set current player's score to 0
            currentplayer += 1      #increment player tracker
            if currentplayer > 3:
                currentplayer -= 3
        else:   #lose a turn
            print(f"{players[currentplayer-1]} has lost their turn!")
            currentplayer += 1  #increment player counter
            if currentplayer > 3:
                currentplayer -= 3
    print(f"Congratulations {players[currentplayer-1]} for winning the round! The current standings are:")
    for i in range(3):      #print post-round standings
        print(f"{players[i]}: ${playerbanks[players[i]]}")
    for i in range(3):      #reset player round scores
        playerscores[players[i]] = 0
        
    print("==========\n")
        #reset for round 2
    cur_puzz = random.choice(puzzles_list).upper()
    puzz_display = txt_to_displaylist(cur_puzz)
    rem_cons = list("BCDFGHJKLMNPQRSTVWXYZ")
    rem_vows = list("AEIOU")
    
    #round 2 - just copy/pasted from round 1
    print("ROUND 2\n")      #(Probably could've done it cleaner, but couldn't think of a solution that didn't involve OOP stuff)
    puzzle_not_solved = True
    while puzzle_not_solved:
        print('\n'+''.join(puzz_display)+'\n')
        print(''.join(rem_cons))
        print(''.join(rem_vows)+'\n')
        input(f"Press Enter to spin the wheel, {players[currentplayer-1]}!")
        spin_result = spin_wheel(play_wheel)
        print(spin_result)
        if spin_result != "BANKRUPT" and spin_result != "LOSE A TURN":
            letterselect = True
            while letterselect:
                ui = input("Choose a consonant: ").upper()
                if len(ui) == 1 and ui in rem_cons:
                    rem_cons[rem_cons.index(ui)] = '_'
                    letterselect = False
                else:
                    print("That isn't a valid letter. Try again.")
            if ui in cur_puzz:
                for i in range(len(puzz_display)):
                    if cur_puzz[i] == ui:
                        playerscores[players[currentplayer-1]] += int(spin_result)
                        puzz_display[i] = ui
                main_turn = True
                while main_turn:
                    print(''.join(puzz_display))
                    print(''.join(rem_cons))
                    print(''.join(rem_vows))
                    print(f"{players[currentplayer-1]}: ${playerscores[players[currentplayer-1]]}")
                    ui = input("Would you like to (s)pin again, (b)uy a vowel, or s(o)lve the puzzle? ").lower()
                    if ui == "s":
                        main_turn = False
                    elif ui == "b":
                        if playerscores[players[currentplayer-1]] >= 250:
                            playerscores[players[currentplayer-1]] -= 250
                            vowel_choice = True
                            while vowel_choice:
                                ui = input("Choose a vowel: ").upper()
                                if ui in rem_vows:
                                    rem_vows[rem_vows.index(ui)] = '_'
                                    vowel_choice = False
                                else:
                                    print("That isn't a valid letter. Try again.")
                            if ui in cur_puzz:
                                for i in range(len(puzz_display)):
                                    if cur_puzz[i] == ui:
                                        puzz_display[i] = ui
                            else:
                                print("Sorry, that letter isn't in the puzzle.")
                                main_turn = False
                                currentplayer += 1
                                if currentplayer > 3:
                                    currentplayer -= 3
                        else:
                            print("Sorry, you don't have enough to buy a vowel.")
                    elif ui == "o":
                        guess = input("Enter your guess: ").upper()
                        if guess == cur_puzz:
                            playerbanks[players[currentplayer-1]] += playerscores[players[currentplayer-1]]
                            main_turn = False
                            puzzle_not_solved = False
                        else:
                            print("Sorry, that isn't the correct answer.")
                            main_turn = False
                            currentplayer += 1
                            if currentplayer > 3:
                                currentplayer -= 3
                    else:
                        print("Sorry, we didn't catch that. Please try again.")
            else:
                print("Sorry, that letter isn't in the puzzle.")
                currentplayer += 1
                if currentplayer > 3:
                    currentplayer -= 3
        elif spin_result == "BANKRUPT":
            print(f"Oh no! {players[currentplayer-1]} has gone bankrupt!")
            playerscores[players[currentplayer-1]] = 0
            currentplayer += 1
            if currentplayer > 3:
                currentplayer -= 3
        else:
            print(f"{players[currentplayer-1]} has lost their turn!")
            currentplayer += 1
            if currentplayer > 3:
                currentplayer -= 3
        
    print(f"Congratulations {players[currentplayer-1]} for winning the round! The current standings are:")
    for i in range(3):
        print(f"{players[i]}: ${playerbanks[players[i]]}")
    for i in range(3):
        playerscores[players[i]] = 0
        
    finalscores = [playerbanks[players[0]],playerbanks[players[1]],playerbanks[players[2]]]     #establish final scores
    highscore = max(finalscores)        #get highest final score
    winner = players[finalscores.index(highscore)]  #get player with highest score
    print(f"\nCongratulations {winner} on winning the game!")
    print("Let's see if you can win a bonus $25000 in the bonus round!")
    
    #bonus round
    cur_puzz = random.choice(puzzles_list).upper()      #get a puzzle
    puzz_display = txt_to_displaylist(cur_puzz)         #convert it to display format
    rem_cons = list("BCDFGHJK_M_PQ___VWXYZ")            #letter list minus RSTLNE
    rem_vows = list("A_IOU")
    given_letters = list("RSTLNE")
    player_letters = []
    for i in given_letters:         #populate puzzle with given letters
        for j in range(len(puzz_display)):
            if cur_puzz[j] == i:
                puzz_display[j] = i
    
    print('\n'+''.join(puzz_display)+'\n')  #display current puzzle status
    print(''.join(rem_cons))
    print(''.join(rem_vows)+'\n')
    letterselect = True
    for i in range(3):          #prompt player for 3 consonants
        letterselect = True
        while letterselect:
            ui = input(f"Choose consonant #{i+1}: ").upper()
            if len(ui) == 1 and ui in rem_cons:
                player_letters += ui
                rem_cons[rem_cons.index(ui)] = '_'
                letterselect = False
            else:
                print("That isn't a valid letter. Please try again.")
    vowel_choice = True
    while vowel_choice:     #prompt player for a vowel
        ui = input("Choose a vowel: ").upper()
        if len(ui) == 1 and ui in rem_vows:
            player_letters += ui
            vowel_choice = False
        else:
            print("That isn't a valid letter. Please try again.")
    for i in player_letters:        #add player letters to the puzzle
        for j in range(len(puzz_display)):
            if cur_puzz[j] == i:
                puzz_display[j] = i
    
    print('\n'+''.join(puzz_display)+'\n')      #display current puzzle status
    ui = input(f"{winner}, you have one guess to solve this puzzle. What is your guess? ").upper()  #ask for player's final guess
    if ui == cur_puzz:      #if correct
        print("Congratulations, you got it right!")
        highscore += 25000  #increase final score by 25000
    else:       #if wrong
        print("Sorry, but that's not correct. The correct answer was:")
        print(cur_puzz)     #show solution
    print(f"{winner} won a total of ${highscore}!\nThanks for playing!")        #display total winnings
main()