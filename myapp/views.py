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
# Create your views here.
from google_images_download import google_images_download  # importing the library

# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/charmander_counter.png

# import the necessary packages
# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/charmander_counter.png

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
def prediction (model, labelbin, image):
    args = [model, labelbin, image]
    # load the image
    image = cv2.imread(args[2])
    # output = image.copy()

    # pre-process the image for classification
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # load the trained convolutional neural network and the label
    # binarizer
    # print("[INFO] loading network...")
    model = load_model(args[0])
    lb = pickle.loads(open(args[1], "rb").read())
    # classify the input image
    # print("[INFO] classifying image...")
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    return label

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
        image_predict = new_data.file
        print(str(image_predict))
        new_data.save()
        result = prediction("myapp/model/new_model", "myapp/model/labelbin", "D:/django_project/django_project/media/"+str(image_predict))
        print(result)
        api.search(result)
    context = {'form': form}
    return render(request, 'index.html', context)


def new_index(request):
