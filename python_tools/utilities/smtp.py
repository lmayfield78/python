from smtplib import SMTP
import smtplib
import email
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendMessage():

    def __init__(self): #sending gmail
        # google server
        self.server = smtplib.SMTP('smtp.gmail.com', 587)  # host name and port

        # connect to the server
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()



    def sendEmail(self, error):
        '''
        https://docs.python.org/3/library/email-examples.html
        https://en.wikibooks.org/wiki/Python_Programming/Email

        This function is the core of the email that will be sent out.
        :param error:
        :return: This will return the error given and added to the email.
        '''
        fromaddr = "vegeta.jerkface@gmail.com"
        toaddr = "it@sixpackshortcuts.com"
        #toaddr = "lmayfield@spscoach.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = 'ATTENTION!!! An Error has occurred with one of our sites.'

        body = "At " + time.strftime(" %H:%M:%S ") + " One of our websites has experienced the following problem. \n " \
               "The error is as follows:  \n" + str(error)

        msg.attach(MIMEText(body, 'plain'))

        # login
        self.server.login("vegeta.jerkface@gmail.com", "Vegetasps1")
        text = msg.as_string()
        #self.server.sendmail(fromaddr, toaddr, text)
        self.server.sendmail(msg['From'], msg['To'], text)



#https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
#https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
#https://docs.python.org/3/library/email-examples.html

# txt messaging? https://www.twilio.com/sms/pricing