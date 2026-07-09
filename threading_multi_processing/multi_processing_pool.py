# Multi-Processing Pool
# divide task between multiple cores.
# Map -> divide the task, Reduce -> get the result from cores and aggreagate it into 1 result;

from multiprocessing import Pool


def f(n):
    return n * n


if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    # p = Pool()
    p = Pool(processes=3)
    result = p.map(f, arr)

    p.close()
    p.join()
    # for n in arr:
    #     result.append(f(n))

    print(result)
