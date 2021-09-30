import multiprocessing
import os


def worker1():
    print('ID process runnig worker1: {}'.format(os.getpid()))


def worker2():
    print('ID process runnig worker2: {}'.format(os.getpid()))


if __name__ == '__main__':
    print('ID process runnig main: {}'.format(os.getpid()))

    p1 = multiprocessing.Process(target=worker1())
    p2 = multiprocessing.Process(target=worker2())

    p1.start()
    p2.start()

    print('ID of process p1: {}'.format(p1.pid))
    print('ID of process p2: {}'.format(p2.pid))

    p1.join()
    p2.join()

    print('Both processes have finished!')

    print('Process p1 is alive {}'.format(p1.is_alive()))
    print('Process p2 is alive {}'.format(p2.is_alive()))
