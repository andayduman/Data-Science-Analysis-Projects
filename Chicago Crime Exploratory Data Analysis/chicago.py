# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import bq_helper
from bq_helper import BigQueryHelper
chicago_crime = bq_helper.BigQueryHelper(active_project="bigquery-public-data",dataset_name="chicago_crime")
bq_assistant = BigQueryHelper("bigquery-public-data", "chicago_crime")
bq_assistant.list_tables()
bq_assistant.head('crime', num_rows=5)

#Do any of the entries have null values
query = '''select * from `bigquery-public-data.chicago_crime.crime`'''
df = bq_assistant.query_to_pandas(query) #none

bq_assistant.table_schema('crime')

query1 = '''select * from `bigquery-public-data.chicago_crime.crime` limit 1'''
bq_assistant.estimate_query_size(query1) #1.4GB
bq_assistant.query_to_pandas(query1)

query2 = '''select count(*) from `bigquery-public-data.chicago_crime.crime`'''
bq_assistant.query_to_pandas(query2) #7,177,384 entries in crime table

query3 = '''select max(date), min(date) from `bigquery-public-data.chicago_crime.crime`'''
bq_assistant.query_to_pandas(query3) #oldest date was January 1 2001 and most recent date was August 15 2020

query4 = '''select distinct block,  count(*) from `bigquery-public-data.chicago_crime.crime` group by block order by 2 desc'''
df = bq_assistant.query_to_pandas(query4)
print(df)
#Ohare St has had the most incident with 15698 followed by N. State St with 13843, S. Cicero Ave with 9640, N. Michigan Ave with 9036 and N. State St with 8441.
#These five blocks are among the safest/least dangerous blocks recorded in the data: W. Elmdale Ave, W. Catalpa Ave, N. Lakewood Ave, N. Sheridan Rd, N. Paulina St

import matplotlib.style as style 
style.available

query5 = '''select distinct block,  count(*) from `bigquery-public-data.chicago_crime.crime` group by block order by 2 desc limit 50'''
df2 = bq_assistant.query_to_pandas(query5)
df2.rename(columns={'block':'Street_Block', 'f0_':'Incident_Count'}, inplace=True)
#print(df2)
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import cm
plt.figure(figsize=(40,30))
sns.barplot(x='Street_Block', y='Incident_Count',data=df2, palette = "Reds_r")
plt.xticks(rotation=90, fontsize=20)
plt.yticks(fontsize=20)
plt.title('Top 50 Chicago Street Blocks with Highest Illegal Incident Count', fontsize=20)
plt.show()

query6 =  '''select distinct primary_type, description from `bigquery-public-data.chicago_crime.crime` where block ="100XX W OHARE ST" or block="001XX N STATE ST" or block = "076XX S CICERO AVE" or block="008XX N MICHIGAN AVE" or block="0000X W TERMINAL ST" '''
df3 = bq_assistant.query_to_pandas(query6)
print(df3)

query7 = '''select distinct primary_type as Type, count(description) as Count 
from `bigquery-public-data.chicago_crime.crime` 
where block ="100XX W OHARE ST" or block="001XX N STATE ST" or block = "076XX S CICERO AVE" or block="008XX N MICHIGAN AVE" or block="0000X W TERMINAL ST" 
group by primary_type order by 2 desc limit 50 '''
df4 = bq_assistant.query_to_pandas(query7)
print(df4)

print(((31480 + 4892 + 3967 + 3802 + 2752 + 1590 + 1264 + 1197 + 1015)/df4['Count'].sum()) * 100)

query8 = '''select distinct primary_type as Type, count(description) as Count 
from `bigquery-public-data.chicago_crime.crime` 
where block ="100XX W OHARE ST" or block="001XX N STATE ST" or block = "076XX S CICERO AVE" or block="008XX N MICHIGAN AVE" or block="0000X W TERMINAL ST" 
group by primary_type order by 2 desc limit 9'''
df5 = bq_assistant.query_to_pandas(query8)
#print(388 + 378 + 215 + 157 + 113 + 67 + 41 + 35 + 29 + 26 + 24 + 19 + 6 + 7 + 3 + 4 + 1) 1513 incidents among remaining categories
df6 = pd.DataFrame({'Type': ['Remaining 20 Categories'], 'Count': [1513]})
df7 = df5.append(df6, ignore_index=True)
#print(df7)
plt.figure(figsize=(20,20))
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5)
plt.pie(df7['Count'], labels=df7['Type'], data = df7, explode=explode, shadow=False, startangle = 360)
plt.title('Distribution of Incidents Occuring in Each Category', fontsize=20)
plt.show()

query9 = '''select distinct description, arrest, count(*) from `bigquery-public-data.chicago_crime.crime` where primary_type = "THEFT" group by description, arrest order by 2 desc, 3 desc'''
df9 = bq_assistant.query_to_pandas(query9)
df9['arrest'] = df9['arrest'].apply(lambda x: 'Arrest' if x == True else 'No Arrest')
print(df9)

retail_theft_pct = (107821 / (107821 + 75919)) * 100
print('Retail Theft Arrest Percentage: ' + str(retail_theft_pct) + '%' )
under_500_pct = (44814 / (44184 + 539646)) * 100
print('Theft of $500 and Under Arrest Percentage: ' + str(under_500_pct) + '%')
over_500_pct = (14176 / (357506 + 14176)) * 100
print('Theft of $500 and Over Arrest Percentage: ' + str(over_500_pct) + '%')
from_building_pct = (6225 / (236529 + 6225)) * 100
print('Theft from Building Arrest Percentage: ' + str(from_building_pct) + '%')
id_theft_pct = (758 / (758 + 43773)) * 100
print('Financial ID Theft Over $300 Arrest Percentage: ' + str(id_theft_pct) + '%')

f, ax = plt.subplots(figsize=(20, 15))
sns.set_style('whitegrid')
palettes = {'Arrest': 'Blues_r', 'No Arrest': 'Reds_r'}
plot = sns.barplot(data = df9, x='f0_', y='description', hue='arrest', orient='h', palette = 'Reds')
ax.legend(loc='upper right')
ax.set_xlabel('Number of Recorded Incidents', labelpad = 10, fontsize=15)
ax.set_ylabel('Types of Theft', labelpad = -20, fontsize=15)
plt.title("Graph of Arrest/No Arrest Ratio for Theft Incidents in Chicago's Highest Crime Populated Blocks ", fontsize=20)
plt.show()
