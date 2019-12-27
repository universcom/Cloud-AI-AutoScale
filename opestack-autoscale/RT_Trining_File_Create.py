from gnocchi_get_data import Resources_Usage

def create_NN_file(instance_id) :
    TIMESTAMP = None
    with open("/root/main_code/autoscale-cloud/opestack-autoscale/RT_data.txt") as RT_file:
        lines = RT_file.readlines()
        for line in lines :
            TIMESTAMP , rt = line.split(",")
            resource_usage = Resources_Usage(instance_id , str(TIMESTAMP))
            RT_Net_Create_File =  open("/root/main_code/autoscale-cloud/opestack-autoscale/RT_Net_data.txt", "aw")
            RT_Net_Create_File.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f\n" %(rt , resource_usage[0], resource_usage[1], resource_usage[2], resource_usage[3], resource_usage[4],resource_usage[5]))
            RT_Net_Create_File.close()

create_NN_file("4616c369-fe47-433d-9dc4-83ad547e95c5")
