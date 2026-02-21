from transformers import pipeline

speech = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny"
)

result = speech(r"C:\Users\david\OneDrive\Desktop\nuhik\audio\sound.wav")

print("Распознанный текст:")
print(result["text"])
#Модель считает что фраза на корейском)))
