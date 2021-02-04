"""Some additional functions."""
import os
from texts import SEPARATOR, CONT_GAME


def clear():
    """Cleaning console."""
    return os.system('cls' if os.name == 'nt' else 'clear')


def printing(f_print):
    """Changing the standard print function."""
    def inner(*args, **kwargs):
        """Printing text in the separator's frame."""
        print(SEPARATOR)
        f_print(*args, **kwargs)
        print(SEPARATOR)
    return inner


def transition():
    """Transition to the next window."""
    input(CONT_GAME)
    clear()


def get_correct_answer(*answers):
    """Checking the correctness of the answer.

    Checking if the user's response is
    included in the set of available responses.
    """
    while 1:
        answer = input()
        if answer in answers:
            return answer
        print('Попробуй еще раз, в ответе нужно указать '
              'номер выбранного тобой варианта ответа.')


def coins(n):
    """Printing the correct form of the word."""
    base = ' монет'
    end = ''
    if n % 100 not in [11, 12, 13, 14]:
        if n % 10 == 1:
            end = 'a'
        elif 2 <= n % 10 <= 4:
            end = 'ы'
    return base + end
