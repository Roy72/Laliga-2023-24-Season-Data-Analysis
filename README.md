# Laliga-2023-24-Season-Data-Analysis
## Data Overviwe
Here laliga resgistered 705 individual players data and 20 teams data has been scrapped from [Laliga Official Website](https://www.laliga.com/en-GB/stats/laliga-easports/scorers)<br/> 

## Problem Satement
The goal is to analysis the Laliga 2023-24 Season Data after 30 matches. From [Laliga Official Website](https://www.laliga.com/en-GB/stats/laliga-easports/scorers) <br/> scraped all the registered player `Scores`, `Assists` & `Passes`  to analyze the `Laliga Player Data Analysis` . Secondly,from [Team Data](https://www.laliga.com/en-GB/stats/laliga-easports/team)<br/>  `Team` data and from [Standings](https://www.laliga.com/en-GB/laliga-easports/standing)<br/> `Team standings` are scraped for `Laliga Team Data Analysis`.

Afterwards we utlized the `Laliga Player Data Analysis` to understand the following [visualization](https://public.tableau.com/app/profile/anik.roy4166/viz/LALIGATEAMPERFORMANCEDATAANALYSIS2023-2024_30MATCH/Home)<br/>
1. Barchart of showing  player and aggregated by their team goals, assits & passes.
2. Relationship btween Team  total Goal Scored and Assists. 
3. Pie chart of total goal percentages from each team.
4. Boxplot of Goal Scored , Assists and Passes from each team. It shows the data distribution.
5. Barchart of Goal and assists per match regading per team accumulate with individual players.

And we utilized the `Laliga Team Data Analysis` to understand the following [visualization]()<br/> 
1. Barchart of Team Points.
2. Relationship between Red cards and yellow cards of all the team using scatter plot.
3. Histogram of Team points.
4. basic exploration of Team goal scored , goal accumulate and goal difference.
5. Relatioship between Shots on target and Goals Scored.
6. Pie Chart of Foul percentages of each team.
   
## Data Findings Overall from two the Tableau [HOME](https://public.tableau.com/app/profile/anik.roy4166/viz/LALIGATEAMPERFORMANCEDATAANALYSIS2023-2024_30MATCH/Home)<br/>
Real madrid have the higher goal score , assists and goal difference. The have the high potential to win the Laliga this 2023-24 seasons. Getafe has the most number of foules comitted (6.5%) and also got higher number of red and yellow cards among 20 teams.

## Build From Sources

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
4.[Download Microsoft Edge Webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads) <br/>

5. Run the scarper
 ---> Laliga Player Data Analysis
 ```bash
scrapers/players_scrapers/Laliga_player_score.py
scrapers/players_scrapers/Laliga_player_assists.py
scrapers/players_scrapers/Laliga_player_passes.py
```
--->Laliga Team Data Analysis
```bash
scrapers/team_scrapers/Laliga_Team_performance.py
scrapers/team_scrapers/Laliga_Team_Standings.py
```
6.You will get file name
---> Laliga Player Data Analysis
`Laliga Player Scores.csv` , `Laliga Player Assists.csv` & `Laliga Player Passes.csv` containing in 
```bash
data/player_data
```
---> Laliga Team Data Analysis
`Laliga Team Performance.csv` & `Laliga Team Standings.csv` containing in
```bash
data/team_data
```
7. You will get a ipynb file that named `merge_player_data.ipynb` which merges 3 csv files `laliga_player_assists.csv`,`laliga_player_passes.csv` & `laliga_player_scores.csv` together on basis of Player name and Team Name and create another csv file.
csv file name ---> `merged_player_data.csv`

