import os, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

def send_gmail(to, subject, text, attach):
	msg=MIMEMultipart()
	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMEText(text))
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(attach, 'rb').read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(attach))

	msg.attach(part)
	mailServer=smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg.as_string())
	mailServer.close()

if __name__ == "__main__":
	title = "test mail"
	to = "darkziny2@gmail.com"
	gmail_user = "darkziny2@gmail.com"
	gmail_pwd = "ziny5601"
	message = "simple test - send email by gmail"
	attach_file = "./abc.jpg"

	send_gmail(to, title, message, attach_file)
