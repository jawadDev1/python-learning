# Multi-Processing Share values between processes
# use Shared Memory to share the data

import multiprocessing


def calc_square(numbers, result, v):
    v.value = 88.9999
    print("Calculate square of numbers")
    for idx, num in enumerate(numbers):
        result[idx] = num * num
        print("square: ", num * num)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    result = multiprocessing.Array(
        "i", 4
    )  # i -> data type (integer), 4 -> length of list
    v = multiprocessing.Value("d", 4.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result, v))

    p1.start()

    p1.join()

    print("Result.", result[:], v.value)
    print("Yohohoho... i am done working")
