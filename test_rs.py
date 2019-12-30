import json
import requests
import zeep
from zeep.client import Client

# RPC style soap service
client = Client('http://api.rossko.ru/service/GetSearch')
response = client.service.GetSearch(KEY1='451a268b4059ff9161bwrasc51ad8dda536', KEY2='dfg0c698e43dab88680445971a4ec9db98', TEXT='333144')
print("len(response.PartsList) = ", len(response.PartsList))
print("len(response.PartsList.Part) = ", len(response.PartsList.Part))
i = 0
for part in response.PartsList.Part:
    if part.brand and part.partnumber and part.name:
        # print(i, " ", part)
        print(i, ':  ', part.brand + ' # ' + part.partnumber + ' : ' + part.name)
        i += 1
