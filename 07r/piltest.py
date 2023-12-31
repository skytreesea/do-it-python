from PIL import Image # PIL에서 Image 매서드를 임포트 합니다. 

# 이미지 열기
img = Image.open(r"C:\Users\skytr\Documents\GitHub\do-it-python\07r\test.jpg") # 주소 앞에 r을 붙이세요. 
new_size = (300, 300)
resized_img = img.resize(new_size) # 이미지 사이즈 조정

rotated_img = img.rotate(45)  # 45도 회전

bw_img = img.convert('L')
 
left, upper, right, lower = 100, 100, 400, 400
cropped_img = img.crop((left, upper, right, lower))
cropped_img.show()
img.save('new_image_path.jpg')