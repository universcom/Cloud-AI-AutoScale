from gnocchi_get_data import Resources_Usage

def Create_NN_File(instance_id , LB_id ):
    Response_time_file =  open("./RT_data.txt", "r")
    RT_Net_Create_File =  open("./RT_Net_data.txt", "w")
    with open("RT_data.txt", "r") as lines:
        for line in lines:
            rt = line.split(",")[1]
            TIMESTAMP = line.split(",")[0]
            resources = Resources_Usage(instance_id , LB_id , TIMESTAMP)
            RT_Net_Create_File.write("%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f\n" %
            (rt, resources[0], resources[1], resources[2], resources[3], resources[4],resources[5]))

    RT_Net_Create_File.close()
