import multiprocessing


result = []


def square_list(number_list):
    global result

    for num in number_list:
        result.append(num * num)

    print('Result in process p1): {}'.format(result))


if __name__ == '__main__':
    number_list = [1, 2, 3, 4]

    p1 = multiprocessing.Process(target=square_list, args=(number_list,))

    p1.start()

    p1.join()

    print('Result in main process): {}'.format(result))