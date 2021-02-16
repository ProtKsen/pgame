"""The main functions of interaction with the player."""
from random import randint
from utilities import get_correct_answer, clear, coins
from texts import SEPARATOR, ORACLE_QUESTION_1, ORACLE_QUESTION_2, NAMES
from classes import Pirate


def ask_oracle(player, island):
    """Interaction with the oracle.

    Return a response of the oracle as a string.
    Change the number of player's money.
    """
    if player.money >= 3:
        print(player.inform)
        print(ORACLE_QUESTION_1)
        print(SEPARATOR)
        player_answer = get_correct_answer('1', '2', '3', '4', '5')
    else:
        print(player.inform)
        print(ORACLE_QUESTION_2)
        player_answer = get_correct_answer('1', '2', '3', '4')
    oracle_answer = {
        '2': 'необходимое количество очков логики ' + str(island[0]) + '.',
        '3': 'необходимое количество очков силы ' + str(island[1]) + '.',
        '4': 'необходимое количество очков ловкости ' + str(island[2]) + '.',
        '5': 'необходимое количество очков логики, силы и ловкости ' \
             + str(island[0]) + ', ' + str(island[1]) + ' и ' \
             + str(island[2]) + ' соответственно.'
    }
    cost = {
        '2': 1,
        '3': 1,
        '4': 1,
        '5': 3
    }
    player.money -= cost.get(player_answer, 0)
    return oracle_answer.get(player_answer, '')


def hire_command(player, team, oracle_answer_str, n_island):
    """Hire a team

    Print the list of available pirates.
    Change the number of player's money and
    team's skills in case of hiring."""
    pirates_list = []
    for i in range(7):
        new_pirate = Pirate(NAMES[randint(0, len(NAMES) - 1)],
                            randint(0, n_island + 1), randint(0, n_island + 1),
                            randint(0, n_island + 1), 0)
        skills_sum = new_pirate.logic + new_pirate.power + new_pirate.agility
        new_pirate.salary = randint(max(1, skills_sum - 3), skills_sum + 1)
        pirates_list.append(new_pirate)

    # buy
    exit_from_tavern = False
    while player.money > 0 and exit_from_tavern is False:
        clear()
        print(SEPARATOR)
        print(team.inform)
        print(player.inform)
        print('Ты собираешься плыть на остров ' + str(n_island) + '.', sep='')
        if oracle_answer_str:
            print('Помни, что сказал оракул:\n', oracle_answer_str, sep='')
        print(SEPARATOR)
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
        print(SEPARATOR)
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

    Returns boolean variable.
    """
    l = team.logic - island[0]
    p = team.power - island[1]
    a = team.agility - island[2]
    return min(l, p, a) >= 0
