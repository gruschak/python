import requests
import zeep
from zeep.client import Client

payload = {'KEY1': '451a268b4059ff9161bdc51ad8dda536', 'KEY2': 'd0c698e43dab88680445971a4ec9db98', 'TEXT': '333114'}

# RPC style soap service
client = Client('http://api.rossko.ru/service/GetSearch')
print(client.service.GetSearch(KEY1='451a268b4059ff9161bdc51ad8dda536', KEY2='d0c698e43dab88680445971a4ec9db98', TEXT='333114'))
