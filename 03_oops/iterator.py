a = ["Ore", "no", "nawa", "Monkey D. Luffy"]

# itr = iter(a)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

itr = reversed(a)

print(next(itr))


class RemoteControl:
    def __init__(self) -> None:
        self.channels = ["HBO", "CNN", "BBC"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]


r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
