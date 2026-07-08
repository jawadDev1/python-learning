def remote_control_next():
    yield "HBO"
    yield "CNN"


itr = remote_control_next()

print(itr)  # Generator object
print(next(itr))

for c in remote_control_next():
    print(c)


def fib():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 13:
        break
    print(f)
