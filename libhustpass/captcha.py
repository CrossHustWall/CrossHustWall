from PIL import Image, GifImagePlugin, ImageFilter
from pytesseract import image_to_string

def Fuckit(imageContent):
    imageObject = Image.open(imageContent)
    imageObject.seek(1)
    grayImage = imageObject.convert("L")
    binarizedImage = grayImage.point(lambda i: i < 255 and 255)
    depointedImage = binarizedImage.filter(ImageFilter.MedianFilter(5))
    code = image_to_string(depointedImage, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return code
