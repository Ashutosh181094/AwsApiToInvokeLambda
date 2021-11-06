import requests
import json

url="Your API URL"
payload={"Country":"India"}
result=requests.post(url,data=json.dumps(payload))
result.text
