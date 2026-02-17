import json
import os
import requests

def main():
    print("Hello from osinter!") #DBP
    ip_address=input("What IP do you want to search up?\nIP: ")
    abuseipdb_ip_call(ip_address)
    virustotal_ip_call(ip_address)



#Consider making IP addresses an IP Class Object, then setting each of the various
    #OSINT sources as methods on that IP to be called in sequence, or walk the list
    #of IP-tagged OSINT sites. Additional option - instead of Class methods, do a 
    #meta-function tree that allows . calls to split out. TBH the Class and Walk method
    #is better, since it allows dynamic expansion with new sites down the line. Sort
    #this out once at least four IP OSINT targets are available to be combined, and
    #consider working that into a broader effort around opensiteskeys.py.
def abuseipdb_ip_call(ip_address):
    with open("sitesnkeys.json", "r") as file: 
        data = json.load(file)
        url=data["sites"]["abuseipdb"]["url"]
        headers = {
            'Accept': data["sites"]["abuseipdb"]["accept"],
            'Key': data["sites"]["abuseipdb"]["key"]
        }
        querystring = {
            'ipAddress': ip_address,
            'maxAgeInDays': data["sites"]["abuseipdb"]["maxAgeInDays"],
            'verbose': True
        }

    response = requests.get(url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    print(f"AbuseIPDB IP Report:\n===============\n{json.dumps(decodedResponse, sort_keys=True, indent=4)}\n")


def virustotal_ip_call(ip_address):
    with open("sitesnkeys.json", "r") as file: 
        data = json.load(file)
        rawurl=data["sites"]["virustotal"]["url"]
        url=f"{rawurl.rstrip('/')}/{ip_address}"
        headers = {
            'Accept': data["sites"]["virustotal"]["accept"],
            'x-apikey': data["sites"]["virustotal"]["key"]
        }

    response = requests.get(url=url, headers=headers)

    # Formatting output and dropping less-useful output bloat
    decodedResponse = json.loads(response.text)
    decodedResponse.get("data", {}).get("attributes", {}).pop("last_analysis_results", None)
    decodedResponse.get("data", {}).get("attributes", {}).get("rdap", {}).pop("notices", None)
    decodedResponse.get("data", {}).get("attributes", {}).get("rdap", {}).pop("links", None)
    decodedResponse.get("data", {}).get("attributes", {}).get("rdap", {}).pop("entities", None)
    
    #Stripped output for DBP/use
    print(f"VirusTotal IP Report:\n===============\n{json.dumps(decodedResponse, sort_keys=True, indent=4)}\n")

        






if __name__ == "__main__":
    main()



