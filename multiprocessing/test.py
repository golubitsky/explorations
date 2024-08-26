from multiprocessing import Process
import os


def cpu_bound_task(items):
    [x for x in range(items)]


if __name__ == "__main__":
    processes = [Process(target=cpu_bound_task(10000000)) for _ in range(os.cpu_count())]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
