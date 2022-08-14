import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as msgbox

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()        #taking image
    try:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    except:
        e = 'Model not found,Please train model'
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(e)
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
        
    now = time.time()  ###For calculate seconds of video
    future = now + 20
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture('http://192.168.43.44:8080/video')
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Enrolment', 'FName', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            global Id

            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf <70):
                print(conf)
               
                global aa
                global date
                global timeStamp
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Enrolment'] == Id]['FName'].values
                global tt
                tt = str(Id) + "-" + aa
                En = '15624031' + str(Id)
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                cv2.putText(im, str(tt), (x , y+w), font, 1, (255, 255, 255), 3)

            else:
                Id = 'Unknown'
                tt = str(Id)
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                cv2.putText(im, str(tt), (x , y+h), font, 1, (0, 25, 255), 2)
        if time.time() > future:
            break

        attendance = attendance.drop_duplicates(['Enrolment'])
        cv2.imshow('Filling attedance..', im)
        key = cv2.waitKey(30) & 0xff
        if key == 27:
            break

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance/"  + "Attendance_" + date + "_" + ".csv"
    attendance = attendance.drop_duplicates(['Enrolment'])
    print(attendance)
    attendance.to_csv(fileName)
    print("Success")
    
    date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
    DB_Table_name = str(  "Attendance_" + date_for_DB )
    import pymysql.connections

    ###Connect to the database
    try:
        global cursor
        connection = pymysql.connect(host='localhost', user='root', password='', db='Face')
        cursor = connection.cursor()
    except Exception as e:
        print(e)

    sql = "CREATE TABLE " + DB_Table_name + """
                (ID INT NOT NULL AUTO_INCREMENT,
                 ENROLLMENT varchar(100) NOT NULL,
                 NAME VARCHAR(50) NOT NULL,
                 DATE VARCHAR(20) NOT NULL,
                 TIME VARCHAR(20) NOT NULL,
                     PRIMARY KEY (ID)
                     );
                """    
    ####Now enter attendance in Database
    insert_data =  "INSERT INTO " + DB_Table_name + " (ID,ENROLLMENT,NAME,DATE,TIME) VALUES (0, %s, %s, %s,%s)"
    VALUES = (str(Id), str(aa), str(date), str(timeStamp))
    try:
        cursor.execute(sql)  ##for create a table
        connection.commit()
    except:
        cursor.execute(insert_data, VALUES)##For insert data into table
        connection.commit()
  
    else:
        cursor.execute(insert_data, VALUES)##For insert data into table
        connection.commit()
    
    cam.release()
    cv2.destroyAllWindows()


TrackImages()
