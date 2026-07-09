# Multi-Threading
# Handling multiple tasks in paralle

import threading
import time


def calc_square(numbers):
    print("Calculate square of numbers")
    for num in numbers:
        time.sleep(0.2)
        print("square: ", num * num)


def calc_cube(numbers):
    print("Calculate cube of numbers")
    for num in numbers:
        time.sleep(0.2)
        print("cube: ", num * num * num)


arr = [2, 3, 8, 9]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()  # wait until above thread is executed like await in js
t2.join()

print("done task.", time.time() - t)
print("Yohohoho... i am done working")
