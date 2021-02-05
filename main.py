import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your-email-id-will be here', 'your-email-password-will-be-here')
for x in range(1):
        server.sendmail('sender-email',
                        'receiver-email',
                        'message-body')
