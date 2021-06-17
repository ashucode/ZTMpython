import smtplib,sys
from email.message import EmailMessage
from string import Template
from pathlib import Path

userid=sys.argv[1]
pwd=sys.argv[2]
recipientid=sys.argv[3]

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Soul\'s Voice'
email['to']=recipientid
email['subject']='test email'
#email.set_content('this was sent using python scripting. have a nice day')
email.set_content(html.substitute({'name':recipientid.split('@')[0]}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login(userid,pwd)
	smtp.send_message(email)
	print('email sent!')