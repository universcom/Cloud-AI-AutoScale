from gnocchi import gnocchi_api

def create_NN_file(instance_id , LB_id) :
    data = gnocchi_api("admin" , "hamed" , "admin")
    instance_resource_id = instance_id
    network_instance_resource_id = data.get_resource_id("instance_network_interface" , instance_id)
    disk_instance_resource_id = data.get_resource_id("instance_disk" , instance_id)
    TIMESTAMP = None

    # cpu_data = resp.get_metric_value("cpu_util" , "instance" , instance_resource_id)[2]
    # memory_data = resp.get_metric_value("memory.usage" , "instance" , instance_resource_id)[2]
    # instance_incomming_bytes_data = resp.get_metric_value("network.incoming.bytes" , "instance_network_interface" , network_resource_id)[2]
    # instance_incomming_bytes_rate_data = resp.get_metric_value("network.incoming.bytes.rate" , "instance_network_interface" , network_resource_id)[2]
    # instance_incomming_packets_data = resp.get_metric_value("network.incoming.packets" , "instance_network_interface" , network_resource_id)[2]
    # instance_incomming_packets_rate_data = resp.get_metric_value("network.incoming.packets.rate" , "instance_network_interface" , network_resource_id)[2]
    # LB_incoming_bytes_data = resp.get_metric_value("network.services.lb.incoming.bytes" , "loadBalancer" , LB_id)[2]
    # LB_outcoming_bytes_data = resp.get_metric_value(" network.services.lb.outgoing.bytes" , "loadBalancer" , LB_id)[2]

    cpuUtileValue = data.get_metric_value("cpu_util" , "instance" , instance_resource_id , TIMESTAMP)
    memoryUSageValue = data.get_metric_value("memory.usage" , "instance" , instance_resource_id , TIMESTAMP)
    incommingPacketRate = data.get_metric_value("network.incoming.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
    outgoingPacketRate = data.get_metric_value("network.outgoing.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
    diskReadPacketRate = data.get_metric_value("disk.device.read.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)
    diskWritePacketRate = data.get_metric_value("disk.device.write.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)






    f = open("./data_rt_rr_statwosysdsk.txt", "ar")
    f.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f\n" % (RT, cpu_data, memory_data, LB_incoming_bytes_data, LB_outcoming_bytes_data, instance_incomming_bytes_data,instance_incomming_bytes_rate_data,instance_incomming_packets_data,instance_incomming_packets_rate_data))
    f.close()


def read_suit_RT():
    RT_file = open("./RT_logs.txt", "r")
    line = RT_file.readline()
    RT , Clock = line.split(",")
    return rt
