from dotenv import load_dotenv
import os
load_dotenv()

MLS_USER_ID = os.environ['MLS_USER_ID']
MLS_USER_PASS = os.environ['MLS_USER_PASS']
CONSUMERS_EMAIL = os.environ['RECIEVERS_EMAIL']
accountSID = os.environ["accountSID"]
authToken = os.environ["authToken"]
myTwilioNumber = os.environ["myTwilioNumber"]
myPhoneNumber = os.environ["myPhoneNumber"]
