### 마우스로 클릭하면 클릭한 값의 극좌표 뜨게 하는 코드

import cv2
import numpy as np
import math

# 원형 감지 함수
def is_circle(contour, tolerance=0.3):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        return False
    circularity = 4 * np.pi * (area / (perimeter ** 2))
    return 1 - tolerance <= circularity <= 1 + tolerance

# 토핑 좌표 저장
toppings = []

def add_topping(event, x, y, flags, param):
    """마우스 클릭으로 토핑 추가"""
    global salad_bowl_center
    if event == cv2.EVENT_LBUTTONDOWN and salad_bowl_center:
        dx = x - salad_bowl_center[0]
        dy = y - salad_bowl_center[1]
        r = math.sqrt(dx ** 2 + dy ** 2)  # 반지름 계산
        theta = math.degrees(math.atan2(dy, dx))  # 각도 계산
        theta = theta if theta >= 0 else 360 + theta  # 각도를 0~360으로 정규화

        toppings.append({'position': (x, y), 'polar': (r, theta)})
        print(f"Topping added at: Cartesian=({x}, {y}), Polar=(r={int(r)}, theta={int(theta)}°)")

# 샐러드볼 중심 좌표
salad_bowl_center = None

camera = cv2.VideoCapture(2)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # 그레이 스케일과 블러링 처리
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 바이너리 이미지 생성
    _, binary = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

    # 컨투어 찾기
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 샐러드 볼 중심 찾기
    for contour in contours:
        if is_circle(contour):
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])  # 중심 X
                cY = int(M["m01"] / M["m00"])  # 중심 Y
                salad_bowl_center = (cX, cY)  # 샐러드볼 중심 저장

                # 중심에 "Salad Bowl" 텍스트 표시
                cv2.putText(frame, "Salad Bowl", (cX - 50, cY - 220), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

                # 샐러드볼 윤곽선 그리기
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cX, cY), 5, (0, 255, 0), -1)

    # 추가된 토핑 표시
    for topping in toppings:
        # 토핑 위치 표시
        cv2.circle(frame, topping['position'], 8, (255, 0, 0), -1)
        cv2.putText(frame, f"r={int(topping['polar'][0])}, theta={int(topping['polar'][1])}°", 
                    (topping['position'][0] + 10, topping['position'][1] + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)

    # 출력
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Salad Bowl", frame)

    # 마우스 콜백 설정
    cv2.setMouseCallback("Salad Bowl", add_topping)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
