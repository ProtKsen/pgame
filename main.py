"""Simple text game.

Made for the competition https://vk.com/wall-193480984_1163
I believe it's strategy.
"""
import datetime
import interactions
from add_functions import *
from texts import *
from classes import Player, Team
from random import randint


def main():
    clear()
    # parameters affecting the difficulty
    start_money = 7
    number_of_islands = 10

    # initialization of a player and team
    player = Player(money=start_money)
    team = Team()

    # start game
    my_print = printing(print)
    my_print(greeting)
    transition()
    my_print(name_question)
    name = input()
    clear()
    my_print(introduction)
    transition()
    win, lose, ext = False, False, False
    n_current_island = 1

    while not (win or lose or ext):
        # initialization of island
        skill_logic = randint(0, n_current_island)
        skill_power = randint(0, n_current_island - skill_logic)
        skill_agility = n_current_island - skill_logic - skill_power
        current_island = [skill_logic, skill_power, skill_agility, n_current_island]

        # oracle
        my_print(player.inform,
                 'На очереди остров ' + str(n_current_island) + '.', sep='\n')
        transition()
        my_print(oracle_question)
        go_oracle = get_correct_answer('1', '2')
        clear()
        oracle_answer_str = ''
        if go_oracle == '1':
            print(separator)
            oracle_answer_str = interactions.ask_oracle(player, current_island)
            transition()
            if oracle_answer_str:
                my_print('После долгих ритуалов оракул говорит, что ',
                         oracle_answer_str, sep='\n')
            transition()
            if player.money < 1:
                lose = True
                break

        # tavern
        my_print(go_tavern_text)
        transition()
        interactions.hire_command(player, team, oracle_answer_str, n_current_island)
        transition()

        # strike
        my_print(team.inform, 'Вперед, на остров!', sep='\n')
        transition()
        diff = interactions.check_attack(current_island, team)
        if diff[0] <= 0 and diff[1] <= 0 and diff[2] <= 0:
            player.money += current_island[3]
            n_current_island += 1
            my_print(success_step, sep='\n')
            transition()
        else:
            my_print(failure_step, sep='\n')
            transition()

        # check if the game should be continued
        my_print(exit_question)
        ext_ans = get_correct_answer('1', '2')
        clear()
        if ext_ans == '2':
            ext = True

        # check win or lose
        team.reset_command()
        if player.money < 1:
            lose = True
        elif n_current_island == number_of_islands + 1:
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
        my_print(winning)
    elif lose:
        my_print(losing)
    else:
        print('Конец игры.')


if __name__ == '__main__':
    main()
