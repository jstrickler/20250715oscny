from functools import wraps
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="functions.log",
    format="%(levelname)s %(asctime)s %(message)s",
)

def doit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(func.__name__)
        result = func(*args, **kwargs)
        return result
    
    return wrapper

@doit
def spam(x):
    print("SPAM SPAM SPAM")

@doit
def ham(x, y):
    print("ham ham wonderful ham")

# spam = doit(spam)
# ham = doit(ham)
print(f"{spam = }")
print(f"{ham = }")
spam("a")
ham(10, 20)
print(spam.__name__)
print(ham.__name__)