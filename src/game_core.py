import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1, 101)

    # Используем два указателя, чтобы запереть искомое значение в некотором интервале.
    # На каждой итерации интервал будет уменьшаться.
    left, right = 1, 100

    while number != predict:
        count += 1
        # Шаг изменения, для нечетных чисел не забудем прибавить единицу,
        # т.к. используем операцию целочисленного деления
        step = (right - left) // 2 + (right - left) % 2
        if number > predict:
            # Чтобы не выйти за рамки интервала возьмём
            # минимальное значение между верхней границей интервала и шагом
            predict = min(predict + step, 100)
            # Обновляем границы интервала после пересчёта значения
            if number > predict:
                left = max(left, predict)
            else:
                right = predict
        elif number < predict:
            # Чтобы не выйти за рамки интервала возьмём
            # максимальное значение между нижней границей интервала и шагом
            predict = max(predict - step, 1)
            # Обновляем границы интервала после пересчёта значения
            if number < predict:
                right = min(predict, right)
            else:
                left = predict

    # Ваш код заканчивается здесь
    return count
