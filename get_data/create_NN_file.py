import time , requests
import os


def READ_CPU_USAGE():
    return 0

def READ_MEMORY_USAGE():
    return 0

def READ_LB_INCOMING_KB():
    return 0

def READ_LB_OUTCOMING_KB():
    return 0

def READ_INSTANE_INCOMING_KB():
    return 0

def READ_INSTANE_INCOMING_KB_RATE():
    return 0

def READ_INSTANE_INCOMING_PKT():
    return 0

def READ_INSTANE_INCOMING_PKT_RATE():
    return 0

def RESPOSNE_TIME():
 return 0

def main():

    RT = RESPOSNE_TIME()
    cpu_usage = READ_CPU_USAGE()
    memory_usage = READ_MEMORY_USAGE()
    LB_incoming_bytes = READ_LB_INCOMING_KB()
    LB_outcoming_bytes = READ_LB_OUTCOMING_KB()
    instance_incoming_bytes = READ_INSTANE_INCOMING_KB()
    instance_incoming_bytes_rate = READ_INSTANE_INCOMING_KB_RATE()
    instance_incoming_packets = READ_INSTANE_INCOMING_PKT()
    instance_incoming_packets_rate = READ_INSTANE_INCOMING_PKT_RATE()


    f = open("./data_rt_rr_statwosysdsk.txt", "ar")
    f.write("%0.2f,%0.3f,%0.2f,%i,%i,%i,%i,%i,%i\n" % (RT, cpu_usage, memory_usage, LB_incoming_bytes, LB_outcoming_bytes, instance_incoming_bytes,instance_incoming_bytes_rate,instance_incoming_packets,instance_incoming_packets_rate))
    f.close()

main()