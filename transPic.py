import numpy as np
import glob
import cv2
path = glob.glob("C:\\pic\\*.jpg")
cv_img = []
file_res=[]
img_rotate=[]
i=0

print(path)
for img in path:
    n = cv2.imread(img)
    cv_img.append(n)

for trans in cv_img:
    dst = cv2.resize(trans, dsize=(600, 400), interpolation=cv2.INTER_AREA)

    #dst = cv2.rotate(dst, cv2.ROTATE_90_CLOCKWISE) #시계방향90도 회전
    #dst = cv2.rotate(dst, cv2.ROTATE_180) #180도 회전
    #dst = cv2.rotate(dst, cv2.ROTATE_90_COUNTERCLOCKWISE) #시계방향270도회전

    #dst = cv2.flip(dst, 1) #좌우반전
    #dst = cv2.flip(dst, 0) #상하반전

    #dst = trans[0:200, 0:500].copy() #이미지 자르기

    file_res.append(dst)

    while i < len(file_res):
        cv2.imwrite('C:\\pic\\output\\'+str(i+1)+'.jpg',file_res[i])
        i=i+1
