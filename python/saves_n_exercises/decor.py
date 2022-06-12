# my_decorator


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("DECORATOOR")
        func(*args, **kwargs)
        print("DECORATOOR")
    return wrapper


@my_decorator
def hello(greeting, ending="magic people"):
    print(f'{greeting} {ending}')


hello("Arse to you,")
