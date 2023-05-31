import cv2
import sys
 
img = cv2.imread('/home/heemin/mv/video/catdog.jpeg')
 
if img is None:
    print('Image load failed')
    sys.exit()

x, y, w, h = cv2.selectROI(img)
# roi = cv2.selectROI(img)
 
roi = img[y:y+h, x:x+w]
color = (0, 255, 0)
thickness = 5
 
cv2.rectangle(img=roi, pt1=(0, 0), pt2=(w, h), color=color, thickness=thickness)
cv2.imshow('image', img)
cv2.waitKey()
cv2.imwrite('result.jpeg', img)
cv2.destroyAllWindows()
