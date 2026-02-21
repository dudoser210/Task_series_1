from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

result = analyzer("I am a priest god never paid")

print(result)