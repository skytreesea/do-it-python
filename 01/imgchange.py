from PIL import Image
import os

# 이미지 파일이 저장된 경로
path = r"C:\Users\skytr\OneDrive\문서\김창현\책\파이썬 생활프로그래밍\imgtest"

# 변경할 크기
new_size = (300, 200)

# 이미지 파일 경로 내 모든 파일에 대해 반복
for filename in os.listdir(path):
    if filename.endswith('.jpg'):  # jpg 파일만 처리
        # 이미지 파일 열기
        with Image.open(os.path.join(path, filename)) as img:
            # 이미지 크기 변경
            img = img.resize(new_size)
            # 변경된 이미지 저장
            img.save(os.path.join(path, "new_" + filename))