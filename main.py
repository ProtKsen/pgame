"""Simple text game.

Made for the competition https://vk.com/wall-193480984_1163
I believe it's strategy.
"""
import datetime
from utilities import get_correct_answer, clear, printing, transition
from texts import EXIT_QUESTION, WINNING, LOSING
from classes import Player, Team
from Game import Game


def main():
    print_in_frame = printing(print)
    clear()
    # parameters affecting the difficulty
    start_money = 7
    number_of_islands = 10

    # initialization of a player and team
    player = Player(money=start_money)
    team = Team()
    game = Game(player, team)

    game.greet_player()
    transition()
    game.ask_name()
    clear()
    game.choose_difficulty_level()
    clear()
    game.print_introduction()
    transition()

    win, lose, ext = False, False, False
    n_current_island = 1
    while not (win or lose or ext):
        game.initialize_islands()

        print_in_frame(player.inform,
                       'На очереди остров ' + str(n_current_island) + '.', sep='\n')
        transition()
        # oracle
        go_oracle = game.ask_about_oracle()
        clear()
        if go_oracle == '1':
            game.talk_with_oracle()
            if player.money < 1:
                lose = True
                break
        transition()

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
        elif game.n_current_island == number_of_islands + 1:
            win = True

    # game over
    with open('records.txt', 'a') as f_out:
        today = datetime.datetime.today()
        f_out.write(today.strftime("%d-%m-%Y %H:%M") + ' | ' +
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
