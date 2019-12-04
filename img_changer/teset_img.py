from PIL import Image
import requests
import cv2
import numpy

### PIL - 이미지변형을 위한
### opencv - 보다 복잡한 연산을 필요로 할때

## 1. PIL
url = 'https://cdn.pixabay.com/photo/2019/10/29/16/43/rope-4587474_960_720.jpg'
img = Image.open(requests.get(url, stream = True).raw)
#img = Image.open('/home/perth/Desktop/workspace/personal_project/00001.jpg')
#img = img.rotate(45)
#img.show()
#print(img.size)


## 2. cv2
img2 = cv2.imread('/home/perth/Desktop/workspace/personal_project/00001.jpg', cv2.IMREAD_COLOR)

# content -> data
arr = numpy.asarray(bytearray(requests.get(url).content), dtype=numpy.uint8)
img3 = cv2.imdecode(arr, cv2.IMREAD_COLOR)

cv2.imshow('A', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(type(img2))