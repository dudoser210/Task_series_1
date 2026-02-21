from transformers import pipeline
from PIL import Image

classifier = pipeline("image-classification")

image = Image.open(r"C:\Users\david\OneDrive\Desktop\nuhik\pictures\dog.jpg")

result = classifier(image)

print("Что на картинке?")
for r in result[:3]:
    print(r["label"], r["score"])