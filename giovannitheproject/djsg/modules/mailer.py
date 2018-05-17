# -*- coding: utf-8 -*-


def sendmail(mail, sel_month, name):
    import smtplib
    import os.path
    from email import encoders
    from email.utils import formatdate
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart

    FROM_ADDRESS = "giovannithedev@gmail.com"
    MY_PASSWORD = "Drum1995"
    TO_ADDRESS = mail
    SUBJECT = "勤務報告書"
    FILENAME = f"media/djsg/timecards/{sel_month}勤務報告書（{name}）.xlsx"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def create_message(from_addr, to_addr, subject, attach_file):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Date'] = formatdate()
        attachment = MIMEBase(
            'application',
            'vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        file = open(attach_file, 'rb')
        attachment.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment)
        msg.attach(attachment)
        attachment.add_header(
            "Content-Disposition", "attachment", filename=f'{sel_month}勤務報告書（{name}）.xlsx')
        return msg

    def send(from_addr, to_addr, msg):
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
        smtpobj.sendmail(from_addr, to_addr, msg.as_string())
        smtpobj.close()

    msg = create_message(
        FROM_ADDRESS, TO_ADDRESS, SUBJECT, os.path.join(
            BASE_DIR, FILENAME))
    send(FROM_ADDRESS, TO_ADDRESS, msg)