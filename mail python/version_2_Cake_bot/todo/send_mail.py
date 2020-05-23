import smtplib
import os
from email.mime.text import MIMEText
import imghdr
from email.message import EmailMessage

password = 'or1Q1Q1Q'
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
        <h2 style="color:SlateGray;"><p>you brings a cake to the next group meeting ! </p></h2> 
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


# todo : 2 mails in one press - to the next member that will bring cake
msg_next.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;"><p>Hi, Yum Yum Yum !</p> </h1>
        <h2 style="color:SlateGray;"><p>You bring a cake right after the upcoming group meeting ! </p></h2> 
        <h2 style="color:SlateGray;"><p>Please get ready ! </p></h2>
        <h2 style="color:SlateGray;"><p></p></h2>
        <h2 style="color:SlateGray;"><p></p></h2>
        <h2 style="color:SlateGray;"><p>your friendly automated cake bot</p></h2>
        <img src="robot.jpg" >
    </body>
</html>
""", subtype='html')




def caller (member1 = None , member2 = None ):
    To = [member1 ,member2 ]
    if ( member1 != None):
        s = smtplib.SMTP_SSL( 'smtp.gmail.com', 465)
        s.login(from_msg, password)

        msg['To'] = To[0]
        s.send_message(msg)
        # todo : 2 mails in one press - to the next member that will bring cake
        if (member2 != None):
            msg_next['To'] = To[1]
            s.send_message(msg_next)
            s.quit()
    else:
        print ( "need more them one mail of mamber ")
