import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_whoer_data():

    page = requests.get("https://whoer.net")
    soup = BeautifulSoup(page.content, "html.parser")
    
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('log-level=3')
    op.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=op)

    driver.get("http://whoer.net")
    driver.implicitly_wait(0.5)

    #get ip address
    results = soup.find("strong", class_="your-ip")
    ip = (results.text.strip())

    #get dns 
    dns_address = driver.find_elements(By.XPATH, "//div[@class='dns_br']")
    dns_address = (dns_address[0].text)
    dns = (dns_address[: dns_address.find(' ')])

    #get proxy status, anonynmizer status, blacklist status
    proxy = soup.find("span", class_ = "proxy-status-message")
    proxy = proxy.text.strip()
    anonymizer = soup.find("span", class_ = "value")
    anonymizer = anonymizer.text.strip()
    blacklist = soup.find("div", class_= "enabled-status__wrapper")
    blacklist = blacklist.text.strip()

    #get local time
    local_time = soup.find("span", class_="time")
    local_time = local_time.text.strip()
    opening_parens = local_time.find('(')
    local_timezone = (local_time[opening_parens + 1: -1])

    # get system time to see time discrepancies
    system_time = driver.find_element(By.CLASS_NAME, "js-time")
    system_time = (system_time.text)
    opening_parens = system_time.find('(')
    system_timezone = (system_time[opening_parens +1: -1])
    if system_timezone == "Eastern Standard Time":
        system_timezone = "EST"
    if system_timezone != local_timezone:
        discrepancies="Time zone different for local and system"
    else:
        discrepancies="None noted"

    driver.quit()
    whoer_json = {
        "ip": ip, 
        "dns": dns,
        "proxy": proxy,
        "anonymizer": anonymizer,
        "blacklist": blacklist,
        "timezone": local_timezone,
        "system_discrepancies": discrepancies
    }
    return whoer_json
