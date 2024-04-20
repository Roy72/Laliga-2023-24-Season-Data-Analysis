# Laliga-2023-24-Season-Data-Analysis

## Problem Satement
The goal is to analysis the 

##Build From Sources

1.Clone the repo
```bash
git clone https://github.com/Roy72/Laliga-2023-24-Season-Data-Analysis.git
```
2. Initialize and activate virtual environment (for windows)
```bash
virtualenv --no-site-packages venv
source venv/bin/activate
```
3.Install dependencies
```bash
pip install -r requiremnets.txt
```
4.Download Chrome webdriver from : https://chromedriver.chromium.org/downloads

5. Run the scarper
 ---> Laliga Player Data Analysis
 ```bash
python Laliga Player Data Analysis/Laliga_player_score.py
python Laliga Player Data Analysis/Laliga_player_assists.py
python Laliga Player Data Analysis/Laliga_player_passes.py
```
--->Laliga Team Data Analysis
```bash
python Laliga Team Data Analysis/Laliga_Team_performance.py
python Laliga Team Data Analysis/Laliga_Team_Standings.py
```
6.You will get file name
---> Laliga Player Data Analysis
`Laliga Player Scores.csv` , `Laliga Player Assists.csv` & `Laliga Player Passes.csv` containing all the required fields.
---> Laliga Team Data Analysis
`Laliga Team Performance.csv` & `Laliga Team Standings.csv`

7. From `Laliga Player Data Analysis` you will get a ipynb file that merges 3 csv files together on basis of Player name and Team Name and create another csv file.
```bash
python Laliga Team Data Analysis/Laliga_player_data_merge.ipynb
```
csv file name ---> `Laliga_stat_dataframe.csv`

##Analytics

Tableau public view for `Laliga Player Data Analysis` : https://public.tableau.com/app/profile/anik.roy4166/viz/LALIGAPLAYERDATAANALYSIS2023-2430MATCH/Dashboard1

Tableau public view for `Laliga Team Data Analysis` :   https://public.tableau.com/app/profile/anik.roy4166/viz/LALIGATEAMPERFORMANCEDATAANALYSIS2023-202430MATCH/Dashboard1
