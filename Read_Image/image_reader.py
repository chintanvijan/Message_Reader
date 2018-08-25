import pytesseract as pyt
import tesseract as tst
from PIL import Image
img = Image.open('edited.jpg')
#print(image_to_string(Image.open('edited.jpg')))

print(tst.image_to_string(img))