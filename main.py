"""Simple text game.

Made for the competition https://vk.com/wall-193480984_1163
I believe it's strategy.
"""
import datetime
from random import randint
from interactions import ask_oracle, hire_command, check_attack
from utilities import get_correct_answer, clear, printing, transition
from texts import GREETING, NAME_QUESTION, CHOOSE_LEVEL, INTRODUCTION, \
    ORACLE_QUESTION, SEPARATOR, GO_TAVERN_TEXT, SUCCESS_STEP, FAILURE_STEP, \
    EXIT_QUESTION, WINNING, LOSING
from classes import Player, Team


def main():
    clear()
    # parameters affecting the difficulty
    START_MONEY = 7
    NUMBER_OF_ISLANDS = 10

    # initialization of a player and team
    player = Player(money=START_MONEY)
    team = Team()

    # start game
    my_print = printing(print)
    my_print(GREETING)
    transition()
    my_print(NAME_QUESTION)
    name = input()
    clear()
    my_print(CHOOSE_LEVEL)
    level = get_correct_answer('1', '2', '3')
    if level == '1':
        level = 4
    elif level == '2':
        level = 3
    else:
        level = 2
    clear()
    my_print(INTRODUCTION)
    transition()
    win, lose, ext = False, False, False
    n_current_island = 1

    while not (win or lose or ext):
        # initialization of island
        skill_logic = randint(0, n_current_island)
        skill_power = randint(0, n_current_island - skill_logic)
        skill_agility = n_current_island - skill_logic - skill_power
        current_island = [
            skill_logic, skill_power,
            skill_agility, n_current_island * level
        ]

        # oracle
        my_print(player.inform,
                 'На очереди остров ' + str(n_current_island) + '.', sep='\n')
        transition()
        my_print(ORACLE_QUESTION)
        go_oracle = get_correct_answer('1', '2')
        clear()
        oracle_answer_str = ''
        if go_oracle == '1':
            print(SEPARATOR)
            oracle_answer_str = ask_oracle(player, current_island)
            transition()
            if oracle_answer_str:
                my_print('После долгих ритуалов оракул говорит, что ',
                         oracle_answer_str, sep='\n')
            transition()
            if player.money < 1:
                lose = True
                break

        # tavern
        my_print(GO_TAVERN_TEXT)
        transition()
        hire_command(player, team, oracle_answer_str, n_current_island)
        transition()

        # strike
        my_print(team.inform, 'Вперед, на остров!', sep='\n')
        transition()
        diff = check_attack(current_island, team)
        if diff[0] <= 0 and diff[1] <= 0 and diff[2] <= 0:
            player.money += current_island[3]
            n_current_island += 1
            my_print(SUCCESS_STEP, sep='\n')
            transition()
        else:
            my_print(FAILURE_STEP, sep='\n')
            transition()

        # check if the game should be continued
        my_print(EXIT_QUESTION)
        ext_ans = get_correct_answer('1', '2')
        clear()
        if ext_ans == '2':
            ext = True

        # check win or lose
        team.reset_command()
        if player.money < 1:
            lose = True
        elif n_current_island == NUMBER_OF_ISLANDS + 1:
            win = True

    # game over
    with open('records.txt', 'a') as f_out:
        today = datetime.datetime.today()
        f_out.write(today.strftime("%d-%m-%Y %H.%M") + ' | ' +
                    'Player: ' + name + ', ' + 'coins: ' +
                    str(player.money) + ', islands passed: ' +
                    str(n_current_island - 1) + '\n')
    print(player.inform)
    if win:
        my_print(WINNING)
    elif lose:
        my_print(LOSING)
    else:
        print('Конец игры.')


if __name__ == '__main__':
    main()
