from RT import Response_Time
from gnocchi_get_data import Resources_Usage
from openstack_api import OpenstackConnection
import ConfigParser
import datetime

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
    #upper_RT = float(configParser.get('configuration', 'upper_RT'))
    print upper_RT
    #lower_RT = float(configParser.get('configuration', 'lower_RT'))
    print lower_RT
    #print Response_Time(instance_id)
    while 1 :
        Now_RT , TIMESTAMP = Response_Time()
        sleep(80)
        Now_Resource_usage = Resources_Usage(instance_id , TIMESTAMP)
        if Now_RT > upper_RT :
            k += 1
            w = sum(osc.workerInit())
            osc.addWorker()
            sleep(80)
            New_Resource_usage = Resources_Usage(instance_id , "last")
            Resource_Net_Create_File =  open("/root/main_code/autoscale-cloud/opestack-autoscale/Resorce_Net_data.txt", "aw")
            RT_Net_Create_File.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%i,%i\n" %
            (New_Resource_usage[0], New_Resource_usage[1], New_Resource_usage[2], New_Resource_usage[3], New_Resource_usage[4],New_Resource_usage[5]
            ,Now_Resource_usage[0], Now_Resource_usage[1], Now_Resource_usage[2], Now_Resource_usage[3], Now_Resource_usage[4],Now_Resource_usage[5]
            ,k ,w))
            Resource_Net_Create_File.close()

        elif Now_RT < lower_RT:
            k -= 1
            w = sum(osc.workerInit())
            if w > 1:
                osc.removeWorker()
                sleep(180)
                New_Resource_usage = Resources_Usage(instance_id , "last")
                Resource_Net_Create_File =  open("/root/main_code/autoscale-cloud/opestack-autoscale//Resorce_Net_data.txt", "w")
                RT_Net_Create_File.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%i,%i\n" %
                (New_Resource_usage[0], New_Resource_usage[1], New_Resource_usage[2], New_Resource_usage[3], New_Resource_usage[4],New_Resource_usage[5]
                ,Now_Resource_usage[0], Now_Resource_usage[1], Now_Resource_usage[2], Now_Resource_usage[3], Now_Resource_usage[4],Now_Resource_usage[5]
                ,k ,w))
                Resource_Net_Create_File.close()

main_proccess()
