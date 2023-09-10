import cv2
import numpy as np
from yolov7 import Detector

# YOLOv7 모델 초기화
model = Detector(weights='yolov7s.pt', device='cpu')

# 카메라 캡처 초기화
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 의미합니다. 필요에 따라 카메라 인덱스를 변경할 수 있습니다.

while True:
    ret, frame = cap.read()  # 카메라에서 프레임 읽기

    if not ret:
        break

    # YOLOv7로 객체 감지 수행
    detections = model.detect(frame)

    # 감지된 객체를 프레임에 표시
    for detection in detections:
        x, y, w, h, label, confidence = detect
        color = (0, 255, 0)  # 객체 경계 상자 색상 (초록)
        cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), color, 2)
        cv2.putText(frame, f'{label}: {confidence:.2f}', (int(x), int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 화면에 프레임 표시
    cv2.imshow('YOLOv7 Object Detection', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
