import json
import time
import re
import pandas as Pd
from pandas import json_normalize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Initialize the chrome Webdriver
driver = webdriver.Chrome(options=options)

#Search term to look for.
keyword = "property+managment+companies"

#Open the webpage
driver.get(f'https://www.google.com/maps/search/{keyword}+in+London,+UK/')

Wait = WebDriverWait(driver, 180)

#loca
scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')

#set a pause time between scrolls
scroll_pause_time = 15

# Get the height of the scrollable element
last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)

while True:
    #scroll down within the element
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    
    #wait for the elemen to load more content
    time.sleep(scroll_pause_time)
    
    # Calculate the new scroll height and compare with the last scroll height
    new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
    if new_height == last_height:
        break
    last_height = new_height
    
items = driver.find_elements(By.CSS_SELECTOR, 'div[role="feed"] > div > div[jsaction]')

#scraping the leads 
leads = []
for item in items:
    data = {}
    
    try:
        data['title'] = item.find_element(By.CSS_SELECTOR, ".fontHeadlineSmall").text
    except Exception:
        pass
    
    try:
        data['link'] = item.find_element(By.CSS_SELECTOR, 'div[role="feed"] > div > div[jsaction] div > a').get_attribute('href')
    except Exception:
      pass
  
    try:
        rating_text = item.find_element(By.CSS_SELECTOR, '.fontBodyMedium > span[role="img"]').get_attribute('aria-label')
        rating_numbers = [float(piece.replace(",", ".")) for piece in rating_text.split(" ") if piece.replace(",", ".").replace(".", "", 1).isdigit()]

        if rating_numbers:
           data['stars'] = rating_numbers[0]
           data['reviews'] = int(rating_numbers[1]) if len(rating_numbers) > 1 else 0
    except Exception:
      pass
  
    try:
      text_content = item.text
      phone_pattern = r'((\+?\d{1,2}[ -]?)?(\(?\d{3}\)?[ -]?\d{3,4}[ -]?\d{4}|\(?\d{2,3}\)?[ -]?\d{2,3}[ -]?\d{2,3}[ -]?\d{2,3}))'
      matches = re.findall(phone_pattern, text_content)

      phone_numbers = [match[0] for match in matches]
      unique_phone_numbers = list(set(phone_numbers))

      data['phone'] = unique_phone_numbers[0] if unique_phone_numbers else None   
    except Exception:
        pass

    if(data.get('stars', 'reviews' )):
        leads.append(data)
                
    with open('leads.json', 'w') as f:
       json.dump(leads, f, indent=2)

#converting the json file into a dataframe
df = Pd.read_json('leads.json')

# save the Dataframe as a CSV file
df.to_csv('leads.csv', index=False)