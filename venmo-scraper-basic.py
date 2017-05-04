# coding - utf-8
import requests
import json
from datetime import datetime
import csv
import time
import pprint

API_ENDPOINT = 'https://venmo.com/api/v5/public'
url = API_ENDPOINT
resp = requests.get(url)
json = resp.json()
data = json['data']

venmo_payments = []

for d in data:
    payment = {}
    payment['id'] = d['payment_id']
    payment['actor_firstname'] = d['actor']['firstname']
    payment['actor_lastname'] = d['actor']['lastname']
    payment['actor_name'] = d['actor']['name']
    payment['actor_dateprofcreated'] = d['actor']['date_created']
    payment['actor_isBusiness'] = d['actor']['is_business']
    payment['transanction_message'] = d['message']
    payment['comments'] = d['comments']
    payment['transaction_datecreated'] = d['created_time']
    payment['transaction_target'] = d['transactions'][0]['target']['name']
    payment['transaction_target_profcreated'] = d['transactions'][0]['target']['date_created']
    payment['type'] = d['type']
    payment['updated_time'] = d['updated_time']

    venmo_payments.append(payment)

pprint.pprint(venmo_payments)
