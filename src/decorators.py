from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """декоратор со значением по умолчанию None"""

    def decorator(func: Callable) -> Callable:
        """функция-декоратор, принимает в качестве аргумента функцию"""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """декоратор, выполняет функцию из аргумента декоратора - def decorator
            записывает результат работы функции в указанный файл, либо в терминал
            """
            if filename is None:
                try:
                    result = func(*args, **kwargs)
                    return f"{result}\nmy_function ok"
                except Exception as e:
                    return f"my_function error: {e}. Inputs: {args}, {kwargs}"
            else:
                try:
                    func(*args, **kwargs)
                    with open(filename, "a") as file:
                        file.write("my_function ok\n")
                except Exception as e:
                    with open(filename, "a") as file:
                        file.write(f"my_function error: {e}. Inputs: {args}, {kwargs}\n")
                return func(*args, **kwargs)

        return wrapper

    return decorator
