import logging
import functools

# Configure logging with filename and line number
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(filename)s:%(lineno)d - %(message)s')

# Decorator to log errors with function name and module
def log_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred in function {func.__name__} in module {func.__module__} : {repr(e)}") #repr(e) gives a detailed representation of the exception
            raise  # Without this, exceptions would be silently caught
    return wrapper  # Without this, the decorator wouldn't work

# Example showing why raise is important
@log_error
def divide(a, b):
    return a / b

try:
    result = divide(10, 0)  # This raises ZeroDivisionError
except ZeroDivisionError as e:
    # Without raise, this except block would never execute
    logging.error(f"Caught exception: {e}")