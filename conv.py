import PIL.Image 
import math
import requests
import sys

# Your ASCII Ramp sort on darkest to lightest characters
toascii = list(reversed(list(" .:-=+*#%@")))
# Grab the file path
option = input("Where is your image from (local or web)? ")
path = input("Image Location: ")

# Open the file and extract the width and height
if option == "local":
    image = PIL.Image.open(path)
elif option == "web":
    image = PIL.Image.open(requests.get(path, stream=True).raw)

w,h = image.size
# Get the new dimensions with a max width/height of 100
if w > h:
    r = h/w
    nw = 300
    nh = int(nw*r)
else:
    r = w/h 
    nh = 300
    nw = int(nh*r)

# Resize the image, convert to grayscale, and get the data in a flattened 2d array
image = image.resize((nw,nh))
image = image.convert('L')
imgVals = PIL.Image.Image.getdata(image)

# Change each grayscale pixel to its ASCII ramp equivelent and combine with newlines
boxLen = int(255/len(toascii))
imgVals2 = ''.join([toascii[int(a/boxLen)-1] for a in imgVals])
asciiImg = "\n".join([imgVals2[a:(a+nw)] for a in range(0, len(imgVals2), nw)])

# Write the ASCII Image to a text file
f = open(sys.path[0]+"\output.txt","w")
f.write(asciiImg)
