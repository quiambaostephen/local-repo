def decorator_func(original_func):
    def wrapper_text():
        return original_func()
    return wrapper_text


@decorator_func
def display():
    print('Display function ran')


display()
