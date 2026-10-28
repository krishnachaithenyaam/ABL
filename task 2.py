def electricity_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed_charge = 50
    surcharge = bill * 0.05
    total = bill + fixed_charge + surcharge

    if units < 100:
        total -= 20  # Rebate

    return total

bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    units = int(input(f"Units for month {i + 1}: "))
    bills.append(electricity_bill(units))
    print("Bill:", round(bills[-1], 2))

for i in range(1, n):
    if bills[i] > bills[i - 1] * 1.25:
        print("Unusual increase in month", i + 1)