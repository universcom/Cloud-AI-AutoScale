import time , requests , datetime


LB_ip = '192.168.0.142'
while 1:
    start = time.time()
    re=requests.get('http://' + LB_ip)
    if re.status_code == 200 or re.status_code == 201 or re.status_code == 202
        roundtrip = (time.time() - start)
        RT= float(roundtrip) * 1000
        f = open("/root/main_code/autoscale-cloud/opestack-autoscale/RT_data.txt" , "aw")
        f.write("%s,%s\n" % (str(datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%dT%H:%M:%S')) , str(RT)))
        f.close()
        break
