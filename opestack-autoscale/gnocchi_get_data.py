from gnocchi_api import gnocchi_api
import time
#def Resources_Usage(instance_id , LB_id , TIMESTAMP) :
def Resources_Usage(instance_id , TIMESTAMP) :
    data = gnocchi_api("admin" , "hamed" , "admin")
    instance_resource_id = instance_id
    network_instance_resource_id = data.get_resource_id("instance_network_interface" , instance_id)
    print network_instance_resource_id
    disk_instance_resource_id = data.get_resource_id("instance_disk" , instance_id)
    print disk_instance_resource_id
    Resources_Usage_array = []

    while 1:
        cpuUtileValue = data.get_metric_value("cpu_util" , "instance" , instance_resource_id , TIMESTAMP)
        if str(cpuUtileValue) == "None":
            print str(cpuUtileValue)
            time.sleep(10)
            continue
        else:
            break
    print cpuUtileValue
    Resources_Usage_array.append(cpuUtileValue)

    memoryUSageValue = data.get_metric_value("memory.usage" , "instance" , instance_resource_id , TIMESTAMP)
    print memoryUSageValue
    Resources_Usage_array.append(memoryUSageValue)


    incommingPacketRate = data.get_metric_value("network.incoming.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
    print incommingPacketRate
    Resources_Usage_array.append(incommingPacketRate)

    outgoingPacketRate = data.get_metric_value("network.outgoing.packets.rate" , "instance_network_interface" , network_instance_resource_id , TIMESTAMP)
    print outgoingPacketRate
    Resources_Usage_array.append(outgoingPacketRate)

    diskReadPacketRate = data.get_metric_value("disk.device.read.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)
    print diskReadPacketRate
    Resources_Usage_array.append(diskReadPacketRate)

    diskWritePacketRate = data.get_metric_value("disk.device.write.requests.rate" , "instance_disk" , disk_instance_resource_id , TIMESTAMP)
    print diskWritePacketRate
    Resources_Usage_array.append(diskWritePacketRate)

    print Resources_Usage_array
    return Resources_Usage_array
