#Sort this out later - may be able to unify the format of querying, standardize. Consider a
    #complex check to see if the site allows for a maxAge value and/or verbose statement.
    #Hold off until at least four sites are set up. 


with open("sitesnkeys.json", "r") as file: 
        data = json.load(file)
        url=data["sites"][sitename]["url"]
        headers = {
            'Accept': data["sites"][sitename]["accept"],
            'Key': data["sites"][sitename]["key"]
        }
        querystring = {
            'ipAddress': ip_address,
            'maxAgeInDays': data["sites"][sitename]["maxAgeInDays"],
            'verbose': True
        }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))