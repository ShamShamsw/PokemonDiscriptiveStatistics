import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('Dataset/PokemonStats.xlsx')

# Basic Descriptive Statistics
print(df.describe())

# Correlation Matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Group by type1 and calculate mean for some columns
type_groups = df.groupby('type1').mean()[['attack', 'defense', 'hp']]
print(type_groups)

# Histogram for attack stat
sns.histplot(df['attack'], kde=True)
plt.title('Distribution of Attack Stat')
plt.show()

# Boxplot for defense stat
sns.boxplot(x=df['defense'])
plt.title('Boxplot of Defense Stat')
plt.show()

# Comparing Legendary vs Non-Legendary Pokémon
legendary_comparison = df.groupby('is_legendary').mean()[['attack', 'defense', 'hp']]
print(legendary_comparison)
