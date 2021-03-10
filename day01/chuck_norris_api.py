''' 
this program requests jokes from chuck 
by aviik chakraborty
date: 02-03-2021

'''

import requests
import json


url = "http://api.icndb.com/jokes/random"


m = requests.get(url)
my_json = json.loads(m.text)

print(my_json['value']['joke'])
