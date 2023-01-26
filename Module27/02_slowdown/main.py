import time
from typing import Callable, Any
import functools
def wait(func: Callable) -> Callable:
    """декоратор wait задержки времени вывода сообщения на экран"""
    @functools.wraps(func)
    def timing() -> Any:
        print('Downloding... Wait!')
        time.sleep(2)
        func()
    return timing

@wait
def test() -> str:
    print('Complete!')

test()
