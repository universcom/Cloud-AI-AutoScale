from gnocchi import gnocchi_api

#def Resources_Usage(instance_id , LB_id , TIMESTAMP) :
def Resources_Usage(instance_id , TIMESTAMP) :
    data = gnocchi_api("admin" , "hamed" , "admin")
    instance_resource_id = instance_id
    network_instance_resource_id = data.get_resource_id("instance_network_interface" , instance_id)
    disk_instance_resource_id = data.get_resource_id("instance_disk" , instance_id)
    Resources_Usage_array = []


    cpuUtileValue = data.get_metric_value("cpu_util" , "instance" , instance_resource_id , TIMESTAMP)
    Resources_Usage_array.append(cpuUtileValue)

    memoryUSageValue = data.get_metric_value("memory.usage" , "instance" , instance_resource_id , TIMESTAMP)
    Resources_Usage_array.append(memoryUSageValue)

    incommingPacketRate = data.get_metric_value("network.incoming.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
    Resources_Usage_array.append(incommingPacketRate)

    outgoingPacketRate = data.get_metric_value("network.outgoing.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
    Resources_Usage_array.append(outgoingPacketRate)

    #diskReadPacketRate = data.get_metric_value("disk.device.read.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)
    #Resources_Usage_array.append(diskReadPacketRate)

    diskWritePacketRate = data.get_metric_value("disk.device.write.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)
    Resources_Usage_array.append(diskWritePacketRate)

    return Resources_Usage_array
