import os

# 이미지 파일이 있는 폴더 경로
image_folder = 'yolov7/dataset/makeSense'  # 학습 데이터 폴더 경로

# 이미지 파일 확장자 (예: jpg, png 등)
image_extension = ['.jpg', '.jpeg',]  # 이미지 파일 확장자

# 이미지 파일 경로를 저장할 txt 파일 이름
output_train_txt = 'train.txt'  # 학습 데이터용 txt 파일
output_val_txt = 'val.txt'      # 검증 데이터용 txt 파일

# 이미지 파일 목록을 저장할 리스트
train_image_list = []
val_image_list = []

# 폴더 내의 이미지 파일을 탐색하고 목록에 추가
for root, _, files in os.walk(image_folder):
    for file in files:
        if any(file.endswith(ext) for ext in image_extension):
            # 이미지 파일 경로를 생성
            image_path = os.path.join(root, file)
            
            # 여기에서 학습 및 검증 데이터셋을 어떻게 구분할지에 따라서 목록을 분리
            # 예를 들어, 홀수 번째 이미지는 학습 데이터셋으로, 짝수 번째 이미지는 검증 데이터셋으로 설정
            if int(file.split('.')[0][-1]) % 2 == 0:
                val_image_list.append(image_path)
            else:
                train_image_list.append(image_path)

# 이미지 파일 목록을 txt 파일에 쓰기
with open(output_train_txt, 'w') as train_txt:
    train_txt.write('\n'.join(train_image_list))

with open(output_val_txt, 'w') as val_txt:
    val_txt.write('\n'.join(val_image_list))
