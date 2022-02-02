from datetime import datetime
import hashlib

PATH='Test.txt'

def log(func):
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

@log
def hash(path: str):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()

print(hash(PATH))
