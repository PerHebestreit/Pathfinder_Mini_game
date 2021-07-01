import random
import json


maps = ['Ruins 1', 'Arena 1', 'Stones 1', 'Bridge 1', 'Camp 1', 'Ruins 2', 'Canyon 1', 'Swamp 1', 'Ruins 3']
pc_level = int(input('PC level: '))
party_size = int(input('Party size: '))
toggle_weakness = input("Toggle Weakened Mob's: ").lower()
toggle_elite = input("Toggle Elite Mob's: ").lower()
toggle_Hazards = input("Toggle Hazard's?: ").lower()
environment = ""
width = 0
height = 0
terminate = ''
total_exp = int(input("Current party exp: "))
total_pc_gp = 0
total_party_gp = 0

income = {
    1: 175,
    2: 300,
    3: 500,
    4: 850,
    5: 1350,
    6: 2000,
    7: 2900,
    8: 4000,
    9: 5700,
    10: 8000,
    11: 11500,
    12: 16500,
    13: 25000,
    14: 36500,
    15: 54500,
    16: 82500,
    17: 128000,
    18: 208000,
    19: 355000,
    20: 490000
}

def getEncounterDifficulty(threat_level):
    
    if threat_level == 'trivial':
        exp_budget = 10 * party_size
        exp_reward = 40
    elif threat_level == 'low':
        exp_budget = 15 * party_size
        exp_reward = 60
    elif threat_level == 'moderate':
        exp_budget = 20 * party_size
        exp_reward = 80
    elif threat_level == 'severe':
        exp_budget = 30 * party_size
        exp_reward = 120
    elif threat_level == 'extreme':
        exp_budget = 40 * party_size
        exp_reward = 160

    return exp_budget, exp_reward

def getMonster(monster_Level, list = "monsters"):
     with open("Monsters.json", "r") as m:
            jFile = json.load(m)
            allMonsters = jFile[list]
            return random.choice(allMonsters[str(monster_Level)])

def get_exp(npc_levels, pc_levels):
    if npc_levels == pc_levels:
        return 40
    elif npc_levels == pc_levels + 1:
        return 60
    elif npc_levels == pc_levels + 2:
        return 80
    elif npc_levels == pc_levels + 3:
        return 120
    elif npc_levels == pc_levels + 4:
        return 160
    elif npc_levels == pc_levels - 1:
        return 30
    elif npc_levels == pc_levels - 2:
        return 20
    elif npc_levels == pc_levels - 3:
        return 15
    elif npc_levels == pc_levels - 4:
        return 10
    else:
        print('error')

def setMapDimensions():
    global height, width
    global environment

    environment = random.choice(maps)

    if environment == 'Ruins 1':
        height = 34
        width = 24
    elif environment == 'Arena 1':
        height = 15
        width = 15
    elif environment == 'Stones 1':
        height = 34
        width = 34
    elif environment == 'Bridge 1':
        height = 34
        width = 34
    elif environment == 'Camp 1':
        height = 44
        width = 30
    elif environment == 'Ruins 2':
        height = 38
        width = 24
    elif environment == 'Canyon 1':
        height = 34
        width = 34
    elif environment == 'Swamp 1':
        height = 69
        width = 23
    elif environment == 'Ruins 3':
        height = 49
        width = 31

while terminate != 'yes' and total_exp <= 1000:
    total_mob = []
    encounter_exp = 0
    exp_budget = 0
    exp_reward = 0
    npc_level = 0
    happiness = ''
    threat_level = ''
    random_choice = ['trivial', 'low', 'moderate', 'severe', 'extreme']
    
    while exp_budget == 0:

        threat_level = input('Threat: ').lower()

        if threat_level == 'random':
            threat_level = random.choice(random_choice)
            exp_budget,exp_reward = getEncounterDifficulty(threat_level)
        elif threat_level in random_choice:
            exp_budget,exp_reward = getEncounterDifficulty(threat_level)
        else:   
            print('''Choose between:
Trivial
Low
Moderate
Severe
Extreme
or Random''')
    
    while encounter_exp != exp_budget:
        npc_level = random.randint(pc_level - 4, pc_level + 4)
        temp = get_exp(npc_level, pc_level)
        if temp + encounter_exp <= exp_budget:
            total_mob.append(npc_level)
            encounter_exp += temp
        if encounter_exp == exp_budget - 5:
            encounter_exp = 0
            total_mob = []

    setMapDimensions()   
    print(f'Environment: {environment}')
    
    while happiness != 'yes':
        monster_group = []
        for mob in total_mob:
            mod = random.randint(1, 100)
            if 24 <= mob <= -2 or mod <= 5 and toggle_weakness == 'yes':
                if mob <= 3:
                    temp_monster = getMonster(mob + 2)
                else:
                    temp_monster = getMonster(mob + 1)
                temp_monster = 'Weakened ' + temp_monster
            elif mod >= 95 and mob >= 1 and toggle_elite == 'yes':
                if mob <= 3:
                    temp_monster = getMonster(mob - 2)
                else:
                    temp_monster = getMonster(mob - 1)
                temp_monster = 'Elite ' + temp_monster
            else:
                if toggle_Hazards == 'yes' and 90 <= mod <= 95 and mob != 20 and mob != 22 and mob <= 23:
                    temp_monster = getMonster(mob, "hazards")
                else:
                    temp_monster = getMonster(mob)
            monster_group.append(temp_monster)
        for enemies in monster_group:
            print(f'{enemies} | Spawning: W:{random.randint(1, width)} H:{random.randint(1, height)}')
        happiness = input("Happy with these Mob's?: ").lower()
    
    value = (income[pc_level] / 4) / 1000
    pc_gp_reward = value * exp_reward
    party_gp_reward = pc_gp_reward * party_size
    print(f'Difficulty: {threat_level}, exp reward: {exp_reward}')
    print(f'Player Gp reward: {pc_gp_reward}')
    print(f'Party GP reward: {party_gp_reward}')
    total_party_gp += party_gp_reward
    total_pc_gp += pc_gp_reward
    total_exp += exp_reward
    terminate = input("Done?: ")

print(f'Total exp so far: {total_exp}')
print(f'Total Gp PC: {total_pc_gp}')
print(f'Total Gp Party: {total_party_gp}')
