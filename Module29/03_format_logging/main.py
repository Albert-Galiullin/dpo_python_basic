import time
from datetime import datetime

def timer(cls, func, date_format):
    def wrapped(*args, **kwargs):
        format_str = date_format
        for symbol in format_str:
            if symbol.isalpha():
                format_str = format_str.replace(symbol, '%' + symbol)
        print(f" Запускается '{cls.__name__}.{func.__name__}'. "
              f"Дата и время запуска: {datetime.now().strftime(format_str)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f" Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
        return result

    return wrapped


def log_methods(date_format):
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# Урок 29.4
# import functools
# from datetime import datetime
# import time
# from typing import Callable
#
# def createtime(cls):
#     """Декоратор класса.Выводит время создания инстанса класса"""
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         insance = cls(*args, **kwargs)
#         print('Время создания инстанса класса:', datetime.utcnow())
#         return insance
#     return wrapper
#
#
# def timer(func: Callable) -> Callable:
#      """Декоратор, выводящий время функции или метода"""
#      @functools.wraps(func)
#      def wrapped(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print('Время работы функции: ', end - start)
#         return result
#      return wrapped
#
# # для того, чтобы не прописывать таймер в каждом методе (нужен для класса,
# # а там он неправильно считает), создадим отдельную функци.
# def for_all_methods(decorator: Callable) ->Callable:
#     """
#     Декоратор класса.
#     получает другой декоратор и
#     применяет его ко всем методам класса
#     """
#     def decorate(cls):
#         # print(dir(cls))
#         for i_method_name in dir(cls):
#             if i_method_name.startswith('__') is False:
#                 cur_method = getattr(cls, i_method_name)
#                 decorated_method = decorator(cur_method)
#                 setattr(cls, i_method_name, decorated_method)
#         return cls
#     return decorate
#
#
#
# @createtime
# @for_all_methods(timer)
# class Functions:
#     def __init__(self, max_num: int) -> None:
#         self.max_num = max_num
#
#     # @timer
#     def squares_sum(self) ->int:
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(self.max_num)])
#         return result
#
#     # @timer
#     def cubes_sum(self, number: int) -> int:
#         result = 0
#         for _ in range(number):
#             result += sum([i_num ** 3 for i_num in range(self.max_num)])
#         return result
#
# my_func_1 = Functions(max_num= 1000)
# # time.sleep(1)
# # my_func_2 = Functions(max_num= 2000)
# # time.sleep(1)
# # my_func_3 = Functions(max_num= 3000)
# my_func_1.squares_sum()
# my_func_1.cubes_sum(number=2000)
#
#
# # result = 0
# # for _ in range(5):
# #     result += sum([i_num ** 3 for i_num in range(6)])
# #     print(result)
# #
# # a = [i_num ** 3 for i_num in range(6)]
# # print(a)