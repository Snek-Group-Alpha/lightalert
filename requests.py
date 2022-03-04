import requests, os

password = os.getenv('LIGHT_PASS')
user = os.getenv('LIGHT_USER')
url = os.getenv('OBSV_URL')

url = f'https://{user}:{password}@{url}/api/alerting/rules/_find?search_fields=name'


resp = requests.get(url=url)
data = resp.json()

count = 0
for alert in data['data']:
    print(alert['execution_status']['status'])
    if alert['execution_status']['status'] == "Error":
        count += 1

print (count)
