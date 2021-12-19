from twilio.rest import Client, TwilioClient
from config import accountSID, authToken, myPhoneNumber, myTwilioNumber

twilioCli = Client(accountSID, authToken)
myTwilioNumber = myTwilioNumber
myPhoneNumber = myPhoneNumber

def txtself(message):
    """
    This is a Function that sends a message to my cell phone
    """
    twilioCli.messages.create(body= f'{message}', from_= myTwilioNumber, to= myPhoneNumber)
  
# testing:
# txtself("Hey Bro")
