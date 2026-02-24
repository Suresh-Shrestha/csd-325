import requests
import json

API_URL = "http://api.open-notify.org/astros.json"

def jprint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

def main():

    # 1) Test connection
    print("1) CONNECTION TEST")
    response = requests.get(API_URL)
    print("Status Code:", response.status_code)
    print()

    # 2) Print raw response (no formatting)
    print("2) RAW RESPONSE")
    print(response.text)
    print()

    # Convert to dictionary
    data = response.json()

    # 3) Print formatted JSON 
    print("3) FORMATTED JSON ")
    jprint(data)
    print()

    # 4) Retrieve astronauts and format output
    print("4) CURRENT ASTRONAUTS")
    print("People currently in space:", data.get("number", 0))
    print("-----------------------------------")

    for person in data.get("people", []):
        print(person.get("name"), "-", person.get("craft"))

if __name__ == "__main__":
    main()
