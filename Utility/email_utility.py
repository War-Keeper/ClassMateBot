import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailUtility:

    def __init__(self):
        self.username = 'username'
        self.password = 'password'
        self.from_address = 'classmatebot@gmail.com'
        self.subject = 'CLASSMATE BOT NOTIFICATION'

    def send_email(self, recipient: str, attachment=None, subject: str = '', body: str = '', filename: str = ''):
        to_address = recipient if type(recipient) is list else [recipient]

        msg = MIMEMultipart()
        msg['Subject'] = subject if subject else self.subject
        msg['From'] = self.from_address
        msg['To'] = recipient
        body = body if body else "This mail was sent from classmatebot notification service, Please unsubscribe to stop notifications."
        msg.attach(MIMEText(body, 'plain'))

        if attachment:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
            msg.attach(part)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(list(self.from_address), to_address, msg.as_string())
            server.close()
            print("successfully sent the mail to " + recipient)
        except Exception as error:
            print(error.__str__())
            print("failed to send mail to " + recipient)

