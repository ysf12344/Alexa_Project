import selenium
import requests
import googleapiclient.discovery
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def play(song):
    options = Options()
    api_service_name = "youtube"
    api_version = "v3"
    driver = webdriver.Chrome(service=Service(), options=options)
    
   
    DEVELOPER_KEY = "xxx"#add you API keys

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(part="snippet",maxResults=5,q=song,type="playlist")

    response = request.execute()


    playlistid=response["items"]
    playlistid=playlistid[1]["id"]["playlistId"]  #first item
    driver.get(f"https://www.youtube.com/playlist?list={playlistid}")

    accept_all= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[.//span[text()='Accept all']]")))
    accept_all.click()
    play_all= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@aria-label='Play all']")))

    play_all.click()

    input("Press Enter to close browser...")


    driver.quit()
    return None


# # API information

# # API key
# DEVELOPER_KEY = "xx"
# # API client
# youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

# request = youtube.search().list(part="snippet",maxResults=5,q="chaabi",type="playlist")

# response = request.execute()


# playlistid=response["items"]
# playlistid=playlistid[1]["id"]["playlistId"]  #first item


# pprint(playlistid)


