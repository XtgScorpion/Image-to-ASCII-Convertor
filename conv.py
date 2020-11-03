import PIL.Image

toascii=['@','#','£','=','+','|',':','.',' ']
def main(i):
    if i>5:
        print('Mate how can you not even paste the location of an image properly...')
        return
    try:
        path=input('Image Location: ')
        image=PIL.Image.open(path)
        w,h=image.size
        r=h/w
        nw=1000
        nh=int(nw*r)
        image=(image.resize((nw,nh)))
        image=image.convert('L')
        imgvals=image.getdata()
        imgvals=''.join([toascii[int(a/30)] for a in imgvals])
        asciiimg="\n".join([imgvals[a:(a+nw)] for a in range(0, len(imgvals), nw)])
        with open("img.txt", "w") as f:
            f.write(asciiimg)
    except: 
        print('Invalid Path location. Try again'+'\n') 
        main(i+1)
main(0)
