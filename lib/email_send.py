import smtplib
import ssl
from email import message
SMTP_SERVERS = {
    "gmail.com": "smtp.gmail.com"
}
def mailsend(
        username: str,
        passwd: str, 
        mail_msg: str,
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
        msg = message.EmailMessage()
        for attachment in mail_attachments:
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


