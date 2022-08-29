import numpy as np
import glob
import cv2
path = glob.glob("C:\\test\\*.png")
cv_img = []
for img in path:
    n = cv2.imread(img)
    cv_img.append(n)

#src = cv2.imread("C:\\test\\img.png", cv2.IMREAD_COLOR)
for trans in cv_img:
    dst = cv2.resize(cv_img, dsize=(300, 200), interpolation=cv2.INTER_AREA)
#dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

#cv2.imshow("src", src)
#cv2.imshow("dst", dst)
#cv2.imshow("dst2", dst2)
#cv2.waitKey()
#cv2.destroyAllWindows()

cv2.imwrite("C:\\test\\img22.png",dst)
