import logging
from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор для логирования выполнения функций"""

    # Настройка logging
    if filename:
        (logging.basicConfig(level=logging.INFO, filename=filename, filemode="w", encoding="utf-8"))

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    logging.error(message)
                else:
                    print(message)
                raise

            if filename:
                logging.info(message)
            else:
                print(message)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function_with_log(x: int, y: int) -> int:
    """Функция с записью в файл"""
    return x + y


@log()
def my_function_without_log(x: int, y: int) -> int:
    """Функция без записи в файл"""
    return x + y


if __name__ == "__main__":
    my_function_with_log(1, 2)
    my_function_without_log(3, 2)
