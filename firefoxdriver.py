from selenium import webdriver
from selenium.webdriver.firefox import firefox_profile
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config import MLS_CONSUMER_ID, MLS_CONSUMER_PASS
import time

def SignIn_MHMLS():
    profile = webdriver.FirefoxProfile()

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX


    #This starts a Firefox session 
    browser = webdriver.Firefox(executable_path = GeckoDriverManager().install(), firefox_profile=profile, desired_capabilities=desired)
    browser.get("http://www.midhudsonmls.com/Login.asp")

    #Enters in Email and Pass
    EmailElement = browser.find_element_by_css_selector('input#MemberId')
    EmailElement.send_keys(MLS_CONSUMER_ID)
    PassElement = browser.find_element_by_css_selector('input#MemberPassword')
    PassElement.send_keys(MLS_CONSUMER_PASS)

    #Submits the Email and Pass
    time.sleep(2)
    AccessAccountElement = browser.find_element_by_id("submit1")
    AccessAccountElement.click()


# SignIn_MHMLS()

