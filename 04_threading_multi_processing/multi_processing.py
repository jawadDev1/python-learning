# Multi-Processing
# Process creates it's own virtual address, so anything that happens in process remains within it, like variables declare their own scope etc

import multiprocessing
import time

square_result = []


def calc_square(numbers):
    global square_result
    print("Calculate square of numbers")
    for num in numbers:
        time.sleep(0.2)
        square_result.append(num * num)
        print("square: ", num * num)

    print("Within Process Result.", square_result)


def calc_cube(numbers):
    print("Calculate cube of numbers")
    for num in numbers:
        time.sleep(0.2)
        print("cube: ", num * num * num)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    t = time.time()

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print("done task.", time.time() - t)
    print("Result.", square_result)
    print("Yohohoho... i am done working")
