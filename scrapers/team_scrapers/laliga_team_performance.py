#Import Necessary Pacakages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
import time
import pandas as pd

#Data Columns for CSV file
columns = ["Team POSITION", "TEAM", "GOALS SCORED", "GOALS CONCEDED", "SHOTS ON TRAGET", "FOULS", "YEELLOW_CARDS","RED CARDS"]

# Function for extract Team details
def get_team_details(row):
    details = row.text.split("\n")
    print(details)
    contents = {}
    contents["Team POSITION"]=        details[0]
    contents['TEAM'] =                details[1]
    contents['GOALS SCORED'] =        details[2]
    contents['GOALS CONCEDED'] =      details[3]
    contents['SHOTS ON TRAGET'] =     details[4]
    contents['FOULS'] =               details[5]
    contents['YEELLOW_CARDS'] =       details[6]
    contents['RED CARDS'] =           details[7]
    
    return contents

#Main function to Scrape Data
def main():

    team_data=[]

    driver=webdriver.Edge()
    url="https://www.laliga.com/en-GB/stats/laliga-easports/team"
    driver.get(url)
    time.sleep(10)
    table = driver.find_element(By.TAG_NAME, 'tbody')
    rows=table.find_elements(By.TAG_NAME,"tr")
    
    for idx,row in enumerate(rows):
        team_data.append(get_team_details(row))

               
    driver.close()

    print(len(team_data))
    
    #CSV file creation with data
    df = pd.DataFrame(data=team_data, columns=columns)
    df.to_csv("Laliga Team Performance.csv", index=False)
    return

    
    
if __name__ == "__main__":
    main()
