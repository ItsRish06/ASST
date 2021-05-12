import smtplib
from email.message import EmailMessage

def sendMail(info):

    EMAIL_ADDRESS = 'asst.technology@gmail.com'
    EMAIL_PASSWORD = 'tavrhxttyhlvmaak'
    body = f"{info['name']} was detected to have a temperature of {info['temp']}*C."
    msg = EmailMessage()
    msg['Subject'] = 'Resident temperature high!'
    msg['From'] = EMAIL_ADDRESS
    msg['to'] = 'debanik.kundu@sakec.ac.in'
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        smtp.send_message(msg)
