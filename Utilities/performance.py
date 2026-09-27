import time


def measure_execution_time(function, *args):
    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return result, execution_time