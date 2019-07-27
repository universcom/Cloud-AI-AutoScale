#!/bin/bash

export OS_PROJECT_DOMAIN_NAME=Default
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=hamed
export OS_AUTH_URL=http://controller:5000/v3
export OS_IDENTITY_API_VERSION=3
export OS_IMAGE_API_VERSION=2
export GNOCCHI_ENDPOINT=http://controller:8041
export OS_AUTH_TYPE=password

LB_id=`neutron lbaas-loadbalancer-list | tail -n 2 | head -n 1 | cut -d "|" -f 2 |sed 's/ //g'`
measures_id=`gnocchi resource show $LB_id -c metrics -f yaml| grep -w "network.services.lb.outgoing.bytes" | cut -d ':' -f 2`
value=`gnocchi measures show $measures_id --granularity 60 | tail -n 2 | head -n 1 | cut -d "|" -f 4 | sed 's/ //g'`
if [[ $? -eq "0" ]]
then
        echo `date +"%d-%m-%y-%T"` " | " $value >> LB_outcoming_bytes.txt
fi
