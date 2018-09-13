from os import listdir
from PIL import Image
    
for filename in listdir('/home/arman/Desktop/Trial/Images/Train/'):
  if filename.endswith('.jpg'):
    try:
      img = Image.open('/home/arman/Desktop/Trial/Images/Train/'+filename) # open the image file
      img.verify() # verify that it is, in fact an image
    except (IOError, SyntaxError) as e:
      print('Bad file:', filename) # print out the names of corrupt files
      
      
for filename in listdir('/home/arman/Desktop/Trial/Images/Train/'):
  if filename.endswith('.jpg'):
    print(filename)