from PIL import Image, GifImagePlugin, ImageFilter
from pytesseract import image_to_string

def Fuckit(imageContent):
    imageObject = Image.open(imageContent)
    imageObject.seek(1)
    grayImage = imageObject.convert("L")
    binarizedImage = grayImage.point(lambda i: i < 255 and 255)
    #binarizedImage = binarizing(imageObject, 255)
    depointedImage = binarizedImage.filter(ImageFilter.MedianFilter(5))
    code = image_to_string(depointedImage, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return code

def binarizing(img,threshold):
    img = img.convert("L") 
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def depoint(img):
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:#上
                count = count + 1
            if pixdata[x,y+1] > 245:#下
                count = count + 1
            if pixdata[x-1,y] > 245:#左
                count = count + 1
            if pixdata[x+1,y] > 245:#右
                count = count + 1
            if pixdata[x-1,y-1] > 245:#左上
                count = count + 1
            if pixdata[x-1,y+1] > 245:#左下
                count = count + 1
            if pixdata[x+1,y-1] > 245:#右上
                count = count + 1
            if pixdata[x+1,y+1] > 245:#右下
                count = count + 1
            if count > 4:
                pixdata[x,y] = 255
    return img

