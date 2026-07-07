x = input("Enter number 1: ")
y = input("Enter number 2: ")

try:
    z = int(x) / int(y)

except ZeroDivisionError as e:
    print("Can't Divide number by zero: ", e)
    z = None
except Exception as e:
    print("Exception type: ", type(e).__name__)  # find type of error
    z = None
print("Division is : ", z)
