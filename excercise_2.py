"""
Task:
    Create a list of fruits with some duplicates.
    Convert it to a set to remove duplicates.
    Write a function count_fruits(fruits) that returns the number of unique fruits.
"""

fruits = ["Apple", "Banana", "Apple", "Orange", "Banana"]

unique_fruits = set(fruits)

print(unique_fruits)

for fruit in unique_fruits:
    print(f"Fruit : {fruit}")


def count_fruits(fruits):
    count = 0
    unique_fruits = set(fruits)
    for _ in unique_fruits:
        count += 1
    return count


print(count_fruits(fruits))
print(len(unique_fruits))
