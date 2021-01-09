"""The main functions of interaction with the player."""
from add_functions import *
from random import randint
from classes import Pirate


def ask_oracle(player, island):
    """Interaction with the oracle.

    Return a response of the oracle as a string.
    Change the number of player's money.
    """
    oracle_answer = ''
    if player.money >= 3:
        print(player.inform)
        print(texts.oracle_question_1)
        print(texts.separator)
        answer = get_correct_answer('1', '2', '3', '4', '5')
    else:
        print(player.inform)
        print(texts.oracle_question_2)
        answer = get_correct_answer('1', '2', '3', '4')
    if answer == '2':
        oracle_answer = 'необходимое количество очков логики ' +\
                        str(island[0]) + '.'
        player.money -= 1
    elif answer == '3':
        oracle_answer = 'необходимое количество очков силы ' +\
                        str(island[1]) + '.'
        player.money -= 1
    elif answer == '4':
        oracle_answer = 'необходимое количество очков ловкости ' +\
                        str(island[2]) + '.'
        player.money -= 1
    elif answer == '5':
        oracle_answer = 'необходимое количество очков логики, силы и ловкости '\
                        + str(island[0]) + ', ' + str(island[1]) + ' и ' \
                        + str(island[2]) + ' соответственно.'
        player.money -= 3
    return oracle_answer


def hire_command(player, team, oracle_answer_str, n_island):
    """Hire a team

    Print the list of available pirates.
    Change the number of player's money and
    team's skills in case of hiring."""
    pirates_list = []
    for i in range(7):
        new_pirate = Pirate(texts.names[randint(0, len(texts.names) - 1)],
                            randint(0, n_island + 1), randint(0, n_island + 1),
                            randint(0, n_island + 1), 0)
        new_pirate.salary = randint(1, new_pirate.logic + new_pirate.power
                                    + new_pirate.agility + 1)
        pirates_list.append(new_pirate)

    # buy
    exit_from_tavern = False
    while player.money > 0 and exit_from_tavern is False:
        clear()
        print(texts.separator)
        print(team.inform)
        print(player.inform)
        print('Ты собираешься плыть на остров ' + str(n_island) + '.', sep='')
        if oracle_answer_str:
            print('Помни, что сказал оракул:\n', oracle_answer_str, sep='')
        print(texts.separator)
        print('В таверне сидят:')
        ans = [str(i + 1) for i in range(len(pirates_list) + 1)]
        for i in range(len(pirates_list)):
            print(i + 1, ' - ', pirates_list[i].name, '.\n',
                  'Логика: ', pirates_list[i].logic, ', ',
                  'сила: ', pirates_list[i].power, ', ',
                  'ловкость: ', pirates_list[i].agility, '. ',
                  'Цена найма: ', pirates_list[i].salary,
                  coins(pirates_list[i].salary), sep='')
            print('------------------')
        print(len(pirates_list) + 1, ' - Команда собрана, уйти из таверны')
        print(texts.separator)
        player_answer = get_correct_answer(*ans)
        if player_answer == ans[-1]:
            exit_from_tavern = True
        else:
            if player.money >= pirates_list[int(player_answer) - 1].salary:
                team.add_member(pirates_list[int(player_answer) - 1])
                player.money -= pirates_list[int(player_answer) - 1].salary
                pirates_list.pop(int(player_answer) - 1)
            else:
                print('Денег не хватает, у тебя всего ',
                      player.money, coins(player.money))


def check_attack(island, team):
    """Checking if the team has enough skills.

    Returns a list of Logic, Strength, and Agility
    points differences. Between those that were
    needed and those that actually were.
    """
    l = island[0] - team.logic
    p = island[1] - team.power
    a = island[2] - team.agility
    return [l, p, a]
