from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love building AI systems!")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")

# NLP experiment for sentiment classification research