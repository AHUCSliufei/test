import cv2
img = cv2.imread('C:/Users/sq/Desktop/pic/052_v_10001.jpg', cv2.IMREAD_UNCHANGED)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('C:/Users/sq/Desktop/pic/052_v_10001_gray.jpg',gray_img)
print("suscess")