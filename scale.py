from ffnet import ffnet, mlgraph, readdata, savenet, loadnet
from datetime import timedelta , datetime
import time,re,subprocess,numpy
import datetime,csv,sys,traceback
upperRT=90
lowerRT=40

def main():
    net=loadnet('./files/trained_net')
    first_time_stamp =  datetime.fromtimestamp(time.time())
    last_time_stamp = first_time_stamp + timedelta(hours=1)
    #last_time_stamp = first_time_stamp + timedelta(days=9, hours=2, minutes=5, seconds=2, microseconds=213)
    time_stamp = first_time_stamp
    while last_time_stamp >= time_stamp:
        
        time.sleep(60)
        time_stamp = datetime.fromtimestamp(time.time())



def addWorker(Number_of_worker):
    pass

def removeWorker(Number_of_worker):
    pass

def workerInit():
    pass

def estimateMetrics(metrics,w,k):
    pass

main()
