from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


# Каждое число из списка floats возводится в третью степень
# и округляется до трёх знаков после запятой.
floats_result: List[float] = list(map(lambda x: round(x ** 3, 3), floats))
print(floats_result)

# Из списка names берутся только те имена, в которых есть минимум пять букв.
names_result: List[str] = list(filter(lambda x: len(x) >= 5, names))
print(names_result)

# Из списка numbers берётся произведение всех чисел.
def my_add(a: int, b: int) -> int:
    result = a * b
    return result

numbers_result: List[int] = list(map(lambda x: reduce(my_add, numbers), numbers))
print(numbers_result)