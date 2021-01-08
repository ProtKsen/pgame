"""All used classes."""
from add_functions import coins


class Player:
    """Player, the one attribute - money."""
    def __init__(self, money=0):
        self.money = money

    @property
    def inform(self):
        """Printing the information about player's money"""
        return 'У тебя ' + str(self.money) + coins(self.money)


class Team:
    """Pirate team, attributes are points of skills."""
    def __init__(self):
        self.logic = 0
        self.power = 0
        self.agility = 0

    def add_member(self, pirate):
        """Adding new pirate to team.

         Changing skill points.
         """
        self.logic += pirate.logic
        self.power += pirate.power
        self.agility += pirate.agility

    def reset_command(self):
        """Setting all skill points to zero."""
        self.logic = 0
        self.power = 0
        self.agility = 0

    @property
    def inform(self):
        """Printing the information about team's skill points."""
        return 'Очки твоей команды: логика - ' + str(self.logic) + ', сила - ' +\
               str(self.power) + ', ловкость - ' + str(self.agility) + '.'


class Pirate:
    """A pirate who can be hired on a ship."""
    def __init__(self, name, logic, power, agility, salary):
        self.name = name
        self.logic = logic
        self.power = power
        self.agility = agility
        self.salary = salary
