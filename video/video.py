import cv2
from transformers import pipeline
from PIL import Image

detector = pipeline("object-detection")

cap = cv2.VideoCapture(0)

running = False

print("Нажми S — Start")
print("Нажми P — Stop")
print("Нажми Q — Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        running = True
        print("Start")

    if key == ord("p"):
        running = False
        print("Stop")

    if key == ord("q"):
        print("Exit")
        break

    if running:
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        results = detector(image)

        for obj in results:
            if obj["score"] < 0.5:
                continue

            box = obj["box"]
            label = obj["label"]

            x1, y1 = int(box["xmin"]), int(box["ymin"])
            x2, y2 = int(box["xmax"]), int(box["ymax"])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    cv2.imshow("Object Detection (S-Start / P-Stop)", frame)

cap.release()
cv2.destroyAllWindows()
#Горячие клавиши: Q-закрыть, S-запустить определение, P-приостановить определение