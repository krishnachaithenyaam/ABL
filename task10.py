
# Multi-Day Bus Route Performance Analysis

# Record format:
# [Route, Day, Passengers, Capacity, Journey_Time_Hours, Fuel_Litres]

bus_data = [
    ["Route A", "Monday",    48, 50, 2.0, 12],
    ["Route A", "Tuesday",   55, 50, 2.2, 14],
    ["Route A", "Wednesday", 45, 50, 1.8, 11],
    ["Route B", "Monday",    35, 40, 1.5, 8],
    ["Route B", "Tuesday",   38, 40, 1.6, 9],
    ["Route B", "Wednesday", 30, 40, 1.4, 7],
    ["Route C", "Monday",    60, 60, 2.5, 16],
    ["Route C", "Tuesday",   65, 60, 2.8, 18],
    ["Route C", "Wednesday", 58, 60, 2.4, 15]
]

routes = {}

# Group records by route
for record in bus_data:
    route, day, passengers, capacity, time, fuel = record

    if route not in routes:
        routes[route] = {
            "passengers": 0,
            "capacity": 0,
            "time": 0,
            "fuel": 0,
            "days": 0,
            "overloaded_days": []
        }

    info = routes[route]
    info["passengers"] += passengers
    info["capacity"] += capacity
    info["time"] += time
    info["fuel"] += fuel
    info["days"] += 1

    if passengers > capacity:
        info["overloaded_days"].append(day)

# Calculate and display route performance
results = []

print("MULTI-DAY BUS ROUTE PERFORMANCE")
print("=" * 65)

for route, info in routes.items():
    days = info["days"]
    total_passengers = info["passengers"]
    total_capacity = info["capacity"]
    total_time = info["time"]
    total_fuel = info["fuel"]

    average_passengers = total_passengers / days
    average_time = total_time / days

    # Passenger capacity utilisation percentage
    utilisation = (total_passengers / total_capacity) * 100

    # Fuel efficiency: passenger journeys per litre
    efficiency = total_passengers / total_fuel

    print(f"\nRoute: {route}")
    print("Total Passengers:", total_passengers)
    print(f"Average Passengers per Day: {average_passengers:.2f}")
    print(f"Average Journey Time: {average_time:.2f} hours")
    print("Total Fuel Used:", total_fuel, "litres")
    print(f"Capacity Utilisation: {utilisation:.2f}%")
    print(f"Operating Efficiency: {efficiency:.2f} passenger/litre")

    if info["overloaded_days"]:
        print("Overloaded Days:", ", ".join(info["overloaded_days"]))
    else:
        print("Overloaded Days: None")

    results.append(
        (route, efficiency, utilisation, average_time)
    )

# Rank routes by fuel efficiency
ranked = sorted(results, key=lambda x: x[1], reverse=True)

print("\n" + "=" * 65)
print("ROUTE EFFICIENCY RANKING")
for rank, result in enumerate(ranked, start=1):
    print(f"{rank}. {result[0]} - {result[1]:.2f} passengers/litre")

# Identify the route with the highest fuel efficiency
best_route = ranked[0]
print("\nMost Fuel-Efficient Route:", best_route[0])
