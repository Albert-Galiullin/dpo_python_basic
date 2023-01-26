from typing import Callable, Any
import functools

def how_are_you(func: Callable) -> Callable:
    """декоратор how_are_you, который запускает троль"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        с = input('Как дела? ')
        print('А у меня не очень. Ладно, держи свою функцию')
        func(*args, **kwargs)

    return wrapped_func


@how_are_you
def test() -> str:
    print('<Тут что-то происходит...>')

test()
