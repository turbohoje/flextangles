#!/usr/bin/python

from PIL import Image

#pull in the backgroun
background = Image.open("template.jpg").convert('RGBA')

#pull in test image
img = Image.open("butters.jpg").convert('RGBA')

#crop it
x = 730
y = 420
width = 500
height = width

outsize = 315

buttersCrop = img.crop((x, y, x+width, y+height)).resize((outsize, outsize)).convert('RGBA')
buttersCrop.save("buttersCrop.jpg")

diamond1 = buttersCrop.crop((0,0, 160,240))
diamond1 = diamond1.rotate(64, expand=1)
# fff = Image.new('RGBA', diamond1.size, (255,255,255,0))
# diamond1 = Image.composite(diamond1, fff, diamond1)

placement = (200, 0)
background.paste(diamond1, placement, diamond1)

background.save("output.jpg")