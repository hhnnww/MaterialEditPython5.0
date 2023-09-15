import time


def run_time(func):
    def wrapper(*args, **kwargs):
        st = time.perf_counter()
        res = func(*args, **kwargs)
        print(func.__name__, "运行时间:", time.perf_counter() - st)
        return res

    return wrapper
