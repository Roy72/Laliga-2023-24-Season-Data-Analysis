#Import Necessary Pacakages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
import time
import pandas as pd

#Data Columns for CSV file
columns = ['Team POSITION', "TEAM", 'POINTS', 'PLAYED','WIN','DRAW','LOOSE','GOAL SCORED','GOAL ACCUMULATE','GOAL DIFFERENCE']

# Function for extract Team details
def get_team_details(row):
    details = row.text.split("\n")
    print(details)
    contents = {}
    contents["Team POSITION"]=        details[0]
    contents['TEAM'] =                details[1]
    contents['POINTS'] =              details[2]
    contents['PLAYED'] =              details[3]
    contents['WIN'] =                 details[4]
    contents['DRAW'] =                details[5]
    contents['LOOSE'] =               details[6]
    contents['GOAL SCORED'] =         details[7]
    contents['GOAL ACCUMULATE'] =     details[8]
    contents['GOAL DIFFERENCE'] =     details[9]


    
    return contents

#Main function to Scrape Data
def main():

    team_data=[]

    driver=webdriver.Edge()
    url="https://www.laliga.com/en-GB/laliga-easports/standing"
    driver.get(url)
    time.sleep(10)
    table = driver.find_element(By.CLASS_NAME, 'show')
    rows=table.find_elements(By.CLASS_NAME,"styled__ContainerAccordion-sc-e89col-11")
    
    for idx,row in enumerate(rows):
        team_data.append(get_team_details(row))

               
    driver.close()

    print(len(team_data))
    
    #CSV file creation with data
    df = pd.DataFrame(data=team_data, columns=columns)
    df.to_csv("Laliga Team Standings.csv", index=False)
    return

if __name__ == "__main__":
    main()
