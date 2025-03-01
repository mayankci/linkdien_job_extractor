# %%
# %%
import pandas as pd
import requests
import gspread as gs
from gspread_dataframe import set_with_dataframe
import time
import warnings


import gspread
from google.oauth2 import service_account
import gspread_dataframe as gd
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
warnings.filterwarnings('ignore')

sheet_creds = r"E:\Naukri\your_cred.json"

def gs_reader(sheet_name,col,sheet_url,skiprows):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(sheet_creds,scope)
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\LENOVO\Downloads\hasan_credentials.json',scope)
    gc = gspread.authorize(credentials)
    sht2 = gc.open_by_url(sheet_url)
    sht = sht2.worksheet(sheet_name)
    if col == 0:
        c = get_as_dataframe(sht,evaluate_formulas = True,skiprows=skiprows)
        return c
    else:
        c = get_as_dataframe(sht,use_cols = col,evaluate_formulas = True,skiprows=skiprows)
        return c
def gs_writer(sheet_name, dataframe, sheet_url, row=1, col=1, include_column_header=True, ):
    check_flag = True
    resize = False
    ct = 0
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(sheet_creds,scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_url(sheet_url)
    ws_list = list(map(lambda x: x.title, sh.worksheets()))
    # print(ws_list)
    # print(sheet_name)
    if sheet_name in ws_list:
        sht = sh.worksheet(sheet_name)
        while check_flag or ct < 12:
            try:
                # print(ct)
                set_with_dataframe(
                    sht, dataframe, resize=resize, row=row, col=col, include_column_header=include_column_header
                )
                print(sheet_name, 'data pushed to sheet')
                return
            except Exception as e:
                if ct > 10:
                    raise Exception(str(e))
                time.sleep(10)
                ct +=1
                continue

    else:
        sht = sh.add_worksheet(title=sheet_name, rows=dataframe.shape[0], cols=dataframe.shape[1])
        set_with_dataframe(
            sht, dataframe, resize=False, row=row, col=1, include_column_header=include_column_header
        )
        print(sheet_name, 'data pushed to sheet')
        
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import  ChromeDriverManager
from bs4 import BeautifulSoup
import pyautogui
import time
from datetime import datetime
import pyautogui
import time

# for _ in range(9):
#     pyautogui.hotkey('ctrl', 'h')  # Corrected lowercase 'ctrl'
#     time.sleep(0.5)  # Pause for better recognition
# time.sleep(10)
# print("DONE")


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D4167547939%26distance%3D25.0%26f_TPR%3Dr86400%26geoId%3D102713980%26keywords%3Dwe%2520are%2520hiring%2520analyst%26origin%3DJOB_SEARCH_PAGE_JOB_FILTER&trk=public_jobs_nav-header-signin")
driver.maximize_window()


email_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "username")) 
).send_keys("Your_email")


password_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "password")) 
).send_keys("Your_Pass")


sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
).click()




time.sleep(2)  



for _ in range(9):
    pyautogui.hotkey('ctrl', '-')  
    

job_data = [] 
page_count = 2 
while page_count < 5: 
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width // 2.3, screen_height // 2, duration=1) 
    for _ in range(5):  
        pyautogui.scroll(-500)
    
    job_cards = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-list__entity-lockup"))
    )
    job_cards = driver.find_elements(By.CLASS_NAME, "job-card-list__entity-lockup")
    print(f"Found {len(job_cards)} job cards.")

    for index, job_card in enumerate(job_cards):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", job_card)
            time.sleep(1)
            job_card.click()
            time.sleep(3)  


            job_title = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "job-details-jobs-unified-top-card__job-title"))
            ).text.strip()
            job_desc = driver.find_element(By.CLASS_NAME, "job-details-jobs-unified-top-card__primary-description-container").text.strip()
            job_link = driver.current_url
            job_data.append({"Job Title": job_title, "Description": job_desc, "Job Link": job_link})


        except Exception as e:
            print(f"⚠️ Error scraping Job {index + 1}: {e}")
       
    page_one_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//button[@aria-label='Page {page_count}']"))
    )
    page_one_button.click()
    print("Page No",page_count)
    time.sleep(5)  
    page_count += 1  
        

df = pd.DataFrame(job_data)
driver.quit()


df['location'] = df['Description'].str.split(" · ").str[0]
df['time'] = (df['Description'].str.split(" · ").str[1]).astype(str) + " " + str(datetime.now().date()) + " " + str(datetime.now().time()).split('.')[0]
df['Click'] = df['Description'].str.split(" · ").str[2]
df['Click_Count'] = df['Click'].str.extract(r'(\d+)').fillna(0).astype(int)
df = df.sort_values(by='Click_Count')
final = df[df['Job Title'].str.contains('Analyst|analyst|Data|Scientist|Science')]
final = final[['Job Title', 'Job Link', 'location', 'time','Click_Count']]

gs_writer(f"Linkedin_{datetime.now().date()}",final,"Your_sheet_link")



