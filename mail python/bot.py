import smtplib
import os
from email.mime.text import MIMEText
import gui_bot as gui
import imghdr
from email.message import EmailMessage

password = ' '
from_msg = 'oshahar149@gmail.com'
Subject = "Bot cake   "
TEXT = " Hi, \n\n Yum Yum Yum ! \n  you brings a cake to the next meeting ! \n\n your friendly automated cake bot"
To = []


msg = EmailMessage()
msg['Subject'] = Subject
msg['From'] = from_msg

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;"><p>Hi, Yum Yum Yum !</p> </h1>
        <h2 style="color:SlateGray;"><p>you brings a cake to the next meeting ! </p></h2> 
        <h2 style="color:SlateGray;"><p></p></h2>
        <h2 style="color:SlateGray;"><p></p></h2>
        <h2 style="color:SlateGray;"><p></p></h2>
        <h2 style="color:SlateGray;"><p>your friendly automated cake bot</p></h2>
        <img src="robot.jpg" >
    </body>
</html>
""", subtype='html')

msg_next = EmailMessage()
msg_next['Subject'] = Subject
msg_next['From'] = from_msg

msg_next.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;"><p>Hi, Yum Yum Yum !</p> </h1>
        <h2 style="color:SlateGray;"><p>You bring a cake right after the upcoming meeting ! </p></h2> 
        <h2 style="color:SlateGray;"><p>Please get ready ! </p></h2>
        <h2 style="color:SlateGray;"><p></p></h2>
        <h2 style="color:SlateGray;"><p></p></h2>
        <h2 style="color:SlateGray;"><p>your friendly automated cake bot</p></h2>
        <img src="robot.jpg" >
    </body>
</html>
""", subtype='html')





def update_file(To):
    tmp = To[0]
    for i in range(0,len(To)-1):
        To[i]= To[i+1]
    To[(len(To) - 1)] = tmp
    f = open("names.txt", "w")
    for name in To:
        f.write(name)
    f.close()

try:
    start = gui.gui()
    if ( start == "run"):
        f = open("names.txt", "r")
        for line in f:
            To.append(line)
        s = smtplib.SMTP_SSL( 'smtp.gmail.com', 465)
        s.login(from_msg, password)

        msg['To'] = To[0]
        s.send_message(msg)

        update_file(To)

        msg_next['To'] = To[1]
        s.send_message(msg_next)
        print('Mail sent')
        s.quit()
    else:
        gui.gui_error()
except:
    print("An exception occurred")


