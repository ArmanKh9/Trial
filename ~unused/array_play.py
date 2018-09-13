'''import numpy as np
import os
import sys




image = cv2.imread('/home/arman/Desktop/Trial/image_2.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype(np.float32)

a=image.shape

print(image.shape[1])'''

'''a = np.array([[[1,2,3],
              [4,5,6]],[[1,2,3],
              [4,5,6]]])

print(a.shape)'''
################################################################
import sys
import glob
sys.path.append('/home/arman/Desktop/Trial/Images/Train/')
a = glob.glob('*.jpg')
print(a[0])