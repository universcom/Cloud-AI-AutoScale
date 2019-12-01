import time , requests , datetime

def Response_Time(self):
    LB_ip = '192.168.0.142'
    while 1:
        start = time.time()
        re=requests.get('http://' + LB_ip)
        if re.status_code == 200 or re.status_code == 201 or re.status_code == 202
            roundtrip = (time.time() - start)
            Now_RT= float(roundtrip) * 1000
            return Now_RT
