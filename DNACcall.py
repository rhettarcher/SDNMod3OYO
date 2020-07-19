
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

#Defines username, password, and URL for auth token
USER = "devnetuser"
PASS = "Cisco123!"
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"



#This code was taken from getDevices.py which was included in Module3
#it was edited to change variables
Wampas = {'Content-Type': 'application/json'}

sith = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=Wampas, verify=False)

token = sith.json()['Token']

print("Your generated token is: " + token)

Jedi = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-health"

getWampa = {'Accept': 'application/json', 'X-auth-token': token}

getSith = requests.get(Jedi, headers=getWampa, verify=False)

forceJSON = getSith.json()

pprint(forceJSON)

#Script pulls Network Health data from DNAC API