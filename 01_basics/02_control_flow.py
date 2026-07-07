# Loops
# for power in super_powers:
# Format String
# print(f"Power - {power}")

revenues = [20, 40, 12]
expenses = [2, 10, 13]

for i in range(len(revenues)):
    profit = revenues[i] - expenses[i]
    margin = profit * 100 / revenues[i]
    print(f"Margin Q{i + 1}: {margin:.2f}")

margins = []


for i in range(len(revenues)):
    profit = revenues[i] - expenses[i]
    margin = profit * 100 / revenues[i]
    margins.append(margin)

# print(margins)

# Dictionary
fin = {"revenue": 40, "expense": 10}

fin["profit"] = fin["revenue"] - fin["expense"]

financials = [
    {"revenue": 40, "expense": 10},
    {"revenue": 50, "expense": 15},
    {"revenue": 45, "expense": 15},
]

for fin in financials:
    profit = fin["revenue"] - fin["expense"]
    margin = profit * 100 / fin["revenue"]
    # print(f"Margin : {margin}")

# Nested Dictonary
financials = {
    "Q1": {"revenue": 40, "expense": 10},
    "Q2": {"revenue": 50, "expense": 15},
    "Q3": {"revenue": 45, "expense": 15},
}

# for quarter, data in financials.items():
#     print(f"Quarter: {quarter} => {data}")

# Tuples - Immuteable
purple = (128, 0, 5)

print(purple[0])
r, g, b = purple
print(r, g, b)
