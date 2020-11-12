from time import process_time


class PerfManager:

    @staticmethod
    def time_measure(input_fun, *args, **kwargs):
        start_time = process_time()
        input_fun(*args, **kwargs)
        return int(process_time() - start_time)
