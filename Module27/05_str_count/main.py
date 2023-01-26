from typing import Callable
import functools

def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f'{func.__name__} была вызвана: {wrapper.count} раз(а)')
        return res

    wrapper.count = 0
    return wrapper


@counter
def test_functions() -> None:
    print('Добрый день!')

@counter
def test_functions2() -> None:
    print('Хорошего дня!')


test_functions()
test_functions2()
test_functions()
test_functions()
test_functions2()
test_functions()

