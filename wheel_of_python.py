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
    return puzz_list
    
def spin_wheel(wheel):
    return random.choice(wheel)

def main():
    print("Welcome to Wheel of Python!")
    print("To begin, please enter the names of the players:")
    p1name = input("Player 1's name: ")
    p2name = input("Player 2's name: ")
    p3name = input("Player 3's name: ")
    
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
    
    cur_puzz = random.choice(puzzles_list)
    
main()