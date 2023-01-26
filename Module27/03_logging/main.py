from typing import  Callable, Dict
from datetime import datetime
import functools


file_in = open("function_errors.log", "w", encoding="utf-8")
def logging(func: Callable) -> Callable:

    """Декоратор. Запись ошибок в файл"""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            print(f'{func.__name__} - {func.__doc__}')
            func()
        except Exception as exc:
            err = (str(datetime.now()) +' При вызове функции {func} ощибка {er} \n'.
                   format(func=func.__name__, er=exc))
            file_in.write(err)
            # return
        # return func
    return wrapped_func

@logging
def cubes_sum(number: int) -> int:
    """Куб числа"""
    result = number ** 3
    return result


@logging
def zero() -> None:
    """Деление на ноль"""
    x = 1 / 0


@logging
def varname() -> None:
    """Присвоение несуществующуй переменной"""
    x = y

@logging
def just() -> None:
    """Присваение переменной значения"""
    x = 25

cubes_sum(25)
zero()
varname()
just()



