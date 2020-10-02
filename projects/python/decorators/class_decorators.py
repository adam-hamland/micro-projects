#Decorator function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper ran extra code before {original_function.__name__} function")
        return original_function(*args, **kwargs)
    return wrapper_function

#Decortator class
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call method ran extra code ran before {self.original_function.__name__} function")
        return self.original_function(*args, **kwargs)

#Functions to decorate
@decorator_function
def display():
    print('display function ran')

@decorator_class
def display_info(name, age):
    print(f'display_info ran with args {name} and {age}')

#Calling decorated functions
display()
print() 
display_info("john", 32)