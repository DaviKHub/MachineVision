import cv2
import numpy as np

img = cv2.imread('/Users/david/MachineVision/res/pics/1.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('cv', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('hand', cv2.WINDOW_AUTOSIZE)
blure = cv2.GaussianBlur(img,(5,5),2)
cv2.imshow('cv', blure)
n = 9
sigma = 5

kernel = np.zeros((n,n))

a, b = n//2, n//2

for x in range(0,n):
    for y in range(0,n):
        gaus = (1/(2*np.pi*(sigma**2)))*(np.exp(-((x - a)**2 + (y - b)**2) / (2 * sigma**2)))
        kernel[x][y] = gaus
print(kernel)
print("До нормализации: ",kernel.sum())
kernel = kernel / np.sum(kernel)
print("После нормализации: ",kernel.sum())

newImg = np.zeros_like(img)
border = n//2
height, width, ch = img.shape
for ch in range(3):
    for i in range(border, height-border):
        for j in range(border, width-border):
            region = img[i-border:i+border+1, j-border:j+border+1, ch]
            res = np.sum(region*kernel)
            newImg[i][j][ch] = res
cv2.imshow('hand', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()