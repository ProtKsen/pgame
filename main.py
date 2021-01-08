"""Simple text game.

Made for the competition https://vk.com/wall-193480984_1163
I believe it's strategy.
"""
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
    island_treasure = [3 * i for i in range(1, 11)]

    # initialization of a player and islands
    player = Player(money=start_money)
    team = Team()
    islands = []
    for i in range(1, number_of_islands + 1):
        skill_logic = randint(0, i)
        skill_power = randint(0, i - skill_logic)
        skill_agility = i - skill_logic - skill_power
        islands.append([skill_logic, skill_power, skill_agility, island_treasure[i - 1]])

    # start game
    my_print = printing(print)
    my_print(greeting)
    transition()
    my_print(introduction)
    transition()
    win, lose = False, False
    current_island = 1

    while not (win or lose):
        # oracle
        my_print(player.inform,
                 'На очереди остров ' + str(current_island) + '.', sep='\n')
        transition()
        my_print(oracle_question)
        go_oracle = get_correct_answer('1', '2')
        transition()
        oracle_answer_str = ''
        if go_oracle == '1':
            print(separator)
            oracle_answer_str = interactions.ask_oracle(player, islands[current_island - 1])
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
        interactions.hire_command(player, team, oracle_answer_str, current_island)
        transition()

        # strike
        my_print(team.inform, 'Вперед, на остров!', sep='\n')
        transition()
        diff = interactions.check_attack(islands[current_island - 1], team)
        if diff[0] <= 0 and diff[1] <= 0 and diff[2] <= 0:
            player.money += islands[current_island - 1][3]
            current_island += 1
            my_print(success_step, sep='\n')
            transition()
        else:
            my_print(failure_step, sep='\n')
            transition()

        # check win or lose
        team.reset_command()
        if player.money < 1:
            lose = True
        elif current_island == 11:
            win = True

    # game over
    if win:
        my_print(winning)
    elif lose:
        my_print(losing)
    else:
        print('Error')


if __name__ == '__main__':
    main()
