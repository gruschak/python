import json
import requests
import zeep
from zeep.client import Client

Rossko = {'HST145': 'RS', 'HST40': 'RSN'}

# RPC style soap service
client = Client('http://api.rossko.ru/service/GetSearch')
response = client.service.GetSearch(KEY1='', KEY2='', TEXT='LAC105')
print("len(response.PartsList) = ", len(response.PartsList))
print("len(response.PartsList.Part) = ", len(response.PartsList.Part))
i = 0
for part in response.PartsList.Part:
    if part.brand and part.partnumber and part.name:
        i += 1
        # print(i, " ", part)
        print(i, ':  ', part.brand + ' # ' + part.partnumber + ' : ' + part.name)
        if part.stocks:
            print(type(part.stocks.stock)) # class 'list'
            for ps in part.stocks.stock :
                if ps.id in Rossko:
                    print(Rossko[ps.id], ps.price, ps.count)

