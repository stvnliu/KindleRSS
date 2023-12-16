import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText
from email.utils            import formatdate, COMMASPACE
SMTP_SERVERS = {
    "gmail.com": "smtp.gmail.com"
}
def mailsend(
        username: str,
        passwd: str,
        recipient: str, 
        mail_msg: str,
        subject: str,
        mail_attachments: list,
        mailserver: str = None
    ) -> bool:
    ssl_port = 465
    context = ssl.create_default_context()
    domain = username.split("@")[1]
    if not mailserver:
        mailserver = SMTP_SERVERS[domain]
    with smtplib.SMTP_SSL() as server:
        server.login(username, passwd)
        msg = MIMEMultipart()
        msg["From"] = username
        msg["To"] = recipient
        msg["Date"] = formatdate(localtime=True)
        msg["Subject"] = subject
        for attachment in mail_attachments:
            with open(attachment, "rb") as file:
                part = MIMEApplication(
                    file.read(),
                    Name=
                )
            msg.add_attachment(attachment)
        print("Sending email...")
    return 
port = 465
context = ssl.create_default_context()
username = input("Email address you would like to send the Kindle email from: ")
_mailserver = input("If you have a custom SMTP server address you would like to use, state here, or leave blank to continue: ")
with smtplib.SMTP_SSL(\
        _mailserver if _mailserver else SMTP_SERVERS[username.split("@")[1]],\
        port=port, \
        context=context \
    ) as server:
    passwd = input("Password for the email address: ")
    server.login(username, passwd)

