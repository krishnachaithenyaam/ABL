positive_words = [
    "good", "excellent", "helpful", "clear", "great", "useful"
]

negative_words = [
    "bad", "poor", "boring", "difficult", "unclear", "slow"
]

feedbacks = [
    "The teacher is excellent and helpful",
    "The lecture was boring and slow",
    "The explanation was clear and useful",
    "The subject is difficult",
    "The class was good but the notes were poor"
]

for sentence in feedbacks:
    words = sentence.lower().replace(".", "").replace(",", "").split()

    positive_count = sum(word in positive_words for word in words)
    negative_count = sum(word in negative_words for word in words)

    score = positive_count - negative_count

    if score > 0:
        result = "Positive"
    elif score < 0:
        result = "Negative"
    else:
        result = "Neutral"

    print("\nFeedback:", sentence)
    print("Positive indicators:", positive_count)
    print("Negative indicators:", negative_count)
    print("Sentiment score:", score)
    print("Classification:", result)