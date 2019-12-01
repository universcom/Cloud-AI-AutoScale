from ffnet import ffnet, mlgraph, readdata, savenet, loadnet
from RT import Response_Time
from gnocchi_get_data import Resources_Usage
from openstack_api import OpenstackConnection
import ConfigParser

def main_proccess(self):
    conf_path = "/root/openstack-autoscale"
    configParser = ConfigParser.RawConfigParser()
    configFilePath = conf_path + "/autoscale.conf"
    configParser.read(configFilePath)
    instance_id = configParser.get('configuration', 'instance_based_id')
    sla_RT_Upper = float(configParser.get('configuration', 'upper_RT'))
    sla_RT_Lower = float(configParser.get('configuration', 'lower_RT'))
    RT_Net = loadnet('/root/autoscale-cloud/opestack-autoscale/RT_Net')
    Resource_Net = loadnet('/root/autoscale-cloud/opestack-autoscale/Resource_Net')
    Now_RT = Response_Time()
    Perdicted_RT = Now_RT
    Now_Resource_usage = Resources_Usage(instance_id , "last")
    perdicted_Resource_usage = Now_Resource_usage
    osc = OpenstackConnection() #OpenStack Controller == > osc
    w = sum(osc.workerInit())
    k = 0
    while 1:
        w = sum(osc.workerInit())
        Now_Resource_usage = Resources_Usage(instance_id , "last")
        Now_Resource_usage.append(k)
        Now_Resource_usage.append(w)
        perdicted_Resource_usage = Resource_Net.test(Now_Resource_usage , sla_resource ,iprint=0)[0][0]
        Perdicted_RT = RT_Net.test(Now_Resource_usage , sla_RT_Upper , iprint=0)[0][0]
        while  Perdicted_RT >= upper_RT:
            Now_Resource_usage = Resources_Usage(instance_id , "last")
            Now_Resource_usage.append(k)
            Now_Resource_usage.append(w)
            perdicted_Resource_usage = Resource_Net.test(Now_Resource_usage , sla_resource ,iprint=0)[0][0]
            Perdicted_RT = RT_Net.test(Now_Resource_usage , sla_RT_Upper , iprint=0)[0][0]
            if Perdicted_RT < upper_RT:
                break
            k + =1
        while Perdicted_RT <= lower_RT and w > 1:
            k -=1
            Now_Resource_usage = Resources_Usage(instance_id , "last")
            Now_Resource_usage.append(k)
            Now_Resource_usage.append(w)
            perdicted_Resource_usage = Resource_Net.test(Now_Resource_usage , sla_resource ,iprint=0)[0][0]
            Perdicted_RT = RT_Net.test(Now_Resource_usage , sla_RT_Upper , iprint=0)[0][0]
            if Perdicted_RT > upper_RT:
                k+=1
                break
            if w+k == 1:
                break

        if k > 0:
            for i in range(0,k):
                osc.addWorker()
            w = sum(osc.workerInit())
        elif k < 0:
            for i in range(0,k):
                osc.removeWorker()
            w = sum(osc.workerInit())
    # while 1:
    #     Now_Resource_usage = Resources_Usage(instance_id , "last")
    #     Now_Resource_usage.append(k)
    #     Now_Resource_usage.append(w)
    #     perdicted_Resource_usage = Resource_Net.test(Now_Resource_usage , sla_resource ,iprint=0)[0][0]
    #     o,r = RT_Net.test(Now_Resource_usage , sla_Resource , iprint=0)
    #     Perdicted_RT = o[0][0]
    #     if Perdicted_RT >= sla_RT_Upper:
    #         k += 1
    #         osc.addWorker()
    #         w = sum(osc.workerInit())
    #     elif Perdicted_RT <= sla_RT_Lower:
    #         k -=1
    #         if w > 1 :
    #             osc.removeWorker()
    #             w = sum(osc.workerInit())
    #     sleep(60)
