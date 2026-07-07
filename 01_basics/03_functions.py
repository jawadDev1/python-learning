# type hint
def calc_margin(revenue: float, expense: float) -> float:
    profit = revenue - expense

    return profit * 100 / revenue


print(calc_margin(50, 10))


# returns tuple
def calc_profit_margin(revenue, expense):
    profit = revenue - expense

    margin = profit * 100 / revenue
    return profit, margin


profit, margin = calc_profit_margin(49, 22)

print(profit, margin)


# Args, accept multiple Arguments
def calc_total_expenses(*args):
    return sum(args)


calc_total_expenses(1, 2, 59, 24)


# Names Arguments
def total_expenses(rent, phone_bill):
    return rent + phone_bill


print(total_expenses(rent=120, phone_bill=5))


# **kargs -> dict
def total_nothing(**kargs):
    print(kargs)
    total = 0
    for key, value in kargs.items():
        total += value

    return total


print(total_nothing(rent=12, phone_billl=1))

# Lambda function
square = lambda x: x**2

print(square(2))
