from itertools import combinations

# this is a Pokedex dictionary
pokedex = {
    'Pikachu': ('Electric',),
    'Charizard': ('Fire', 'Flying'),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),  
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

def strongest_team(pokedex, k):
    max_types = 0
    best_teams = []

    # Try all possible combinations of k pokemons
    for team in combinations(pokedex.keys(), k):
        combined_types = set()
        for pokemon in team:
            combined_types.update(pokedex[pokemon])
        
        # Count distinct types
        type_count = len(combined_types)

        # Update strongest team
        if type_count > max_types:
            max_types = type_count
            best_teams = [(team, combined_types)]
        elif type_count == max_types:
            best_teams.append((team, combined_types))
    
    return best_teams, max_types


# Example run
k = 3
teams, max_types = strongest_team(pokedex, k)

print(f"Strongest teams with {max_types} types:")
for team, types in teams:
    print(f"Team: {team}, Types: {types}")
