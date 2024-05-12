#Import Necessary Pacakages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
import time
import pandas as pd

#Data Columns for CSV file
columns = ["Assists_Position", "NAME", "TEAM", "ASSISTS", "GAMES", "ASSISTS PER MATCH"]

# Function for extract player details
def get_players_details(row):
    details = row.text.split("\n")
    print(details)
    contents = {}
    contents['Assists_Position']=   details[0]
    contents['NAME'] =              details[1]
    contents['TEAM'] =              details[2]
    contents['ASSISTS'] =           details[3]
    contents['GAMES'] =             details[4]
    contents['ASSISTS PER MATCH'] = details[5]
    
    return contents

#Main function to Scrape Data
def main():

    player_data=[]

    for page_id in range(1,37):

        driver=webdriver.Edge()
        url=f"https://www.laliga.com/en-GB/stats/laliga-easports/assists/page/{page_id}"
        driver.get(url)
        time.sleep(10)
        table = driver.find_element(By.TAG_NAME, 'tbody')
        rows=table.find_elements(By.TAG_NAME,"tr")

        for idx,row in enumerate(rows):
                player_data.append(get_players_details(row))

               
    driver.close()

    print(len(player_data))
    
    #CSV file creation with data
    df = pd.DataFrame(data=player_data, columns=columns)
    df.to_csv("Laliga Player Assists.csv", index=False)
    return

    
    
if __name__ == "__main__":
    main()