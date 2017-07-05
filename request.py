from requests import Request, Session
import urllib3
import json

s = Session()
headers = {'User-Agent': 'fake1.3.4'}
url = "https://10.70.82.204:9060/ers/config/endpoint"
headers={'Content-Type':'application/json','Accept':'application/json'}
req = Request('GET', url, auth=('ersadmin', 'BNbn1234'), headers=headers)
urllib3.disable_warnings()
prepped = req.prepare()
print prepped.body
print prepped.headers

resp = s.send(prepped, verify=False)
print resp.status_code
print resp.request.headers
print resp.text
