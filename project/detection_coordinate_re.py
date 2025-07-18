from ultralytics import YOLO
import cv2
import numpy as np

# 신뢰도(confidence) 설정
CONF = 0.80
# 캠 번호 설정
CAM_NUM = 0
# best.pt 모델 파일 경로
MODEL_PATH = "All2_best.pt"

# 극좌표 변환 함수
def convert_to_polar_cm(x, y, center_x, center_y, pixel_to_cm_ratio):
    """중심 좌표 기준으로 극좌표 변환 (센티미터 단위)"""
    dx = x - center_x
    dy = y - center_y
    r = np.sqrt(dx**2 + dy**2) * pixel_to_cm_ratio  # 픽셀을 센티미터로 변환
    theta = np.degrees(np.arctan2(dy, dx))
    theta = theta if theta >= 0 else theta + 360  # 각도를 0~360으로 변환
    return r, theta

# 픽셀-센티미터 비율 계산 함수
def calculate_pixel_to_cm_ratio(pixel_diameter, actual_diameter):
    """픽셀-실제 크기 비율 계산"""
    return actual_diameter / pixel_diameter

# Load YOLO 모델
model = YOLO(MODEL_PATH)

# 카메라 초기화
camera = cv2.VideoCapture(CAM_NUM)

# 샐러드볼 중심 및 지름
salad_bowl_center = None
ACTUAL_BOTTOM_DIAMETER = 7  # 밑바닥 지름 (cm)
ACTUAL_TOP_DIAMETER = 14    # 윤곽선 지름 (cm)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture frame from camera.")
        break

    # 그레이 스케일 및 블러링
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 바이너리 이미지 변환
    _, binary = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

    # 윤곽선 찾기
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    pixel_to_cm_ratio = None
    for contour in contours:
        # 원형 윤곽선 확인
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        if perimeter == 0 or area == 0:
            continue
        circularity = 4 * np.pi * (area / (perimeter**2))
        if 0.7 <= circularity <= 1.3:
            # 샐러드볼 중심 및 크기 계산
            x, y, w, h = cv2.boundingRect(contour)
            center_x, center_y = x + w // 2, y + h // 2
            salad_bowl_center = (center_x, center_y)

            # 픽셀-센티미터 비율 계산
            pixel_to_cm_ratio = calculate_pixel_to_cm_ratio(max(w, h), ACTUAL_TOP_DIAMETER)

            # 윤곽선 및 중심 표시
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            cv2.circle(frame, salad_bowl_center, 5, (0, 0, 255), -1)

    if not salad_bowl_center or not pixel_to_cm_ratio:
        cv2.imshow("Binary Image", binary)
        cv2.imshow("Detections", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    # YOLO 감지 실행
    results = model(frame, imgsz=640, conf=CONF)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            conf = box.conf[0]
            cls = box.cls[0]
            label = model.names[int(cls)]

            # 바운딩 박스 중심 계산
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # 극좌표 변환 (센티미터 단위)
            polar_r, polar_theta = convert_to_polar_cm(center_x, center_y, salad_bowl_center[0], salad_bowl_center[1], pixel_to_cm_ratio)
            print(f"Label: {label}, Polar Coordinates: r={polar_r:.2f} cm, θ={polar_theta:.2f}°")

            # 바운딩 박스 그리기
            color = (0, 0, 255) if label == 'strawberry' else (255, 0, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f'{label}: {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # 중심 좌표 표시
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

    # 샐러드볼 중심이 설정된 경우 밑바닥 영역 표시
    bottom_radius = (ACTUAL_BOTTOM_DIAMETER / 2) / pixel_to_cm_ratio
    cv2.circle(frame, salad_bowl_center, int(bottom_radius), (255, 0, 0), 2)

    # 이미지 출력
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Detections", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
