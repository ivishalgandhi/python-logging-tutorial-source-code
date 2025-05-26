import logging
import functools

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(filename)s:%(lineno)d - %(message)s')

def log(logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            A decorator function that logs debug information when the wrapped function is called
            and logs error information if an exception occurs.

            Args:
                *args: Variable length argument list of the wrapped function
                **kwargs: Arbitrary keyword arguments of the wrapped function
                         # kwargs allows passing key-value pair arguments to the function
                         # Example: function(name="John", age=25)

            Returns:
                The result of the wrapped function execution

            Raises:
                Exception: Re-raises any exception that occurs in the wrapped function
                          after logging the error
            """
            logger.debug(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"An error occurred in {func.__name__}: {str(e)}")
                raise
        return wrapper
    return decorator

# Configure a named logger
logger = logging.getLogger('my_module')
logger.setLevel(logging.DEBUG) # Set the logger to debug level for both debug and error messages

# Create a console handler to output logs to the console

handler = logging.StreamHandler()  # Output to console
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')  # Format with timestamp
handler.setFormatter(formatter)
logger.addHandler(handler)

@log(logger=logger)
def divide(a, b):
    return a / b
try:
    divide(4, 0)
except ZeroDivisionError as e:
    logger.error(f"Caught an exception: {e}")
# This code demonstrates how to use a custom logger with a decorator that logs function calls and errors.