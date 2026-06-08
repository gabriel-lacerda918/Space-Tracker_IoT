import cv2
from ultralytics import YOLO
import time

KNOWN_WIDTH_CM = 8.56
FOCAL_LENGTH = 700

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("Webcam não encontrada")

start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)

    for result in results:
        for box in result.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            width_px = x2 - x1
            height_px = y2 - y1

            if width_px <= 0:
                continue

            distance_cm = (KNOWN_WIDTH_CM * FOCAL_LENGTH) / width_px

            cls = int(box.cls[0])
            label = model.names[cls]

            risk = "BAIXO"
            if distance_cm < 40:
                risk = "ALTO"
            elif distance_cm < 80:
                risk = "MEDIO"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

            cv2.putText(frame, f"Objeto: {label}", (x1,y1-80),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

            cv2.putText(frame, f"Distancia: {distance_cm:.1f} cm", (x1,y1-55),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

            cv2.putText(frame, f"Largura(px): {width_px}", (x1,y1-30),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

            cv2.putText(frame, f"Risco Colisao: {risk}", (x1,y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)

    fps = 1 / max((time.time() - start_time), 0.0001)
    start_time = time.time()

    cv2.putText(frame, f"FPS: {fps:.1f}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

    cv2.imshow("Space Tracker Monitor Academic", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
