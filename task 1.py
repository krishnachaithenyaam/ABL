vehicles = []
n = int(input("Enter number of vehicles: "))

distance = float(input("Enter journey distance (km): "))
fuel_price = float(input("Enter fuel price per litre: "))
reserve = float(input("Enter reserve fuel required (litres): "))

for i in range(n):
    print("\nVehicle", i + 1)
    name = input("Vehicle name: ")
    mileage = float(input("Mileage (km/litre): "))
    tank = float(input("Available fuel (litres): "))

    if mileage <= 0 or tank < 0:
        print("Invalid vehicle details")
        continue

    fuel_needed = distance / mileage
    total_fuel = fuel_needed + reserve
    cost = fuel_needed * fuel_price

    print("Fuel required:", round(fuel_needed, 2), "litres")
    print("Fuel including reserve:", round(total_fuel, 2))
    print("Journey cost: Rs.", round(cost, 2))

    if tank >= total_fuel:
        vehicles.append((cost, name))

if vehicles:
    vehicles.sort()
    print("\nLowest-cost feasible vehicle:", vehicles[0][1])
    print("Journey cost: Rs.", round(vehicles[0][0], 2))
else:
    print("\nNo vehicle has sufficient fuel for the journey and reserve.")