
# Project: Image Processor 
# Source: https://www.youtube.com/watch?v=vEQ8CXFWLZU&list=WL&index=7&t=57s


from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}") # image variable holds the image object
    
    # Apply edits to all photos then save the edited photo. Sharpen and Black and White.
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    
    # Increase Contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splittext(filename)[0]
     
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')