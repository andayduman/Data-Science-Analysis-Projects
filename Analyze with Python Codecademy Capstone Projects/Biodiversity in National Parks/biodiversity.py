from matplotlib import pyplot as plt
import pandas as pd
from scipy.stats import chi2_contingency

#data from csv files used in analysis contain mock data based on real data from National Parks Service in USA

species = pd.read_csv('species_info.csv') 
#loading in csv file containing info on species found within parks
species.head()

species.scientific_name.nunique() 
#calculating number of species in dataset: 5541 species

species.category.unique() 
#determining the different categories of species in dataset: Mammal, Bird, Reptile, Amphibian, Fish, Vascular Plant, Nonvascular plant

species.conservation_status.unique()
#determing differet values in conservation_status column: nan, Species of Concern, Endangered, Threatened, In Recovery

species.groupby('conservation_status').scientific_name.nunique().reset_index()
#creating table to group each unique scientific_name (species) category within the different conservation statuses

species.fillna('No Intervention', inplace=True)
#replacing 'None' with 'No Intervention'

species.groupby('conservation_status').scientific_name.nunique().reset_index()
#creating table from species dataframe listing the different conservation statuses and how many unique scientific names (species) are categorized in each status

protection_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index().sort_values(by='scientific_name')

plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(scientific_name)), protection_counts.conservation_status.values)
ax.set_xticks(range(len(protection_counts))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.xlabel('Status of species')
plt.ylabel('Number of species')
plt.title('Conservation Status by Species')
plt.show()

species['is_protected'] = species.conservation_status != 'No Intervention'

category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()
category_counts.head(10)

category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()

category_pivot.columns = ['category', 'not_protected', 'protected']
              
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)
category_pivot.head(10)

contingency = [[30, 146], [75, 413]]
chi2_contingency(contingency)

contingency2 = [[5, 73], [30, 146]]
chi2_contingency(contingency2)

observations = pd.read_csv('observations.csv')
observations.head(6)

species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
species.head()
              
species[species.is_sheep]
              
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
              
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
              
sheep_observations = observations.merge(sheep_species)

sheep_obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
sheep_obs_by_park.head()

plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(sheep_obs_by_park)),sheep_obs_by_park.observations.values)
ax.set_xticks(range(len(sheep_obs_by_park)))
ax.set_xticklabels(sheep_obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()
