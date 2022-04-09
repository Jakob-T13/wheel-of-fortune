import random

def generate_wheel():
    wheel_lst = []
    wheel_choice = input("Would you like to play with the (n)ormal wheel, or the (e)vil wheel? ")
    if wheel_choice == 'e':
        wheelf = open("evil_wheel.txt", "rt")
        wheel_lst = wheelf.readlines()
        wheelf.close()
    else:
        wheelf = open("basic_wheel.txt", "rt")
        wheel_lst = wheelf.readlines()
        wheelf.close()

    for i in range(len(wheel_lst)):
        wheel_lst[i] = wheel_lst[i].strip()
    
    return wheel_lst
    
def generate_puzz_list():
    puzzf = open("puzzles.txt", "rt")
    puzz_list = puzzf.readlines()
    puzzf.close
    for i in range(len(puzz_list)):
        puzz_list[i] = puzz_list[i].strip()
        puzz_list[i] = puzz_list[i].upper()
    return puzz_list
    
def spin_wheel(wheel):
    return random.choice(wheel)
    
def txt_to_displaylist(stringin):
    out = []
    for i in stringin:
        if i == ' ':
            out += ' '
        else:
            out += '_'
    return out

def main():
    titlef = open("title.txt", "rt")
    titletext = titlef.read()
    titlef.close()
    print(titletext)
    print("Welcome to Wheel of Python!")
    print("To begin, please enter the names of the players:")
    p1name = input("Player 1's name: ")
    p2name = input("Player 2's name: ")
    p3name = input("Player 3's name: ")
    
    players = [p1name, p2name, p3name]
    
    playerscores = {
        p1name : 0,
        p2name : 0,
        p3name : 0
    }
    
    playerbanks = {
        p1name : 0,
        p2name : 0,
        p3name : 0
    }
    
    play_wheel = generate_wheel()
    
    puzzles_list = generate_puzz_list()
    
    cur_puzz = random.choice(puzzles_list).upper()
    puzz_display = txt_to_displaylist(cur_puzz)
    rem_cons = list("BCDFGHJKLMNPQRSTVWXYZ")
    rem_vows = list("AEIOU")
    currentplayer = 1
    
    #round 1
    print("ROUND 1\n")
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
                            playerbanks[players[currentplayer-1]] = playerscores[players[currentplayer-1]]
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
        
    print("==========\n")
        
    cur_puzz = random.choice(puzzles_list).upper()
    puzz_display = txt_to_displaylist(cur_puzz)
    rem_cons = list("BCDFGHJKLMNPQRSTVWXYZ")
    rem_vows = list("AEIOU")
    
    #round 2
    print("ROUND 2\n")
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
                            playerbanks[players[currentplayer-1]] = playerscores[players[currentplayer-1]]
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
        
    print(f"Congratulations {players[currentplayer-1]} for winning the round! The current standings are:")
    for i in range(3):
        print(f"{players[i]}: ${playerbanks[players[i]]}")
    for i in range(3):
        playerscores[players[i]] = 0
        
    finalscores = [playerbanks[players[0]],playerbanks[players[1]],playerbanks[players[2]]]
    highscore = max(finalscores)
    winner = players[finalscores.index(highscore)]
    print(f"\nCongratulations {winner} on winning the game!")
    print("Let's see if you can win a bonus $25000 in the bonus round!")
    
    #bonus round
    cur_puzz = random.choice(puzzles_list).upper()
    puzz_display = txt_to_displaylist(cur_puzz)
    rem_cons = list("BCDFGHJK_M_PQ___VWXYZ")
    rem_vows = list("A_IOU")
    given_letters = list("RSTLNE")
    player_letters = []
    for i in given_letters:
        for j in range(len(puzz_display)):
            if cur_puzz[j] == i:
                puzz_display[j] = i
    
    print('\n'+''.join(puzz_display)+'\n')
    print(''.join(rem_cons))
    print(''.join(rem_vows)+'\n')
    letterselect = True
    for i in range(3):
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
    while vowel_choice:
        ui = input("Choose a vowel: ").upper()
        if len(ui) == 1 and ui in rem_vows:
            player_letters += ui
            vowel_choice = False
        else:
            print("That isn't a valid letter. Please try again.")
    for i in player_letters:
        for j in range(len(puzz_display)):
            if cur_puzz[j] == i:
                puzz_display[j] = i
    
    print('\n'+''.join(puzz_display)+'\n')
    ui = input(f"{winner}, you have one guess to solve this puzzle. What is your guess? ").upper()
    if ui == cur_puzz:
        print("Congratulations, you got it right!")
        highscore += 25000
    else:
        print("Sorry, but that's not correct. The correct answer was:")
        print(cur_puzz)
    print(f"{winner} won a total of ${highscore}!\nThanks for playing!")
main()