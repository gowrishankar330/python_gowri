import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info(content):
    url = f"{base_url}/pokemon/{content}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("recieved response")
        return data
    else:
        print(f"not found with {response.status_code}")



recieved_data = get_info("ditto")

if recieved_data:
    print(f"{recieved_data["name"]}")
    print(f"{recieved_data["id"]}")
    