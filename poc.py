#!/usr/bin/python

from PIL import Image, ImageDraw

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
# buttersCrop.save("buttersCrop.jpg")

#first diamond
diamond1 = buttersCrop.crop((0,0, 160,240))
diamond1_mask = Image.new("RGBA", buttersCrop.size)
dr = ImageDraw.Draw(diamond1_mask)
dr.polygon([(155,0),(155,160),(0,240),(0,80)], outline=(0xff, 0xff, 0xff), fill=(0xff, 0xff, 0xff) )
diamond1 = Image.composite(buttersCrop, diamond1_mask, diamond1_mask)
# diamond1.save("1.jpg")


#second diamond
diamond2 = buttersCrop.crop((0,0, 160,240))
diamond2_mask = Image.new("RGBA", buttersCrop.size)
dr = ImageDraw.Draw(diamond2_mask)
dr.polygon([(155,0),(312,80),(312,240),(155,160)], outline=(0xff, 0xff, 0xff), fill=(0xff, 0xff, 0xff) )
diamond2 = Image.composite(buttersCrop, diamond2_mask, diamond2_mask)
# diamond2.save("2.jpg")


#third diamond
diamond3 = buttersCrop.crop((0,0, 160,240))
diamond3_mask = Image.new("RGBA", buttersCrop.size)
dr = ImageDraw.Draw(diamond3_mask)
dr.polygon([(155,160),(312,240),(155,312),(0,240)], outline=(0xff, 0xff, 0xff), fill=(0xff, 0xff, 0xff) )
diamond3 = Image.composite(buttersCrop, diamond3_mask, diamond3_mask)
# diamond3.save("3.jpg")

diamond1 = diamond1.rotate(124, expand=1)
d1_placement = (-220, -223)
d1_otherPlacement = (686, -223)

diamond2 = diamond2.rotate(57, expand=1)
d2_placement = (87, -55)

diamond3 = diamond3.rotate(180, expand=1)
d3_placement = (470, 0)


background.paste(diamond1, d1_placement, diamond1)
background.paste(diamond2, d2_placement, diamond2)
background.paste(diamond3, d3_placement, diamond3)
background.paste(diamond1, d1_otherPlacement, diamond1)

background.save("output.jpg")