import requests
import json

response = requests.get("https://raw.githubusercontent.com/registreerocks/studentNFT/master/build/contracts/Registree.json")
registree_interface = response.json()
registree_address = registree_interface['networks']['4']['address']