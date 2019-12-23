from RT import Response_Time
from gnocchi_get_data import Resources_Usage
from openstack_api import OpenstackConnection
import ConfigParser
import datetime
import time

def main_proccess():
    conf_path = "/root/main_code/autoscale-cloud/opestack-autoscale"
    configParser = ConfigParser.RawConfigParser()
    configFilePath = conf_path + "/autoscale.conf"
    configParser.read(configFilePath)
    k = 0
    osc = OpenstackConnection() #OpenStack Controller == > osc
    print osc
    instance_id = configParser.get('configuration', 'instance_based_id')
    print instance_id
    upper_RT = float(configParser.get('configuration', 'upper_RT'))
    print "upper_RT is: %s" %(upper_RT)
    lower_RT = float(configParser.get('configuration', 'lower_RT'))
    print "lower_RT is: %s" %(lower_RT)
    #print Response_Time(instance_id)
    while 1 :
        Now_RT , TIMESTAMP = Response_Time()
        print "now RT is: %s" %(Now_RT)
        print "TIMESTAMP is: %s" %(TIMESTAMP)
        #time.sleep(90)
        #Now_Resource_usage = Resources_Usage(instance_id , TIMESTAMP)
        print Now_Resource_usage
        w = osc.workerInit()
        while Now_RT > upper_RT :
            k += 1
            print "k is %s" %(k)
            print "w is %s" %(w)
            Now_Resource_usage = Resources_Usage(instance_id , TIMESTAMP)
            osc.addWorker()
            time.sleep(60)
            TIMESTAMP = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')
            New_Resource_usage = Resources_Usage(instance_id , TIMESTAMP)
            Now_RT , TIMESTAMP = Response_Time()
            print "now RT is: %s" %(Now_RT)
            print New_Resource_usage
            Resource_Net_Create_File =  open("/root/main_code/autoscale-cloud/opestack-autoscale/Resorce_Net_data.txt", "aw")
            Resource_Net_Create_File.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%i,%i\n" %
            (New_Resource_usage[0], New_Resource_usage[1], New_Resource_usage[2], New_Resource_usage[3], New_Resource_usage[4],New_Resource_usage[5]
            ,Now_Resource_usage[0], Now_Resource_usage[1], Now_Resource_usage[2], Now_Resource_usage[3], Now_Resource_usage[4],Now_Resource_usage[5]
            ,k ,w))
            Resource_Net_Create_File.close()
        w = osc.workerInit()
        k = 0
        while Now_RT < lower_RT and w>1:
            k -= 1
            print "k is %s" %(k)
            print "w is %s" %(w)
            Now_Resource_usage = Resources_Usage(instance_id , TIMESTAMP)
            osc.removeWorker()
            sleep(60)
            TIMESTAMP = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')
            New_Resource_usage = Resources_Usage(instance_id , TIMESTAM)
            Now_RT , TIMESTAMP = Response_Time()
            print "now RT is: %s" %(Now_RT)
            print New_Resource_usage
            Resource_Net_Create_File =  open("/root/main_code/autoscale-cloud/opestack-autoscale/Resorce_Net_data.txt", "w")
            Resource_Net_Create_File.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%i,%i\n" %
            (New_Resource_usage[0], New_Resource_usage[1], New_Resource_usage[2], New_Resource_usage[3], New_Resource_usage[4],New_Resource_usage[5]
            ,Now_Resource_usage[0], Now_Resource_usage[1], Now_Resource_usage[2], Now_Resource_usage[3], Now_Resource_usage[4],Now_Resource_usage[5]
            ,k ,w))
            Resource_Net_Create_File.close()
            if k + w -1 == 0 :
                break


main_proccess()
