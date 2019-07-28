import time,re,subprocess,numpy
import os
import requests


def cpu_read(instance_id):
    os.system("./read_CPU_utile_current.sh " + str(instance_id))
    cpu_usage=float(open("temp_value", "r").readline())
    os.system("rm temp_value")
    return cpu_usage


def memory_read(instance_id):
    os.system("./read_Memory_usage.sh " + str(instance_id))
    memory_usage = float(open("temp_value", "r").readline())
    os.system("rm temp_value")
    return memory_usage

def respans_time_calculator():
    start = time.time()
    payload = {"id": "1' and if (ascii(substr(database(), 1, 1))=115,sleep(3),null) --+"}
    #r = requests.get('http://127.0.0.1/sqli-labs/Less-9', params=payload)
    requests.get('http://31.184.132.45')
    #time.sleep(5)
    roundtrip = (time.time() - start) *1000
    #print ("%0.2f" %(float(roundtrip)))
    return str(round(roundtrip, 2))