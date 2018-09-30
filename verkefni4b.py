import json
from bottle import route, run , template
import requests

main_api = "http://apis.is/currency/lb"

def GetInfo():
    url = main_api
    json_data = requests.get(url).json()
    return json_data

print(GetInfo())

gogn=GetInfo()
 
mydict={"Shortname":["value","askValue","bidValue","changeCur","changePer"]}

for r in range(19):
    lina=gogn["results"][r]
    value=str(round(lina["value"],2))
    mydict.update({lina["shortName"]:[value,lina["changeCur"],lina["changePer"]]})

fjöldi = 3



@route('/')
def serve_homepage():
    return template('disp_table',rows = mydict, cases = fjöldi)

run(host="localhost", port=8080, debug=True)

