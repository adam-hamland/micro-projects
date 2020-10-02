#Examples on how to use decorators

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args: {args}, and kwargs: {kwargs}'
        )
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__}() ran in: {round(t2,2)} seconds')
        return result

    return wrapper


#Functions to decorate
# @my_logger
# def display():
#     print('display function ran')

@my_timer
@my_logger
def display_info(name, age):
    print(f'display_info ran with args {name} {age}')

#Calling decorated functions
# display()
print() 
display_info("john", 32)