# import time , requests , datetime
#
# def Response_Time():
#     RT_array = []
#     LB_ip = '192.168.0.142'
#     while 1:
#         start = time.time()
#         re=requests.get('http://' + LB_ip)
#         if re.status_code == 200 or re.status_code == 201 or re.status_code == 202:
#             roundtrip = (time.time() - start)
#             Now_RT= float(roundtrip) * 1000
#             TIMESTAMP = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%dT%H:%M:%S')
#             RT_array.append(Now_RT)
#             RT_array.append(TIMESTAMP)
#             return RT_array

import time , requests , datetime


LB_ip = '192.168.0.142'
while 1:
    start = time.time()
    re=requests.get('http://' + LB_ip)
    if re.status_code == 200 or re.status_code == 201 or re.status_code == 202:
        roundtrip = (time.time() - start)
        RT = roundtrip
        f = open("/root/autoscale-cloud/get_data/RTs.txt" , "aw")
        f.write("%s,%s\n" % (str(datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%dT%H:%M:%S')) , str(RT)))
        f.close()
        break
