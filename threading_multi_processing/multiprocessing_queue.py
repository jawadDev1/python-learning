# Multi-Processing Share data between processes using Queue

import multiprocessing


def calc_square(numbers, q):
    print("Calculate square of numbers")
    global result
    for num in numbers:
        q.put(num * num)
        print("square: ", num * num)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(arr, q))

    p1.start()

    p1.join()

    while q.empty() is False:
        print(q.get())

    print("Yohohoho... i am done working")
