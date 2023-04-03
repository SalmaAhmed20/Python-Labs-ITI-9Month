import smtplib
sender_email = "ur email"

def sendEmail(recEmail,msg):
    password = "ur email password"
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recEmail, msg)

    print("Email sent successfully!")
    print("Check your inbox or junks/spam")