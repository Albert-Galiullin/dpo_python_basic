from functools import wraps
from typing import Callable, Dict, Any

app = {'//': 1}

def callback(route: str) -> Callable:
    """Декоратор функции обратного вызова"""
    def decorator_callback(func: Callable) -> Callable:
        if route in app:
            app[route] = func
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator_callback
@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
