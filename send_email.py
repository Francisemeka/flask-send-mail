import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_welcome_email(recipient_email):
    sender_email = 'francisonoyima@gmail.com'
    sender_password = 'zsrn xbti hpdh thmx'
    subject = "Welcome to our website"
    body = """
<!DOCTYPE html>
<html>
<body>
    <div>
       <h1>Welcome to our website!</h1>
    </div>
</body>
</html>
"""

    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email 

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, html_message.as_string())

# Handle form submission
if __name__ == '__main__':
    recipient_email = input("Enter recipient's email: ")
    send_welcome_email(recipient_email)
    print('Email sent!')
