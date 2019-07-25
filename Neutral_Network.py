#!/bin/python

################### import libraries ###################

from ffnet import ffnet, mlgraph, readdata, savenet, loadnet
from openstack import connection
import time,re,subprocess,numpy
import datetime,csv,sys,traceback
from gnocchiclient import *
import os
import requests
























################### connection openstack ##################

conn = connection.Connection(auth_url = "http://panel.xaas.ir:5000/v3",
                             project_name = "DaaS",
                             username = "hamed.enayatzare@gmail.com",
                             password = "p@ssw0rd",
                             user_domain_id = "default",
                             project_domain_id = "default",
                             region_name = "Tehran" ,
                             identity_api_version = "3"
                             )

# scalelog=open('scalelog','w')
#
#
# def main():
#     conec = mlgraph((8,4,1))
#     net = ffnet(conec)
#     print net
#     first = True
#     cts = -1
#     RT = 0
#     RTs = []
#     N = 0
#     timesSuggested = 0
#     logLines = open('files/apacheLog', 'r')
# #    workerStatus=workerInit()
# #   w=sum(workerStatus.values())
#     for line in logLines:
#         matches = re.search('.*:([0-9]*:[0-9]*:[0-9])[0-9] .* ([0-9]*)', line)
#         cts = matches.group(1)
#         RT = respans_time_calculator()
#         print cts
#         print RT


def addWorker(workerStatus,scalelog):

     image = conn.compute.find_image("df36bfde-3fad-4dec-a17c-81ebb1140321")
     flavor = conn.compute.find_flavor("97")
     network = conn.network.find_network("d5f2bfb4-7910-4729-a7f3-a457ecfd1b2d")
     print "1"

     server = conn.compute.create_server(
        name="testAPI3", image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}])
     server = conn.compute.wait_for_server(server, status='ACTIVE', failures=None, interval=2, wait=120)
     print "2"

     worker_id = str(server.id)
     worker_name = str(server.name)
     worker_ip = str(server.addresses['DaaS-Network'][0]['addr'])
     print "3"

     scalelog.write(datetime.datetime.now().strftime("%H:%M:%S ")+" Worker :" + worker_id + " by IP:" + worker_ip + " by name:" + worker_name + " added.\n")
     scalelog.flush()
     addedmember=conn.network.create_pool_member("7c904e3d-9745-47e4-bdaa-9cf88e234d16" ,
                                    address=worker_ip , protocol_port="80" , subnet_id="259b9592-013f-47c8-b4bc-f66b627dff88"
                                                , name=worker_name, weight="1")

     time.sleep(5)
     print "4"
     print addedmember.id


def removeWorker(workerStatus,scalelog):
    member_id = "aa46b6f8-d298-4239-a960-8130989b5c44"
    pool_id = "7c904e3d-9745-47e4-bdaa-9cf88e234d16"
    instance_id = "a5e8bd0a-9748-4575-9bde-3c4b2824adbc"
    conn.network.delete_pool_member(member_id , pool_id)
    print "member by id = %s removed from pool %s" %(member_id , pool_id)
    conn.compute.delete_server(instance_id, ignore_missing=True, force=True)
    print "instance by id = %s removed " % (instance_id)

def workerInit():
    Worker_Status = {}
    for server in conn.compute.servers():
        worker_ip = str(server.addresses['DaaS-Network'][0]['addr'])
        if server.status == "ACTIVE":
            Worker_Status[worker_ip] = True
        else :
            Worker_Status[worker_ip] = False
    return Worker_Status

#scalelog.close()


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
#main()