import requests

url = 'https://mstdn.social/api/v1/accounts/305125/statuses'

r = requests.get(url)

status_update = r.json()

for entry in status_update:
    print(entry['content'])