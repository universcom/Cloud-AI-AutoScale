import requests
import json
import time
from datetime import datetime , timedelta

class gnocchi_api:
    def __init__(self , username , password , project_name):
        self.username = username
        self.password = password
        self.project_name = project_name

    def get_tocken(self ,usename , password , project_name):
        task = { "auth": {
            "identity": {
              "methods": ["password"],
              "password": {
                "user": {
                  "name": str(usename),
                  "domain": { "id": "default" },
                  "password": str(password)
                }
              }
            },
            "scope": {
              "project": {
                "name": str(project_name),
                "domain": { "id": "default" }
              }
            }
          }
        }
        try:
            resp = requests.post('http://localhost:5000/v3/auth/tokens' , data=json.dumps(task) , headers={'Content-Type':'application/json'} )
            if resp.status_code == 200 or resp.status_code ==201 or resp.status_code == 202 :
                return resp.headers['X-Subject-Token']
            else:
                raise "error during get tocken form keystone"
        except Exception as e:
            raise "error during get tocken form keystone"


    def get_all_metrics(self):
        header_date = {
            'Content-Type':'application/json' ,
            'Content-Length': '0' ,
            'X-AUTH-TOKEN' : self.get_tocken(self.username , self.password , self.project_name)
        }
        resp = requests.get(self._url('/v1/metric') , headers=header_date)
        print resp.text


    def get_metric_value(self , metric_name , resource_type ,resource_id , RT_timestamp ):
        header_date = {
            'Content-Type':'application/json' ,
            'Content-Length': '0' ,
            'X-AUTH-TOKEN' : self.get_tocken(self.username , self.password , self.project_name)
        }
        url = self._url('/v1/resource/' + resource_type + '/' + resource_id + '/metric/' + metric_name + '/measures?granularity=60second&refresh=true')
        resp = requests.get(url , headers=header_date)
        all_responses = resp.json()
        if RT_timestamp == "last":
            return resp[-1][2]
        for response in all_responses:
            if self.time_compersation(RT_timestamp , response[0].split("+")[0]):
                return response[2]

    def get_resource_id(self , resource_type ,instance_id):
        header_date = {
            'Content-Type':'application/json' ,
            'Content-Length': '0' ,
            'X-AUTH-TOKEN' : self.get_tocken(self.username , self.password , self.project_name)
        }
        url= self._url('/v1/search/resource/' + resource_type)
        resp = requests.post(url , headers=header_date)
        i = 0
        for res in resp :
            if str(resp.json()[i]['instance_id']) == instance_id:
                return resp.json()[i]['id']
            i+=1
        raise "no have any network interface exist for instance: " + instance_id

    def _url(self , path):
        return 'http://localhost:8041' + path

    def time_compersation(self , RT_timestamp , Value_timestamp):
        RTT = RT_timestamp
        T1 = Value_timestamp
        T2 = (datetime.strptime(T1, '%Y-%m-%dT%H:%M:%S') + timedelta(seconds=60)).strftime('%Y-%m-%dT%H:%M:%S')
        if (RTT >= T1) and (RTT < T2):
            return True
        else:
            return False



def main():
    resp = gnocchi_api("admin" , "hamed" , "admin")
    print resp.get_metric_value("cpu_util" , "instance" , "661449cf-b267-4849-8613-9a348b35a9ee" , "2019-10-07T07:17:00")
    #print resp.get_resource_id("instance_network_interface" , "4bcb2b5b-0946-4b88-bfea-d43956333020")

main()
