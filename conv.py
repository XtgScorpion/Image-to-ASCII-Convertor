import PIL.Image
import math

ramp1=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,. ")
ramp2=list(" .:-=+*#%@")
ramp2.reverse()

path=input('Image Location: ')
toascii=ramp2
image=PIL.Image.open(path)
w,h=image.size
r=h/w
nw=100
nh=int(nw*r)
image=(image.resize((nw,nh)))
image=image.convert('L')
imgvals=PIL.Image.Image.getdata(image)
boxLen=int(255/len(toascii))
print(nw,nh,len(imgvals), type(imgvals),boxLen)
imgvals2=''.join([toascii[int(a/boxLen)-1] for a in imgvals])
asciiimg="\n".join([imgvals2[a:(a+nw)] for a in range(0, len(imgvals2), nw)])
print('a')
f = open("ASCIIConverter\output.txt","w")
f.write(asciiimg)
