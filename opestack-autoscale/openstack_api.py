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


    def addWorker(self ,workerStatus, scalelog):
        image = self.conn.compute.find_image("df36bfde-3fad-4dec-a17c-81ebb1140321")
        flavor = self.conn.compute.find_flavor("97")
        network = self.conn.network.find_network("d5f2bfb4-7910-4729-a7f3-a457ecfd1b2d")

        server = self.conn.compute.create_server(
            name="testAPI3", image_id=image.id, flavor_id=flavor.id,
            networks=[{"uuid": network.id}])
        server = self.conn.compute.wait_for_server(server, status='ACTIVE', failures=None, interval=2, wait=120)

        worker_id = str(server.id)
        worker_name = str(server.name)
        worker_ip = str(server.addresses['DaaS-Network'][0]['addr'])
        print "3"

        scalelog.write(datetime.datetime.now().strftime(
            "%H:%M:%S ") + " Worker :" + worker_id + " by IP:" + worker_ip + " by name:" + worker_name + " added.\n")
        scalelog.flush()
        addedmember = self.conn.network.create_pool_member("7c904e3d-9745-47e4-bdaa-9cf88e234d16",
                                                      address=worker_ip, protocol_port="80",
                                                      subnet_id="259b9592-013f-47c8-b4bc-f66b627dff88"
                                                      , name=worker_name, weight="1")

        time.sleep(5)
        print "4"
        print addedmember.id


    def removeWorker(self, workerStatus, scalelog ):
        member_id = "aa46b6f8-d298-4239-a960-8130989b5c44"
        pool_id = "7c904e3d-9745-47e4-bdaa-9cf88e234d16"
        instance_id = "a5e8bd0a-9748-4575-9bde-3c4b2824adbc"
        self.conn.network.delete_pool_member(member_id, pool_id)
        print "member by id = %s removed from pool %s" % (member_id, pool_id)
        self.conn.compute.delete_server(instance_id, ignore_missing=True, force=True)
        print "instance by id = %s removed " % (instance_id)


    def workerInit(self):
        Worker_Status = {}
        for server in self.conn.compute.servers():
            worker_ip = str(server.addresses['DaaS-Network'][0]['addr'])
            if server.status == "ACTIVE":
                Worker_Status[worker_ip] = True
            else:
                Worker_Status[worker_ip] = False
        return Worker_Status

    def estimateMetrics(metrics, w, k):
        from bvalues import bvalues as bv
        for i in range(0, len(metrics)):
            metrics[i] = numpy.dot(bv[i], [(metrics[i] * w) / (w + k), (metrics[i] * k) / (w + k), 1])
        return metrics
