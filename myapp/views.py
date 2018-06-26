from django.shortcuts import render, HttpResponse
from . forms import data
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import cv2
import os
from . import api
from . model import classify as cs


def sendmail(reciever, mes):
    sender = 'nahi.khojoge@gmail.com'  # place your email id here
    sender_pswd = 'nahi1234'  # place your pswd here
    # reciever = 'piplani.rohan@gmail.com'
    attach = 'myapp/downloads/selena/sel.jpg'
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = "selena image"
    msg.preamble = "selena image"

    ctype, encoding = mimetypes.guess_type(attach)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "image":
        print ('image')
        fp = open(attach, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()

    attachment.add_header("Content-Disposition", "attachment", filename=attach)
    msg.attach(attachment)

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender, sender_pswd)
    mail.sendmail(sender, reciever, msg.as_string())
    mail.close()


def index(request):
    import subprocess
    form = data(request.POST or None, request.FILES)
    if form.is_valid():
        new_data = form.save(commit=False)
        image_predict = new_data.upload_your_image
        print(str(image_predict))
        new_data.save()
        result = cs.prediction("myapp/model/new_model", "myapp/model/labelbin", "D:/django_project/django_project/media/"+str(image_predict))
        min_range = new_data.min_range
        maax_range = new_data.max_range

        print(result)
        api.search(result)
        new_data.delete()
        os.system("RD /S /Q D:\django_project\django_project\media")
    context = {'form': form}
    return render(request, 'index.html', context)



