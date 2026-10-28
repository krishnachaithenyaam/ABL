
# Nested List Sports Performance Analysis

# Each row contains a player's scores across five matches
players = [
    ["Arun", 45, 50, 55, 60, 65],
    ["Bala", 60, 55, 60, 55, 60],
    ["Charan", 40, 45, 50, 45, 55],
    ["Deepak", 60, 60, 60, 60, 60]
]

# Ranking rules:
# 1. Highest average score
# 2. If tied, highest score in the latest match
# 3. If still tied, lowest score variation (range)

results = []

print("SPORTS PERFORMANCE ANALYSIS")
print("-" * 60)

for player in players:
    name = player[0]
    scores = player[1:]

    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    score_range = highest - lowest

    # Performance trend
    if scores[-1] > scores[0]:
        trend = "Improving"
    elif scores[-1] < scores[0]:
        trend = "Declining"
    else:
        trend = "Stable"

    results.append([
        name, total, average, scores[-1],
        score_range, trend
    ])

# Display individual performance
for result in results:
    print(f"\nPlayer: {result[0]}")
    print(f"Total Score: {result[1]}")
    print(f"Average Score: {result[2]:.2f}")
    print(f"Latest Match Score: {result[3]}")
    print(f"Score Range: {result[4]}")
    print(f"Performance Trend: {result[5]}")

# Rank players using the supplied tiebreaking rules
ranked = sorted(
    results,
    key=lambda r: (-r[2], -r[3], r[4])
)

print("\n" + "-" * 60)
print("FINAL PLAYER RANKING")
print("-" * 60)

for rank, result in enumerate(ranked, start=1):
    print(
        f"{rank}. {result[0]} - "
        f"Average: {result[2]:.2f}, "
        f"Latest Score: {result[3]}, "
        f"Range: {result[4]}"
    )
