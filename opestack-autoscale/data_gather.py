from gnocchi_get_data import Resources_Usage
import ConfigParser

def Create_NN_File(instance_id):
    RT_Net_Create_File =  open("/root/autoscale-cloud/opestack-autoscale/RT_Net_data.txt", "aw")
    with open("/root/autoscale-cloud/opestack-autoscale/RT_data.txt/RT_data.txt", "r") as RT_file:
        lines = RT_file.readlines()
        for line in lines:
            TIMESTAMP , rt = line.split(",")
            RT = float(RT) * 1000
            resources = Resources_Usage(instance_id , TIMESTAMP)
            RT_Net_Create_File.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f\n" %
            (RT, resources[0], resources[1], resources[2], resources[3], resources[4]))
    RT_Net_Create_File.close()


conf_path = "/root/openstack-autoscale"
configParser = ConfigParser.RawConfigParser()
configFilePath = conf_path + "/autoscale.conf"
configParser.read(configFilePath)
instance_id = configParser.get('configuration', 'instance_based_id')
Create_NN_File(instance_id)
