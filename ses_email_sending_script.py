from email.utils import formataddr
from smtplib import SMTP_SSL, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = 'email registered and verified in SES'
SENDERNAME = 'FirstName LastName'

RECIPIENT = 'somemail@gmail.com'

USERNAME_SMTP = 'SES credentials username generated'
PASSWORD_SMTP = 'SES credentials secret key generated'

CONFIGURATION_SET = "you need to create the configuration set - however it's not needed"

HOST = "email-smtp.eu-central-1.amazonaws.com" #Check which smtp endpoing are you using
PORT = 465 #or 2465

SUBJECT = 'Subject of the email'

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Hello,\r\n"
             "You are invited to and origanization "
             "Please open and accept invitation.\r\nOrganization Team Team")

# The HTML body of the email.
BODY_HTML = """<!DOCTYPE html>
<html>
<head>
</head>
<body>
    Hello, <br>
    You are invited to and origanization <b>{{ organization_name }}</b> <br>
    Please open <a href="{{ url }}" target="blank">Link</a> and accept invitation <br><br>
    <b>Organization Team</b>
</body>
</html>"""

msg = MIMEMultipart('alternative')
msg['Subject'] = SUBJECT
msg['From'] = formataddr((SENDERNAME, SENDER))
msg['To'] = RECIPIENT
msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

part1 = MIMEText(BODY_TEXT, 'plain')
part2 = MIMEText(BODY_HTML, 'html')

msg.attach(part1)
msg.attach(part2)

context = ssl.create_default_context()
try:
    with SMTP_SSL(HOST, PORT) as server:
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
        print("Email sent!")

except SMTPException as e:
    print("Error: ", e)
