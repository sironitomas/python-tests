#!/usr/bin/python
# pylint: disable=I0011,C0103,C0111
__author__ = "Tomás Sironi"
__email__ = "sironitomas@gmail.com"
__license__ = "GPL"
__version__ = "1.0.0"

import json
import random

try:
    with open('user.json') as data:
        user = json.load(data)
    with open('campaigns.json') as data:
        campaigns = json.load(data)
except FileNotFoundError:
    exit('Json file not found')
except ValueError:
    exit('Json file is invalid')

del data

# First priority candidates list.
candid_A = []
# Second priority candidates list.
candid_B = []

# The following loop will filter out campaigns which don't comply with the user data.
# Also, the campaigns will be prioritized based on the type of connection
# because it's the only field that I consider flexible.

for camp in campaigns:
    if camp['gender'] != 'All':
        if camp['gender'] != user['gender']:
            continue

    if camp['min_age'] != None:
        if camp['min_age'] > user['age']:
            continue

    if camp['max_age'] != None:
        if camp['max_age'] < user['age']:
            continue

    if camp['platform'] != user['platform']:
        continue

    if camp['connection'] != 'All':
        if camp['connection'] != user['connection']:
            candid_B.append(camp)
            continue

    candid_A.append(camp)

# Select a random campaign from candid_A.
# If candid_A is empty, select one from candid_B.

if len(candid_A) > 0:
    i = random.randint(0, len(candid_A) - 1)
    final = candid_A[i]
    print(json.dumps(final, indent=4, sort_keys=True))

elif len(candid_B) > 0:
    i = random.randint(0, len(candid_B) - 1)
    final = candid_B[i]
    print(json.dumps(final, indent=4, sort_keys=True))

else:
    print('No campaings found for the user')
    exit(1)
