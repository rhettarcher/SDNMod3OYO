"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list, then adds them to the Webex Teams Space

"""
import requests
from requests.auth import HTTPBasicAuth

addresses = []

more = input("Do you have an email address to enter (y/n)? ")

while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")


for email in addresses:
    print(email)

    url = "https://api.ciscospark.com/v1/memberships"

    payload = { "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTNlODQ0ZDAtY2Y2Zi0xMWVhLTk2MGQtZmQ2NTRiM2YzYjNm", "personEmail": email, "isModerator": false }
    headers = {'Authorization': 'Bearer ZWQyYWM1MjgtMzNmMC00ODE0LWI4YjctM2NiNzQzYmJlY2QzNTFkYzNhOTUtMTUx_PF84_consumer', 'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data = payload)


"""
Hey Professor I know this probably doesn't work but I've honestly given up hope and run out of time
I would love to know what is wrong with it though to learn how to correct it next time
"""
