import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = '/workspaces/PokemonDiscriptiveStatistics/Dataset/pokemon.xlsx'
df = pd.read_excel(file_path)

# Define the categories
categories = ['attack', 'defense', 'sp_attack', 'sp_defense', 'speed']

# Function to get top 5 Pokémon in each category
def get_top_five(df, category):
    return df[['Name', category]].sort_values(by=category, ascending=False).head(5)

# Function to get the stats of a Pokémon
def get_pokemon_stats(df, pokemon_name, categories):
    if pokemon_name not in df['Name'].values:
        print(f"Pokémon '{pokemon_name}' not found in the dataset.")
        return
    
    print(f"\nStats for {pokemon_name}:")
    pokemon_stats = df[df['Name'] == pokemon_name][categories].iloc[0]
    for category in categories:
        print(f"{category.capitalize()}: {pokemon_stats[category]}")

# Plot bar graphs for the top 5 Pokémon in each category
for category in categories:
    top_five = get_top_five(df, category)
    plt.figure(figsize=(10, 6))
    plt.bar(top_five['Name'], top_five[category], color='skyblue')
    plt.xlabel('Pokémon')
    plt.ylabel(category.capitalize())
    plt.title(f'Top 5 Pokémon in {category.capitalize()}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Take user input and display stats
while True:
    pokemon_name = input("Enter the name of a Pokémon (or 'exit' to quit): ").strip()
    if pokemon_name.lower() == 'exit':
        break
    get_pokemon_stats(df, pokemon_name, categories)

# Display the DataFrame
print(df)
