from locale import D_FMT
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(START_URL)

temp_list=[]
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find_all('table')
table_rows=star_table[5].find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
#print(temp_list)

star_name=[]
star_distance=[]
star_mass=[]
star_radius=[]
for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    star_distance.append(temp_list[i][5])
    star_mass.append(temp_list[i][7])
    star_radius.append(temp_list[i][8])

df=pd.DataFrame(list(zip(star_name,star_distance,star_mass,star_radius)),columns=['name','distance','mass','radius'])
df.to_csv('project2_output.csv')

