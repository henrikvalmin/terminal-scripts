import requests



def perform_attack(n):
   headers = {'x-api-user': "18733f50-7595-468b-a0e1-694d9534c7ea",
               'x-api-key': "bb64b369-64fd-400f-9566-72aea9f6fe63"}
  
   for i in range(n):
        req = requests.post(
            'https://habitica.com/api/v3/user/class/cast/smash?targetId=87aff353-8bb8-4da7-941e-8882d28bd148', 
            headers=headers
        )
    

def switch_equipment(isAttack):
    equipment_codes = []
    if isAttack:
        equipment_codes = ['weapon_warrior_6', 'shield_special_lootBag', 'armor_special_finnedOceanicArmor']
    else:
        equipment_codes = ['weapon_special_nomadsScimitar', 'shield_special_wintryMirror', 'armor_special_2']
    
    for item in equipment_codes:
        switch_to_item(item)

def switch_to_item(item_name):
    headers = {'x-api-user': "18733f50-7595-468b-a0e1-694d9534c7ea",
               'x-api-key': "bb64b369-64fd-400f-9566-72aea9f6fe63"}
    req = requests.post(
        'https://habitica.com/api/v3/user/equip/equipped/{}'.format(item_name), 
        headers=headers
    )

def attack(n):
    switch_equipment(True)
    
    #do the attack
    perform_attack(n)

    switch_equipment(False)



