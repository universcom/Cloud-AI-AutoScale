import time , requests , datetime

start = time.time()
f = open("RTs.txt" , "w")
payload = {"id": "1' and if (ascii(substr(database(), 1, 1))=115,sleep(3),null) --+"}
# r = requests.get('http://127.0.0.1/sqli-labs/Less-9', params=payload)
LB_ip = '192.168.0.142'
requests.get('http://' + LB_ip)
# time.sleep(5)
roundtrip = (time.time() - start) * 1000
RT= round(roundtrip, 3)
f = open("./RT_logs.txt", "ar")
f.write("%s,%s\n" % (str(datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%dT%H:%M:%S')) , str(RT)))
f.close()
