import cv2
import matplotlib.pyplot as plt

# Hiển thị ảnh trên lưới 
fig, axs = plt.subplots(2, 3)
#Yêu cầu HW2
def readImg(image):
    #Đọc ảnh và hiển thị ảnh đã tạo
    img = cv2.resize(image, (566, 1080), interpolation=cv2.INTER_LINEAR)
    axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Origin')


def RBG(image):
    #Tách ảnh thành b,g,r
    b, g, r = cv2.split(image)
    #Hiển thị từng lớp
    #cv2.imshow("red", r)
    #cv2.imshow("green", g)
    #cv2.imshow("blue", b)
    axs[0, 1].imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title('B')
    axs[0, 2].imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
    axs[0, 2].set_title('G')
    axs[1, 0].imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
    axs[1, 0].set_title('R')


def grayImg(image):
    #img = cv2.imread(image)
    #Chuyển ảnh thành đa mức xám
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Hiển thị ảnh gray scale
    axs[1, 1].imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    axs[1, 1].set_title('Gray scale')

def rotate(image):
    #img = cv2.imread(image)
    #Quay ảnh 100 lần, mỗi lần 10 độ
    rows, cols = image.shape[:2]
    for i in range(100):
        M = cv2.getRotationMatrix2D((cols/2, rows/2), 10*i, 1)
        rotate = cv2.warpAffine(image, M, (cols, rows))
        cv2.imshow("rotate", rotate)
        cv2.waitKey(100) 
   

def cropImg(image):
    #img = cv2.imread(image)
    # Đọc vào 1 ảnh, sau đó crop 1⁄4 ảnh tính từ tâm ảnh
    r, c = image.shape[:2]
    start_row, start_col = int(r/4), int(c/4)
    end_row, end_col = int(3*r/4), int(3*c/4)
    cropped = image[start_row:end_row, start_col:end_col]
    #Ảnh sau crop
    axs[1, 2].imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
    axs[1, 2].set_title('Crop 1/4')
    plt.show() 


image = cv2.imread("./jpg/pic1.jpg")
#Hiển thị ảnh và resize
readImg(image)
#Hiển thị RBG
RBG(image)
#Hiển thị ảnh gray scale
grayImg(image)
#Crop 1/4 ảnh từ tâm
cropImg(image)      
#Xoay ảnh 100 lần, mỗi lần 10 độ       
rotate(image)


