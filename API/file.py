import requests
import _json

response = requests.get("https://api.stackexchange.com/docs/questions#order=desc&sort=activity&filter=default&site=stackoverflow&run=true")

for data in response.json()["items"];
print(data[title])