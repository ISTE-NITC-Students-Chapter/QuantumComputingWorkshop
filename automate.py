from PIL import Image, ImageDraw,ImageFont,ImageFilter
import csv
import pyqrcode
import png
from pyqrcode import QRCode
import random




def reader():
    names=[]
    emails=[]
    with open("names.csv",'r') as file:
        reader=csv.reader(file)
        for x in reader:
            names.append(x[0])
            emails.append(x[1])
    return(names,emails)


def geturl(name):
    name=name.replace(" ","")
    rand=str(random.randrange(0,10**5))
    st="www.github.io/"+name+rand
    img=pyqrcode.create(st)
    img.png("QRCODES/"+name+rand+".png",scale=6)
    return(name+rand)

def write(names):
    for name in names:
        img=Image.open("certificate.png",mode='r')
        width,height=img.width,img.height
        drawer=ImageDraw.Draw(img)
        font=ImageFont.truetype(r'C:\Users\91721\AppData\Local\Microsoft\Windows\Fonts\CAC Champagne.ttf',250)
        txt_width,_=drawer.textsize(name,font=font)
        drawer.text(((width-txt_width)//2,650),name,font=font,fill=(0,0,0,255) )
        url=geturl(name)
        qrc=Image.open("QRCODES/"+url+".png")
        img.paste(qrc,(300,1500))
        img.save("Certificates\{}.png".format(url))
        
def main():
    names,emails=reader()
    write(names)

main()