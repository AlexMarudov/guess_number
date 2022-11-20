"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def guess_number(number: int = 1) -> int:
    """Угадываем число, используя алгоритм деления пополам диапазона возможных чисел

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_num = 1
    max_num = 101
    while True:
        count += 1
        predict_number = (min_num + max_num)//2
        if number == predict_number:
            break  # выход из цикла если угадали
        if number > predict_number:
            min_num = predict_number # сокращаем диапазон угадываемого числа
        if number < predict_number:
            max_num = predict_number # сокращаем диапазон угадываемого числа
    return count

def score_game(guess_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        guess_number ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(guess_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(guess_number)
