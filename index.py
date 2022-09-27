from PIL import Image
import os

os.system("clear")
dirr = r"img/"
img = os.listdir(dirr)
logo = Image.open("logo.png")
wCount = len(img)
c = 0
while c < wCount:
    copy_image = Image.open(dirr+img[c])
    copy_logo = logo.copy()
    copy_image.paste(copy_logo,(0,0),copy_logo)
    copy_image.save('output/'+img[c])
    c += 1
print("done! saved in output/")

# created by dai re
# 27 sep 23
