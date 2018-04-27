# -*- coding: utf-8 -*-

def sendmail(nextmonth, sendaddres):
    import smtplib
    import os.path
    import datetime
    from email import encoders
    from email.mime.text import MIMEText
    from email.utils import formatdate
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart


    FROM_ADDRESS = "giovannithedev@gmail.com"
    MY_PASSWORD  = "Drum1995"
    TO_ADDRESS = sendaddres
    SUBJECT= f"{nextmonth}月シフト"
    BODY = f"{nextmonth}月のシフトです。"
    
    FILENAME = f"djsg/media/djsg/shifts/{nextmonth}月のShift.xlsx"    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    
    
    def create_message(from_addr, to_addr, body, subject, attach_file):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['BODY'] = body
        msg['Date'] = formatdate()
        attachment = MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        file = open(attach_file, 'rb')
        attachment.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment)
        msg.attach(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=f'{nextmonth}月分のShift.xlsx')
        return msg
    def send(from_addr, to_addr, msg):
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
        smtpobj.sendmail(from_addr, to_addr, msg.as_string())
        smtpobj.close()



    msg= create_message(FROM_ADDRESS, TO_ADDRESS, SUBJECT, BODY, os.path.join(BASE_DIR, FILENAME))
    send(FROM_ADDRESS, TO_ADDRESS, msg)
