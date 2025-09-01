from itertools import combinations

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


    for team in combinations(pokedex.keys(), k):
        combined_types = set()
        for pokemon in team:
            combined_types.update(pokedex[pokemon])
        
    
        type_count = len(combined_types)

        
        if type_count > max_types:
            max_types = type_count
            best_teams = [(team, combined_types)]
        elif type_count == max_types:
            best_teams.append((team, combined_types))
    
    return best_teams, max_types



k = 3
teams, max_types = strongest_team(pokedex, k)

print(f"Strongest teams with {max_types} types:")
for team, types in teams:
    print(f"Team: {team}, Types: {types}")
