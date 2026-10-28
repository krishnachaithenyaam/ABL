wards = {
    "General Ward": [35, 40, 42, 38, 45],
    "ICU": [8, 9, 10, 12, 11],
    "Pediatric Ward": [15, 18, 16, 20, 19]
}

capacity = {
    "General Ward": 40,
    "ICU": 10,
    "Pediatric Ward": 18
}

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday"]

peak_occupancy = -1
peak_ward = ""
peak_day = ""

for ward, occupancy in wards.items():
    print("\nWard:", ward)

    for i, beds in enumerate(occupancy):
        utilization = beds / capacity[ward] * 100

        print(days[i],
              "- Occupied:", beds,
              "- Utilization:", round(utilization, 2), "%")

        if beds > capacity[ward]:
            print("WARNING: Capacity exceeded!")

        if beds > peak_occupancy:
            peak_occupancy = beds
            peak_ward = ward
            peak_day = days[i]

print("\n--- Peak Demand Report ---")
print("Ward:", peak_ward)
print("Day:", peak_day)
print("Occupied beds:", peak_occupancy)
print("Capacity:", capacity[peak_ward])
print("Utilization:",
      round(peak_occupancy / capacity[peak_ward] * 100, 2), "%")