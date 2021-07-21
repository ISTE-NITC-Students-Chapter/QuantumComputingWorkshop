from PIL import Image, ImageDraw,ImageFont,ImageFilter
import csv
import pyqrcode
import png
from pyqrcode import QRCode
import random
import smtplib
import imghdr
from string import Template
from email.message import EmailMessage



def read_template(filename):
    mfile = open(filename)
    msg = mfile.read()
    return msg

def reader():
    names=[]
    emails=[]
    with open("names.csv",'r') as file:
        reader=csv.reader(file)
        for x in reader:
            names.append(x[0])
            emails.append(x[1])
    return(["abhishekthesuperb@gmail.com"],["abhishek"])


def geturl(name):
    name=name.replace(" ","")
    rand=str(random.randrange(0,10**5))
    st=r'https://raw.githubusercontent.com/ISTE-NITC-Students-Chapter/QuantumComputingWorkshop/main/Certificates/'+name+rand+".png"
    img=pyqrcode.create(st)
    img.png("QRCODES/"+name+rand+".png",scale=4)
    return(name+rand)

def automate(names,emails):
    data=[[names[x],emails[x]] for x in range(len(names))]
    for name,email in data:
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
        MY_ADDRESS = r''
        PASSWORD = r''
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        msg = EmailMessage()  
        message = read_template("Body.txt")
        msg['From'] = MY_ADDRESS
        msg['To'] = email.rstrip('\n')
        msg['Subject'] = "Quantum Computing Workshop"
        msg.set_content(message)
        with open("Certificates\{}.png".format(url), 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        s.send_message(msg)
        print("Message sent to", email)
        del msg
        s.quit()
        
def main():
    names,emails=reader()
    automate(names,emails)

main()
