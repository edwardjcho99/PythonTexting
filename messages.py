import smtplib, ssl
import imaplib,email

# a class that sends and receives SMS messages
# from a specific email address
# so far, the only address you can use is gmail.
class MessageCarrier:

    # __init__ takes two parameters:
    # a string username and string password.
    # Important Security Note: do not upload code
    # that creates an instance of MessageCarrier without
    # the input() function. It is not safe to store passwords
    # in plain text.
    def __init__(self,username,password):

        if type(username) != str or type(password) != str:
            raise Exception("wrong input type")

        self.username = username
        self.password = password

        # Establish a secure session with gmail's incoming IMAP server
        self.imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
        self.imap_server.login(username,password)

        # Establish a secure session with gmail's outgoing SMTP server
        self.smtp_server = smtplib.SMTP_SSL("smtp.gmail.com")
        self.smtp_server.login(username,password)

    # Input: string, string, string
    # header: subject title of the message
    # message: the body of the message
    # address: the address receiving the message
    # format of address:
    # if it is a phone number, address="1234567890@carrier.com"
    # if it is an email address, address="example@email.com"
    # Future updates: look up carrier based on phone number,
    # be able to figure out whether it is sending
    # an email or phone number.
    def sendMessage(self,message,address,header=''):
        self.smtp_server.sendmail(header,address,message)

    # gets the most recent message in this instance's gmail
    def get_newest_message(self):
        result, data = self.imap_server.fetch(self.imap_server.select()[1][0],'(RFC822)')
        raw = email.message_from_bytes(data[0][1])
        def get_message(msg):
            if msg.is_multipart():
                return get_message(msg.get_payload(0))
            else:
                return msg.get_payload(None, True)
        return get_message(raw).decode("utf-8")
