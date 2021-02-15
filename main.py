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
from Game import Game

def main():
    print_in_frame = printing(print)
    clear()
    # parameters affecting the difficulty
    START_MONEY = 7
    NUMBER_OF_ISLANDS = 10

    # initialization of a player and team
    player = Player(money=START_MONEY)
    team = Team()
    game = Game(player, team)

    game.greet_player()
    transition()
    game.ask_name()
    transition()
    game.choose_difficulty_level()
    transition()
    game.print_introduction()
    transition()
    win, lose, ext = False, False, False
    n_current_island = 1

    while not (win or lose or ext):
        game.initialize_islands()
        go_oracle = game.ask_about_oracle()
        transition()

        oracle_answer_str = ''
        if go_oracle == '1':
            game.talk_with_oracle()
            if player.money < 1:
                lose = True
                break

        # tavern
        game.action_in_tavern()
        transition()

        # strike
        print_in_frame(team.inform, 'Вперед, на остров!', sep='\n')
        transition()
        game.try_get_chest()

        # check if the game should be continued
        print_in_frame(EXIT_QUESTION)
        ext_ans = get_correct_answer('1', '2')
        clear()
        if ext_ans == '2':
            ext = True

        # check win or lose
        team.reset_command()
        if player.money < 1:
            lose = True
        elif game.n_current_island == NUMBER_OF_ISLANDS + 1:
            win = True

    # game over
    with open('records.txt', 'a') as f_out:
        today = datetime.datetime.today()
        f_out.write(today.strftime("%d-%m-%Y %H.%M") + ' | ' +
                    'Player: ' + game.player_name + ', ' + 'coins: ' +
                    str(player.money) + ', islands passed: ' +
                    str(n_current_island - 1) + '\n')
    print(player.inform)
    if win:
        print_in_frame(WINNING)
    elif lose:
        print_in_frame(LOSING)
    else:
        print('Конец игры.')


if __name__ == '__main__':
    main()
