import json
import os
import requests

def main():
    # print("Hello from osinter!") #DBP
    ip_address=input("What IP do you want to search up?\nIP: ")
    abuseipdb_call(ip_address)


def catcalls():
    facts=[]
    numfact=int(input("How many cat facts do ya want?\nNumber: "))
    #print("Hello from osinter!") #DBP
    iter=0
    while iter != numfact:
        r = requests.get('https://catfact.ninja/fact')
        facts.append(r.json()['fact'])
        iter+=1
    for fact in facts:
        print(f"Fact: {fact}\n")

def abuseipdb_call(ip_address):
    # Defining the api-endpoint

    with open("sitesnkeys.json", "r") as file: 
        data = json.load(file)
        url=data["sites"]["abuseipdb"]["url"]
        headers = {
            'Accept': data["sites"]["abuseipdb"]["accept"],
            'Key': data["sites"]["abuseipdb"]["key"]
        }
        querystring = {
            'ipAddress': ip_address,
            'maxAgeInDays': data["sites"]["abuseipdb"]["maxAgeInDays"]
        }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))

if __name__ == "__main__":
    main()

#catcalls() #Debug, testing for API mechanic practice

