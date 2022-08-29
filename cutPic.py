
import glob
import cv2
path = glob.glob("C:\\pic\\*.png")
cv_img = []
file_res=[]
img_rotate=[]
i=0

for img in path:
    n = cv2.imread(img)
    cv_img.append(n)

for trans in cv_img:
    dst = trans[0:200, 0:500].copy()

    file_res.append(dst)

    while i < len(file_res):
        cv2.imwrite('C:\\pic\\output\\'+str(i+1)+'.png',file_res[i])
        i=i+1
