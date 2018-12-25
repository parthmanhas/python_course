import cv2
import os

for file in os.listdir():
	print(file.strip(".jpg"))
	img=cv2.imread(file,1)
	resized_img = cv2.resize(img,(100,100))
	cv2.imwrite(file.strip(".jpg") + "_100x100.jpg",resized_img)
