import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart   import MIMEMultipart
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
                    Name=attachment,
                )
            msg.attach(part)
        reply = server.login(username, passwd)
        reply
        print("Sending email...")
    return 