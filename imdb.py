
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import codecs

import re

from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.imdb.com/what-to-watch/fan-favorites/?ref_=hm_fanfav_sm'

driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Find all the movie titles
movie_titles = driver.find_elements(By.XPATH, "//span[@data-testid='title']")
movie_reviews = driver.find_elements(By.CLASS_NAME,"ipc-rating-star-group ipc-poster-card__rating-star-group sc-a885001d-0 kzmDax")

# Extract and print the titles
for title in movie_titles:
    print(title.text)
# print(movie_titles)
    
with open('movie_titles.txt', 'w') as file:
    for title in movie_titles:
        file.write(title.text + '\n')



# Close the browser
driver.quit()

