"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import math


def random_predict(number: int = 1) -> int:
    count = 0
    predict_number = 50
    
    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            predict_number += math.ceil(100/(2**(count+1)))
        else:
            predict_number -= math.ceil(100/(2**(count+1)))
    return count


def score_game(random_predict) -> int:
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)