from openstack import connection
import datetime , subprocess , time , numpy



class OpenstackConnection :
    def __init__(self):
        self.conn = connection.Connection(auth_url="http://controller:5000/v3",
                                     project_name="admin",
                                     username="admin",
                                     password="hamed",
                                     user_domain_id="default",
                                     project_domain_id="default",
                                     region_name="RegionOne",
                                     identity_api_version="3",
                                     volume_api_version="2"
                                     )
        self.VMs_dict = {}
        self.member_id = {}
        self.fill_VMs_dict()

    def fill_VMs_dict(self):
        with open("/root/main_code/autoscale-cloud/opestack-autoscale/VMs_status_file.txt", "r") as VMs_file:
                lines = VMs_file.readlines()
                for line in lines:
                        index , value = line.split(",")
                        print index
                        self.VMs_dict[int(index)] = self.convert_to_boolean(value)
        VMs_file.close()
        print self.VMs_dict

    def update_file(self):
        with open("/root/main_code/autoscale-cloud/opestack-autoscale/VMs_status_file.txt", "wa") as VMs_file:
                for index , value in self.VMs_dict.items():
                        VMs_file.write(str(index) + "," + str(self.convert_to_number(value)) + "\n")
        VMs_file.close()

    def get_last_inactive_VM(self):
        Index = 0
        for index , value in self.VMs_dict.items():
                if not value  :
                        self.VMs_dict[int(index)] = True
                        Index = index
                        break
        #print VM_arrays
        self.update_file()
        return Index

    def get_last_active_VM(self):
        Index = 0
        firt_item = True
        for index , value in self.VMs_dict.items():
                if firt_item:
                    firt_item = False
                    continue
                if value :
                        self.VMs_dict[int(index)] = False
                        #Index = index
                        break
        #print VM_arrays
        self.update_file()
        return Index

    def addWorker(self):
        # image = self.conn.compute.find_image("df36bfde-3fad-4dec-a17c-81ebb1140321")
        # flavor = self.conn.compute.find_flavor("97")
        # network = self.conn.network.find_network("d5f2bfb4-7910-4729-a7f3-a457ecfd1b2d")
        #
        # server = self.conn.compute.create_server(
        #     name="testAPI3", image_id=image.id, flavor_id=flavor.id,
        #     networks=[{"uuid": network.id}])
        # server = self.conn.compute.wait_for_server(server, status='ACTIVE', failures=None, interval=2, wait=120)
        #
        # worker_id = str(server.id)
        # worker_name = str(server.name)
        # worker_ip = str(server.addresses['DaaS-Network'][0]['addr'])
        # print "3"
        #
        # scalelog.write(datetime.datetime.now().strftime(
        #     "%H:%M:%S ") + " Worker :" + worker_id + " by IP:" + worker_ip + " by name:" + worker_name + " added.\n")
        # scalelog.flush()
        print "add workerrrrrrr"
        last_OCT_Worker_IP = self.get_last_inactive_VM()
        worker_ip = "172.16.1." + str(last_OCT_Worker_IP)
        worker_name = "worker-" + str(last_OCT_Worker_IP)
        addedmember = self.conn.network.create_pool_member("09b7c08e-c993-47b7-a52f-373e89bf1535",
                                                      address=worker_ip, protocol_port="80",
                                                      subnet_id="047893e0-3a15-43dd-8078-d8a3acd1f4fc"
                                                      , name=worker_name, weight="1")
        time.sleep(5)
        print "member_id is : %s" %(addedmember.id)
        self.member_id[last_OCT_Worker_IP] = addedmember.id
        print "worker added by index: %s and member_ids dict is : " %(last_OCT_Worker_IP)
        print self.member_id


    def removeWorker(self):
        print "remove workerrrrrrr"
        Index = self.get_last_active_VM()
        print "worker removed by index: %s and member_ids dict is : " %(Index)
        member_id = self.member_id[Index]
        pool_id = "09b7c08e-c993-47b7-a52f-373e89bf1535"
        #instance_id = "a5e8bd0a-9748-4575-9bde-3c4b2824adbc"
        self.conn.network.delete_pool_member(member_id, pool_id)
        #print "member by id = %s removed from pool %s" % (member_id, pool_id)
        #self.conn.compute.delete_server(instance_id, ignore_missing=True, force=True)
        #print "instance by id = %s removed " % (instance_id)
        print self.member_id


    def workerInit(self):
        Active_Workers = 0
        for index in self.VMs_dict.keys():
            if self.VMs_dict[index] :
                Active_Workers += 1
        return Active_Workers

    # def estimateMetrics(metrics, w, k):
    #     from bvalues import bvalues as bv
    #     for i in range(0, len(metrics)):
    #         metrics[i] = numpy.dot(bv[i], [(metrics[i] * w) / (w + k), (metrics[i] * k) / (w + k), 1])
    #     return metrics

    def convert_to_boolean(self , value):
        if int(value) == 1:
                return True
        else:
                return False

    def convert_to_number(self , value):
        if value:
                return 1
        else:
                return 0
