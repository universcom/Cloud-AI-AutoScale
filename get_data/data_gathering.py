from gnocchi import gnocchi_api

def create_NN_file(instance_id , LB_id) :
    data = gnocchi_api("admin" , "hamed" , "admin")
    instance_resource_id = instance_id
    network_resource_id = data.get_resource_id("instance_network_interface" , instance_id)

    cpu_data = round(resp.get_metric_value("cpu_util" , "instance" , instance_resource_id), 3)
    memory_data = round(resp.get_metric_value("memory.usage" , "instance" , instance_resource_id), 3)
    instance_incomming_bytes_data = round(resp.get_metric_value("network.incoming.bytes" , "instance_network_interface" , network_resource_id), 3)
    instance_incomming_bytes_rate_data = round(resp.get_metric_value("network.incoming.bytes.rate" , "instance_network_interface" , network_resource_id), 3)
    instance_incomming_packets_data = round(resp.get_metric_value("network.incoming.packets" , "instance_network_interface" , network_resource_id), 3)
    instance_incomming_packets_rate_data = round(resp.get_metric_value("network.incoming.packets.rate" , "instance_network_interface" , network_resource_id), 3)
    LB_incoming_bytes_data = round(resp.get_metric_value("network.services.lb.incoming.bytes" , "loadBalancer" , LB_id), 3)
    LB_outcoming_bytes_data = round(resp.get_metric_value(" network.services.lb.outgoing.bytes" , "loadBalancer" , LB_id), 3)
