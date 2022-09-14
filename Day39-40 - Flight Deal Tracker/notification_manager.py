import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.my_email = "dgko31@gmail.com"
        self.password = "vkomkcdthltoqtpr"

    def send_email(self, message):
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # check connection
            server.starttls()  # Secure the connection
            server.ehlo()  # check connection
            server.login(self.my_email, self.password)

            # Send email here
            server.sendmail(from_addr=self.my_email,
                            to_addrs="berkeebrus@gmail.com",
                            msg=f"Subject:Cheap Flight Found!!!!\n\n{message}")
