import requests, json, time
from datetime import datetime
from pyprnt import prnt

headers = {'Content-Type': 'application/json; charset=utf-8'} # cookies = {'session_id': 'sorryidontcare'}
url_PTM = 'http://localhost:10011/scenario'
scenario = [0, {"scenario" : 1},{"scenario" : 2},{"scenario" : 3},{"scenario" : 4}]
scenario_num = int(input('scenario num: '))

res = requests.post(url_PTM, headers=headers, data=json.dumps(scenario[scenario_num]))
prnt(res.json())
