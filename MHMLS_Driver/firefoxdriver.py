from selenium import webdriver
from selenium.webdriver.firefox import firefox_profile
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config import MLS_CONSUMER_ID, MLS_CONSUMER_PASS, CONSUMERS_EMAIL
import time

def Foreclosed_Properties_MHMLS():
    """
    This is a Function that find the current foreclosures in Dutchess County, Creates a Document, and Sends myself an email of the Document.
    """
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

    # Bring to Search Page
    browser.get("http://www.midhudsonmls.com/XMLSearch/XMLSearch.asp?strSearchName=MLSA&frommenu=1")

    # Get Saved Searches
    SavedSearchesElement = browser.find_element_by_link_text('Saved Searches')
    SavedSearchesElement.click()
    # Get DUT ForeClosures Search
    DUTForeclosureElement = browser.find_element_by_css_selector("#SaveListBox > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > select:nth-child(1) > option:nth-child(2)")
    DUTForeclosureElement.click()
    OpenButtonElement = browser.find_element_by_css_selector("#SaveListBox > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1) > img:nth-child(1)")
    OpenButtonElement.click()
    # Search
    SearchButtonElement = browser.find_element_by_css_selector(".search-btnNew")
    SearchButtonElement.click()

    # Print this to a PDF
    time.sleep(2)
    CheckAllElement = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/form/ul/li[1]/a")
    CheckAllElement.click()

    time.sleep(1)
    ReviseSearchElement = browser.find_element_by_xpath("./html/body/div[5]/div[1]/div[2]/select")
    ReviseSearchElement.click()
    time.sleep(1)
    PublicFull = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/select/option[25]")
    PublicFull.click()

    GoElement = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/input[3]")
    GoElement.click()

    # Send An Email with the Foreclosures
    time.sleep(1)
    EmailSenderElement = browser.find_element_by_xpath("/html/body/table[3]/tbody/tr[2]/td[2]/input")
    EmailSenderElement.send_keys(CONSUMERS_EMAIL)
    SubjectLineElement = browser.find_element_by_xpath("/html/body/table[4]/tbody/tr[2]/td[2]/input")
    SubjectLineElement.send_keys("Current MIDHUDSON MLS Foreclosures in Dutchess County")
    EmailBodyElement = browser.find_element_by_css_selector("#Msg")
    EmailBodyElement.send_keys("Dear Michael,\n \nAttached is a document with a list of all of the current foreclosures listed on the Mid-Hudson MLS in Dutchess County.\n")
    EmailSignElement = browser.find_element_by_css_selector("table.noprint:nth-child(59) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > textarea:nth-child(1)")
    EmailSignElement.send_keys("From Me to You,\nMichael Vanikiotis")
    SendEmailElement = browser.find_element_by_css_selector("input.input_img:nth-child(1)")
    SendEmailElement.click()

    # Close the Driver
    time.sleep(5)
    browser.close()

# Testing:
# Foreclosed_Properties_MHMLS()

