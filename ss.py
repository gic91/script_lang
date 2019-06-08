import  smtplib
from email.mime.text import  MIMEText

def sendMail(me, you, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(me, 'dltkdwlr2934')
    msg = MIMEText(msg)
    msg['Subject'] = '날씨정보'
    smtp.sendmail(me, you, msg.as_string())
    smtp.quit()

sendMail('gic9111@gmail.com', 'gic911@naver.com', '메일보내기')