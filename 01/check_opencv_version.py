"""
Чтение, отображение и сохранение изображения в разных форматах
"""
import cv2

I = cv2.imread('img/Birds.jpg')

cv2.namedWindow("Image", 0)
cv2.imshow("Image", I)
cv2.waitKey(0)

cv2.imwrite('img/Birds.png', I)
cv2.destroyAllWindows()
