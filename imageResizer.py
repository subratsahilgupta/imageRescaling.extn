import cv2

path = input("Enter the path to your image :")

src = cv2.imread(fr"{path}",cv2.IMREAD_UNCHANGED)
percent = int(input("enter the percentage you want you image to be resized at: "))
scalePercent = percent

width = int(src.shape[1] * scalePercent / 100)
height = int(src.shape[0] * scalePercent / 100)
dsize =(width,height)

output = cv2.resize(src,dsize)

resizedImageName = input("What name do you want to give to your resized image: ")
resizedImageExtention = input("What extention do you want your resized image to have: ")

cv2.imwrite(f"{resizedImageName}.{resizedImageExtention}",output)
cv2.waitKey(0)