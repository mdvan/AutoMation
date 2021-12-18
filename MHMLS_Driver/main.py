from firefoxdriver import Foreclosed_Properties_MHMLS
from SmsSender import txtself
import time

def main():
    """
    This is the main program
    """
    Foreclosed_Properties_MHMLS()
    txtself("Your Foreclosure Report is Ready, Look for an Email")

while True:
    main()
    time.sleep(100000000)
    