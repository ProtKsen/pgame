from random import randint
from interactions import ask_oracle, hire_command, check_attack
from utilities import get_correct_answer, clear, printing, transition
from texts import GREETING, NAME_QUESTION, CHOOSE_LEVEL, INTRODUCTION, \
    ORACLE_QUESTION, SEPARATOR, GO_TAVERN_TEXT, SUCCESS_STEP, FAILURE_STEP, \
    EXIT_QUESTION, WINNING, LOSING

print_in_frame = printing(print)


class Game():
    n_current_island = 1
    current_island = [0, 0, 0]
    oracle_answer_str = ''

    def __init__(self, player, team):
        self.player_name = "Noname"
        self.player = player
        self.team = team

    def greet_player(self):
        print_in_frame(GREETING)

    def ask_name(self):
        print_in_frame(NAME_QUESTION)
        self.player_name = input()

    def choose_difficulty_level(self):
        print_in_frame(CHOOSE_LEVEL)
        level = get_correct_answer('1', '2', '3')
        if level == '1':
            self.level = 4
        elif level == '2':
            self.level = 3
        else:
            self.level = 2

    def print_introduction(self):
        print_in_frame(INTRODUCTION)

    def initialize_islands(self):
        skill_logic = randint(0, self.n_current_island)
        skill_power = randint(0, self.n_current_island - skill_logic)
        skill_agility = self.n_current_island - skill_logic - skill_power
        self.current_island = [
            skill_logic, skill_power,
            skill_agility, self.n_current_island * self.level
        ]

    def ask_about_oracle(self):
        print_in_frame(self.player.inform,
                 'На очереди остров ' + str(self.n_current_island) + '.', sep='\n')
        print_in_frame(ORACLE_QUESTION)
        return get_correct_answer('1', '2')

    def talk_with_oracle(self):
        self.oracle_answer_str = ask_oracle(self.player, self.current_island)
        transition()
        if self.oracle_answer_str:
            print_in_frame('После долгих ритуалов оракул говорит, что ',
                     self.oracle_answer_str, sep='\n')
        transition()

    def action_in_tavern(self):
        print_in_frame(GO_TAVERN_TEXT)
        transition()
        hire_command(self.player, self.team, self.oracle_answer_str, self.n_current_island)

    def try_get_chest(self):
        is_success = check_attack(self.current_island, self.team)
        if is_success:
            self.player.money += self.current_island[3]
            self.n_current_island += 1
            print_in_frame(SUCCESS_STEP, sep='\n')
            transition()
        else:
            print_in_frame(FAILURE_STEP, sep='\n')
            transition()