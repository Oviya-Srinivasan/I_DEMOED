import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import os
import sys
import cv2
import numpy as np
import qrcode

def resource_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),relative)

list_of_QR = os.listdir(resource_path("QR_code_Images"))
My_qr = cv2.imread(resource_path("QR_code_Images\\")+list_of_QR[len(list_of_QR)-1])
detector = cv2.QRCodeDetector()
Data, bbox, straight_qrcode = detector.detectAndDecode(My_qr)
print(Data)
Master_list2 = str(Data)
Master_list = Master_list2.split("#")
Medicine_list = [["Panadol",1,1],["Ibuprofen",1,2],["Paracetomol",2,1]]

Coord_list = []
for i in range(1,len(Master_list)):
    Coord = []
    for j in range(0,len(Medicine_list)):
        if Master_list[i]==Medicine_list[j][0]:
            Coord.append(Medicine_list[j][1])
            Coord.append(Medicine_list[j][2])
    Coord_list.append(Coord)

print(Coord_list)           


