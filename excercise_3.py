"""
Task:
    Create a list of temperatures.
    Loop through them and print:
    "Hot" if temperature is 30 or above.
    "Cold" otherwise.
    Use a lambda function to convert each temperature from Celsius to Fahrenheit.
"""

temps = [22, 35, 18, 30, 27]

for temp in temps:
    if temp > 30:
        print("Hot")
    else:
        print("Cold")

celc_to_fahren = lambda c: c * 1.8 + 32

print(celc_to_fahren(48))
