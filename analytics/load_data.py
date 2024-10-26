# insert_data.py

import requests
import random
import string

def generate_user_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_action():
    actions = ['login', 'view', 'click', 'purchase', 'logout']
    return random.choice(actions)

url = 'http://localhost:8000/record/'  # Update to your server's URL if deployed

# Insert 1000 entries
for _ in range(1000):
    data = {
        'user_id': generate_user_id(),
        'action': generate_action()
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Data recorded successfully")
    else:
        print("Failed to record data", response.json())
