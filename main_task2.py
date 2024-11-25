import re
from typing import Callable


# Функція яка повертає генератор, що ітерує по всіх дійсних числах у тексті.
def generator_numbers(text: str):
    for digit in re.findall(r'\d+\.\d+', text):
        try:
            yield float(digit)
        except ValueError:
            continue


# Функція для обчислення загальної суми чисел у вхідному рядку
def sum_profit(text: str, func: Callable):
    sum_digits = 0
    for digit in generator_numbers(text):
        sum_digits += digit
    return sum_digits


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
