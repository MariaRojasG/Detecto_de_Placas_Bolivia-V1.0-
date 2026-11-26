from ultralytics import YOLO
import cv2
import numpy as np
from util import read_license_plate, write_csv
import util

# cargar modelo detector de placas
licence_plate_detector = YOLO('./models/license_plate_detector.pt')

# cargar camara web
cap = cv2.VideoCapture(0)

results = {}
frame_nmr = -1

while cap.isOpened():
    frame_nmr += 1
    ret, frame = cap.read()
    if not ret:
        break

    results[frame_nmr] = {}

    # detectar placas directamente en el frame
    license_plates = licence_plate_detector(frame)[0]
    for plate_idx, license_plate in enumerate(license_plates.boxes.data.tolist()):
        x1, y1, x2, y2, score, class_id = license_plate

        # recorte de placa
        license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]

        # procesamiento de placa
        license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
        _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

        # leer numero de placa
        license_plate_text, license_plate_text_score = util.read_license_plate(license_plate_crop_thresh)

        # dibujar recuadro rojo alrededor de la placa
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

        if license_plate_text is not None:
            # mostrar el texto leido encima de la placa
            cv2.putText(frame, license_plate_text, (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            results[frame_nmr][plate_idx] = {
                'car': {'bbox': [0, 0, 0, 0]},
                'license_plate': {
                    'bbox': [x1, y1, x2, y2],
                    'text': license_plate_text,
                    'bbox_score': score,
                    'text_score': license_plate_text_score
                }
            }

    # mostrar ventana en vivo
    cv2.imshow('Deteccion de placas - Presiona Q para salir', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# escribir resultados en csv
write_csv(results, './test.csv')