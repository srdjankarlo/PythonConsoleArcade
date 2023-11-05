import os
import time


def main_meny():
    while True:
        os.system('cls')
        print("\nWelcome to Python Console Arcade. Games available are listed bellow.")
        print("ID |Game")
        print("0  |Exit Arcade, close program")
        print("1  |Tic-Tac-Toe")
        print("2  |Snake")
        print("3  |Tower of Hanoi")
        game_to_play = input("\nChose your poison: ")
        if game_to_play not in [str(game_id) for game_id in range(4)]:  # list comprehension
            os.system('cls')
            print("Invalid input...are you mentally challenged?")
            time.sleep(2)
            continue
        else:
            break

    return game_to_play


def tic_tac_toe():
    os.system('cls')
    print("Not implemented")
    time.sleep(1)


def snake():
    os.system('cls')
    print("Not implemented")
    time.sleep(1)


def tower_of_hanoi():
    os.system('cls')
    print("Not implemented")
    time.sleep(1)


def main():
    while True:
        game_id = main_meny()
        if game_id == '0':
            print("Exiting arcade...hope to never see you again!")
            break
        elif game_id == '1':
            # ToDo: tic_tac_toe()
            tic_tac_toe()
            pass
        elif game_id == '2':
            # ToDo: snake()
            snake()
            pass
        elif game_id == '3':
            # ToDo: tower_of_hanoi()
            tower_of_hanoi()
            pass


# This helps us to prevent executing code in this script if it was called from somewhere else
if __name__ == "__main__":
    main()
