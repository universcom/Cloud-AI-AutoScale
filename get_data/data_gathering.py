from gnocchi import gnocchi_api

def create_NN_file(instance_id) :
    data = gnocchi_api("admin" , "hamed" , "admin")
    instance_resource_id = instance_id
    network_instance_resource_id = data.get_resource_id("instance_network_interface" , instance_id)
    disk_instance_resource_id = data.get_resource_id("instance_disk" , instance_id)
    TIMESTAMP = None
    with open("/root/autoscale-cloud/get_data/RTs.txt") as RT_file:
        lines = RT_file.readlines()
        for line in lines :
            TIMESTAMP , rt = line.split(",")
            RT = float(RT) * 1000
            cpuUtileValue = data.get_metric_value("cpu_util" , "instance" , instance_resource_id , TIMESTAMP)
            memoryUSageValue = data.get_metric_value("memory.usage" , "instance" , instance_resource_id , TIMESTAMP)
            incommingPacketRate = data.get_metric_value("network.incoming.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
            outgoingPacketRate = data.get_metric_value("network.outgoing.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
            diskReadPacketRate = data.get_metric_value("disk.device.read.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)
            diskWritePacketRate = data.get_metric_value("disk.device.write.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)
            f = open("./data_rt_rr_statwosysdsk.txt", "ar")
            f.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f\n" % (RT, cpuUtileValue, memoryUSageValue
            , incommingPacketRate, outgoingPacketRate, diskReadPacketRate,diskWritePacketRate))
        f.close()
create_NN_file("3b4419bb-b94f-45a7-b699-3e9c9e3bc108")
