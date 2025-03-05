import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'Dataset/pokemon.xlsx'
df = pd.read_excel(file_path)

# Define the categories
categories = ['attack', 'defense', 'sp_attack', 'sp_defense', 'speed']

# Function to get top 5 Pokémon in each category
def get_top_five(df, category):
    return df[['name', category]].sort_values(by=category, ascending=False).head(5)

# Function to get the stats of a Pokémon
def get_pokemon_rank(df, pokemon_name, categories):
    pokemon_name = pokemon_name.title()  # Capitalizes first letter of each word
    
    if pokemon_name not in df['Name'].values:
        print(f"Pokémon '{pokemon_name}' not found in the dataset.")
        return
    
    print(f"\nRanks for {pokemon_name} in different categories:")
    for category in categories:
        df_sorted = df[['Name', category]].sort_values(by=category, ascending=False).reset_index(drop=True)
        rank = df_sorted[df_sorted['Name'] == pokemon_name].index[0] + 1  # +1 for 1-based ranking
        stat_value = df_sorted[df_sorted['Name'] == pokemon_name][category].values[0]
        print(f"{category}: Rank {rank} (Stat: {stat_value})")

# Plot bar graphs for the top 5 Pokémon in each category
for category in categories:
    top_five = get_top_five(df, category)
    plt.figure(figsize=(10, 6))
    plt.bar(top_five['name'], top_five[category], color='skyblue')
    plt.xlabel('Pokémon')
    plt.ylabel(category.capitalize())
    plt.title(f'Top 5 Pokémon in {category.capitalize()}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Take user input and display stats
while True:
    pokemon_name = input("Enter the name of a Pokémon (or 'exit' to quit): ").strip().title()  # Format input
    if pokemon_name.lower() == 'Exit':  # Checking lowercase to match 'exit' exactly
        break
    get_pokemon_rank(df, pokemon_name, categories)

# Display the DataFrame
print(df)