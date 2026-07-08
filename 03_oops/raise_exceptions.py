# try:
#     raise MemoryError("memory error")
# except MemoryError as e:
#     print(e)

# General Exception
# try:
#     raise Exception("memory error")
# except Exception as e:
#     print(e)


# user define exception
class Accident(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

    def print_exception(self):
        print("user define exception: ", self.msg)


try:
    raise Accident("crashed with a truck")
except Accident as e:
    e.print_exception()
