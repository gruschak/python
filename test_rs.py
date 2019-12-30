import requests
import zeep
from zeep.client import Client

# RPC style soap service
client = Client('http://api.rossko.ru/service/GetSearch')
print(client.service.GetSearch(KEY1='451a268bwr59ff9161bdc51ad8dda536', KEY2='z0c68e43dab88680445971a4ec9db98', TEXT='333114'))
