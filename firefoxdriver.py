from selenium import webdriver
from selenium.webdriver.firefox import firefox_profile
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config import MLS_CONSUMER_ID, MLS_CONSUMER_PASS
import time

def Foreclosed_Properties_MHMLS():
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



    # # Get DUT Results / Click OK Button
    # OKButtonElement = browser.find_element_by_id("CriteriaOKButton")
    # OKButtonElement.click()

    # # Get Active Results
    # StatusElement = browser.find_element_by_link_text('Status')
    # StatusElement.click()

    # # Get Active Results
    # OKButtonElement = browser.find_element_by_id("CriteriaOKButton")
    # OKButtonElement.click()

    # # Get Forclosures
    

Foreclosed_Properties_MHMLS()

