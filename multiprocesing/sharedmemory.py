import multiprocessing


def square_list(number_list, result, square_sum):
    for idx, num in enumerate(number_list):
        result[idx] = num * num

    square_sum.value = sum(result)

    print ('Result in process p1 {}'.format(result[:]))

    print('Sum of squares in process p1 {}'.format(square_sum.value))


if __name__ == '__main__':
    number_list = [1, 2, 3, 4]

    result = multiprocessing.Array('i', 4)

    square_sum = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=square_list, args=(number_list, result, square_sum,))

    p1.start()

    p1.join()

    print('Result in main program: {}'.format(result[:]))

    print ('Sum of squares in main program {}'.format(square_sum.value))
