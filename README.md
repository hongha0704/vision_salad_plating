🥗 비전 기술을 활용한 샐러드 사용자 커스텀 플레이팅
===
&nbsp;

### 📷 작업공간
<img src="https://github.com/user-attachments/assets/d49039c5-8c1e-432e-844c-f7061b0cb455" width="50%" height="50%" title="px(픽셀) 크기 설정" alt="project_workspace"><img src="https://github.com/user-attachments/assets/e30fb8ba-2b58-49fa-8919-c3172bdef0e1" width="50%" height="50%" title="px(픽셀) 크기 설정" alt="project_workspace"></img>   
&nbsp;

### 📷 시연 영상
https://youtu.be/NBL9EKFYKEo

---

&nbsp;

## 목차

#### [1. 📘 프로젝트 개요](#1--프로젝트-개요-1)   
#### [2. 👥 프로젝트 팀 구성 및 역할분담](#2--프로젝트-팀-구성-및-역할분담-1)   
#### [3. 🗓 프로젝트 구현 일정](#3--프로젝트-구현-일정-1)   
#### [4. 📌 SKILLS](#4--skills-1)   
#### [5. 🤖 Hardware](#5--hardware-1)   
#### [6. 🎬 System Flow](#6--system-flow-1)   
#### [7. 🔍 프로젝트 기대효과](#7--프로젝트-기대효과-1)   

---

&nbsp;

## 1. 📘 프로젝트 개요
기사를 통해 최근에는 사람들이 요리를 단순히 맛으로만 즐기는 것이 아니라, 예쁘게 플레이팅하고 이를 공유하는 라이프스타일이 자리 잡고 있음을 확인하였습니다.   
이러한 흐름 속에서 단순히 예쁘게 완성된 음식을 제공하는 것을 넘어, 사용자가 직접 플레이팅을 결정할 수 있는 시스템을 도입하면 어떨까 하는 아이디어에서 이번 프로젝트를 기획하게 되었습니다.   

### **문제해결 전략**
1. 손님이 샐러드 가게에 들어오면 키오스크를 통해 원하는 토핑을 선택합니다. 이는 기업체의 필요에 따라 토핑의 종류와 갯수는 추가 및 수정이 가능합니다.
2. 사용자가 원하는 토핑을 선택하고 나면, 선택한 토핑의 위치를 사용자가 키오스크상에서 직접 드래그 앤 드롭하여 결정할 수 있습니다.   
3. 사용자가 선택한 토핑의 위치와 실제 샐러드 토핑이 토출된 위치와 같은지 실시간으로 검수하고, 같다면 same이라는 문구가 출력되고 다르다면 not same이라는 문구가 출력됩니다. 만약 not same이라는 문구가 뜨면 이에 따른 조정이 가능합니다.   

&nbsp;

## 2. 👥 프로젝트 팀 구성 및 역할분담
|이름|담당 업무|
|--|--|
|김솔비(팀장)| 키오스크 개발, 키오스크와 카메라 통신, 물체의 좌표 확인 및 오차 비교 |
|권빈| YOLO 커스텀 데이터셋 제작 및 학습, 과일 분류 및 좌표 출력 알고리즘 개발 |
|강순혁| 샐러드볼 설계 및 제작, 검수 환경 하드웨어 제작, 물체의 좌표 확인 및 오차 비교 |
|백홍하| YOLO 커스텀 데이터셋 제작 및 학습, 과일 분류 및 좌표 출력 알고리즘 개발 |

&nbsp;

<img src="https://github.com/user-attachments/assets/ad44d7fb-b894-46e0-81ac-3cb1ea63d847" width="75%" height="75%" title="px(픽셀) 크기 설정" alt="역할분담"></img>

&nbsp;

## 3. 🗓 프로젝트 구현 일정
**진행 일자: 24.11.10(일) ~ 24.12.16(화) (5주)**
<img src="https://github.com/user-attachments/assets/e15ce93b-f5cb-41ae-ae57-0ef69336322b" width="75%" height="75%" title="px(픽셀) 크기 설정" alt="project_management"></img>
<img src="https://github.com/user-attachments/assets/42c0a623-232a-4565-aba9-0dfd90c001be" width="75%" height="75%" title="px(픽셀) 크기 설정" alt="project_management"></img>

&nbsp;

## 4. 📌 SKILLS
### **Development Environment**
<div align=left>
  
  ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
</div>

[![My Skills](https://skillicons.dev/icons?i=vscode&theme=light)](https://skillicons.dev)

### **Programming Languages**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   
[![My Skills](https://skillicons.dev/icons?i=python&theme=light)](https://skillicons.dev)   

### **GUI**
![Swift](https://img.shields.io/badge/swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white)   
[![My Skills](https://skillicons.dev/icons?i=swift&theme=light)](https://skillicons.dev)   

### **AI & Computer Vision**
<div align=left>
  
  ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
  ![YOLO](https://img.shields.io/badge/YOLO-111F68?style=for-the-badge&logo=YOLO&logoColor=white)
</div>

[![My Skills](https://skillicons.dev/icons?i=opencv,yolo&theme=light)](https://skillicons.dev)   

### **Network**
![Socket](https://img.shields.io/badge/Socket-C93CD7?style=for-the-badge&logo=Socket&logoColor=white)   

&nbsp;

## 5. 🤖 Hardware
### **Vision Camera**
- Intel RealSense D435i

&nbsp;

## 6. 🎬 System Flow
1. 키오스크에서 샐러드 토핑을 선택
2. 키오스크에서 샐러드 토핑 위치 설정
3. 카메라 화면에서 YOLO를 활용하여 실제 샐러드 토핑을 detection 하고, bounding box의 중심점 좌표 반환
4. 최종적으로 socket 통신을 사용하여 실제 샐러드 토핑의 위치와 사용자가 선택한 샐러드 토핑 위치와 동일한지 확인

&nbsp;

## 7. 🔍 프로젝트 기대효과
### **기대 효과**
- 고객의 재방문율 증가 및 SNS를 통한 홍보 효과
- 실시간 식재료 소진율 및 식재료 별 재고 소진 예측 가능
- 고객 참여와 재미 및 개인화 된 경험 제공

&nbsp;
