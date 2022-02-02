from datetime import datetime


PATH = 'result.txt'


def log(path):
    def dec (func):
        def fun_file(*args, **kwargs):
            date = datetime.now()
            name = func.__name__
            result = func(*args, **kwargs)
            with open('result.txt', 'w') as file:
                file.write(f'{date}\n'
                       f'{name}\n'
                       f'{args, kwargs}\n'
                       f'{result}\n')
            return result
        return fun_file
    return dec


@log(PATH)
def get_sum(a, b):
    return a+b


if __name__ == '__main__':
    get_sum(5,3)
