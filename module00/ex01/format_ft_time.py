import time

def print_seconds():
    second: float = time.time_ns() / 10e9


def print_date():
    date: tuple = time.localtime()
    str_date: str = time.strftime("%b %d %Y", date)
    print(str_date)


print_seconds()
print_date()
