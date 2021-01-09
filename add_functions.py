"""Some additional functions."""
import os
from texts import separator, cont_game


def clear():
    """Cleaning console."""
    return os.system('cls' if os.name == 'nt' else 'clear')


def printing(f_print):
    """Changing the standard print function."""
    def inner(*args, **kwargs):
        """Printing text in the separator's frame."""
        print(separator)
        f_print(*args, **kwargs)
        print(separator)
    return inner


def transition():
    """Transition to the next window."""
    input(cont_game)
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
    d = n % 10
    if d == 0 or 5 <= d <= 10 or 11 <= n % 100 <= 14:
        end = ''
    elif d == 1:
        end = 'a'
    elif 2 <= d <= 4 or 12 <= d <= 14:
        end = 'ы'
    return base + end
