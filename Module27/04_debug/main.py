from typing import  Callable, Dict
import functools
def debug(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        """Декоратор. Вывод информации о функции"""

        print("Вызывается {}({})".format(
            func.__name__,
            ", ".join(
                list(f"{arg}"
                     if isinstance(arg, str) else
                     repr(arg) for arg in args)
                +
                list(f"{k}={v}\""
                     if isinstance(v, str) else
                     f"{k}={v}" for k, v in kwargs.items())
            )
        ))
        result = func(*args, **kwargs)
        print("'{}' вернула значение'{}'".format(
            func.__name__, result
        ))
        print(result)
        return result
    return wrapper

@debug
def greeting(name: str, age=None) -> str:
    """Вывод обращения к пользователю"""
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)













