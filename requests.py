import requests, os

password = os.getenv('light_pass')
user = os.getenv('light_user')
url = os.getenv('obs_url')

url = 'https://'+user+':'+password+'@'+url+'/api/alerting/rules/_find?search_fields=name'


resp = requests.get(url=url)
data = resp.json()

count = 0
for alert in data['data']:
    print(alert['execution_status']['status'])
    if alert['execution_status']['status'] == "Error":
        count += 1

print (count)
