import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency
from codecademySQL import sql_query
#this import allows for using SQL commands within a Python 3 file on Jupyter Notebook

#sample query using sql_query from codecademySQL library
sql_query('''
SELECT *
FROM visits
LIMIT 5
''')

#examining each table
sql_query('''SELECT * FROM visits LIMIT 10''')
sql_query('''SELECT * FROM fitness_tests LIMIT 5''')
sql_query('''SELECT * FROM applications LIMIT 5''')
sql_query('''SELECT * FROM purchases LIMIT 5''')

#creating large dataframe 'df' to combine all the data together using LEFT JOIN
df = sql_query('''
SELECT visits.first_name,
       visits.last_name,
       visits.visit_date,
       fitness_tests.fitness_test_date,
       applications.application_date,
       purchases.purchase_date
FROM visits
LEFT JOIN fitness_tests
    ON fitness_tests.first_name = visits.first_name
    AND fitness_tests.last_name = visits.last_name
    AND fitness_tests.email = visits.email
LEFT JOIN applications
    ON applications.first_name = visits.first_name
    AND applications.last_name = visits.last_name
    AND applications.email = visits.email
LEFT JOIN purchases
    ON purchases.first_name = visits.first_name
    AND purchases.last_name = visits.last_name
    AND purchases.email = visits.email
WHERE visits.visit_date >= '7-1-17'
''')

#adding new column to df dataframe called 'ab_test_group'
df['ab_test_group'] = df.fitness_test_date.apply(lambda x: 'A' if pd.notnull(x) else 'B') 

#creating new table 'ab_counts'
ab_counts = df.groupby('ab_test_group').first_name.count().reset_index()
ab_counts

#building pie cart of ab_counts information
plt.pie(ab_counts.first_name.values, labels=['A', 'B'], autopct='%0.2f%%')
plt.axis('equal')
plt.title('Pie Chart of ab_counts')
plt.savefig('ab_test_pie_chart.png')
plt.show()

#STEP 4: Who pick's up an application?
#new column in df called 'is_application' where if application_date column entry is not null, then is_application column value for entry is 'Application' else 'No Application'
df['is_application'] = df.application_date.apply(lambda x: 'Application' if pd.notnull(x) else 'No Application')

app_counts = df.groupby(['ab_test_group', 'is_application']).first_name.count().reset_index()
app_counts

#creating pivoted app_counts table called app_pivot
app_pivot = app_counts.pivot(columns='is_application', index='ab_test_group', values='first_name').reset_index()
app_pivot

#adding a new column to app_pivot called 'Total' combining a row's values in 'Application' and 'No Application' columns
app_pivot['Total'] = app_pivot.Application + app_pivot['No Application']

#adding a new column to app_pivot called 'Percent with Application' taking a row's value in 'Application' column and dividing it by the row's 'Total' value
app_pivot['Percent with Application'] = app_pivot.Application / app_pivot['Total']
app_pivot

#using chi squared test to determine that the fact that more gym participants in Group B turned in gym applications is statistically significant
contingency = [[250, 2254], [325, 2175]]
chi2_contingency(contingency)
#this is the output: (10.893961295282612, 0.0009647827600722304, 1,array([[ 287.72981615, 2216.27018385], [ 287.27018385, 2212.72981615]]))

#STEP 5: Who purchases a membership?
#of those who picked up an application, how many purchased a membership?

#creating new column in df called 'is_member' to identify which participants have a registered membership purchase_date
df['is_member'] = df.purchase_date.apply(lambda x: 'Member' if pd.notnull(x) else 'Not Member')

#creating new dataframe called 'just_apps' containing only individuals who picked up an application for a membership
just_apps = df[df.is_application == 'Application']

member_count = just_apps.groupby(['ab_test_group', 'is_member'])\
                 .first_name.count().reset_index()
member_pivot = member_count.pivot(columns='is_member',
                                  index='ab_test_group',
                                  values='first_name')\
                           .reset_index()

member_pivot['Total'] = member_pivot.Member + member_pivot['Not Member']
member_pivot['Percent Purchase'] = member_pivot.Member / member_pivot.Total
member_pivot

#performing another chi squared test
contingency = [[200, 50], [250, 75]]
chi2_contingency(contingency)
