import smtplib
from email.mime.text import MIMEText
import gui_bot as gui

password =
from_msg = 'oshahar149@gmail.com'
Subject = "Bot cake"
TEXT = " Hi, \n\n Yum Yum Yum ! \n  you brings a cake to the next meeting ! \n\n your friendly automated cake bot"
message = 'Subject: {}\n\n{}'.format(Subject, TEXT)
To = []


try:
    start = gui.gui()
    if ( start == "run"):
        f = open("names.txt", "r")
        for line in f:
            To.append(line)
        s = smtplib.SMTP_SSL( 'smtp.gmail.com', 465)
        s.login(from_msg, password)
        s.sendmail(from_msg,To,message)
        print('Mail sent')
        s.quit()
    else:
        gui.gui_error()
except:
    print("An exception occurred")



