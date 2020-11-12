import inspect
from time import time, sleep


class WaitError(Exception):
    def __init__(self, func):
        self.func = func

    def __str__(self):
        return repr(f'[ERROR] failed to wait {self.func}')


def wait(condition, timeout, silent=False):
    flag = False
    start = time()
    while time() - start <= timeout:
        try:
            if condition():
                flag = True
                break
        except Exception:
            pass
        sleep(1)
    if flag is False and silent is False:
        raise WaitError(inspect.getsource(condition).strip())
