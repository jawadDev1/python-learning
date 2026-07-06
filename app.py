temps = [22, 35, 18, 30, 27]

for temp in temps:
    if temp > 30:
        print("Hot")
    else:
        print("Cold")

celc_to_fahren = lambda c: c * 1.8 + 32

print(celc_to_fahren(48))
