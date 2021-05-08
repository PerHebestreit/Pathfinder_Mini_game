import random

temp_choice = ['trivial', 'low', 'moderate', 'severe', 'extreme']
encounter_exp = 0
min_pool = 0
max_pool = 0
total_mob = []
pc_level = int(input('PC level: '))
party_size = int(input('Party size: '))
threat_level = ''

while max_pool == 0:
    threat_level = input('Threat: ').lower()
    if threat_level == 'trivial':
        max_pool = 10 * party_size
    elif threat_level == 'low':
        min_pool = 40
        max_pool = 60
    elif threat_level == 'moderate':
        min_pool = 60
        max_pool = 80
    elif threat_level == 'severe':
        min_pool = 80
        max_pool = 120
    elif threat_level == 'extreme':
        min_pool = 120
        max_pool = 160
    elif threat_level == 'random':
        threat_level = random.choice(temp_choice)
        if threat_level == 'trivial':
            min_pool = 10
            max_pool = 40
        elif threat_level == 'low':
            min_pool = 40
            max_pool = 60
        elif threat_level == 'moderate':
            min_pool = 60
            max_pool = 80
        elif threat_level == 'severe':
            min_pool = 80
            max_pool = 120
        elif threat_level == 'extreme':
            min_pool = 120
            max_pool = 160
    else:
        print('error')
        print('''Choose between:
Trivial
Low
Moderate
Severe
Extreme
or Random''')

print(max_pool)