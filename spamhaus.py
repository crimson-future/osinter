import json
import requests


headers={
    'Auth-Key':"b4eec6e85575a8f777fa51ebe8858d5976fd0ae260f9ecb6"
}
url="https://threatfox-api.abuse.ch/api/v1/"
ioc="103.7.60.82"
payload={"query": "search_ioc", "search_term": ipaddress, "exact_match":False}




response = requests.post(url, headers=headers, json=payload)


# Formatted output
decodedResponse = json.loads(response.text)
print(f"Spamhaus IP Report: \n(Check to confirm IP is the desired one, Spamhaus has an inexact match when not searching explicit port numbers. Reports generated show all close matches, and may not be exact.)\n===============\n{json.dumps(decodedResponse, sort_keys=True, indent=4)}\n")







# def abuseipdb_ip_call(ip_address):
#     with open("sitesnkeys.json", "r") as file: 
#         data = json.load(file)
#         url=data["sites"]["abuseipdb"]["url"]
#         headers = {
#             'Accept': data["sites"]["abuseipdb"]["accept"],
#             'Key': data["sites"]["abuseipdb"]["key"]
#         }
#         querystring = {
#             'ipAddress': ip_address,
#             'maxAgeInDays': data["sites"]["abuseipdb"]["maxAgeInDays"],
#             'verbose': True
#         }

#     response = requests.get(url=url, headers=headers, params=querystring)

#     # Formatted output
#     decodedResponse = json.loads(response.text)
#     print(f"AbuseIPDB IP Report:\n===============\n{json.dumps(decodedResponse, sort_keys=True, indent=4)}\n")
