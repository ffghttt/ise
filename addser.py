#!/usr/bin/python
from httplib2 import Http

import csv
ifile = open( 'profiler_endpoints.csv', "rb")
reader = csv.reader(ifile)
endpointdata = list(reader)
n = len(endpointdata)

#Set correct IP address
url = "https://10.70.82.204:9060/ers/config/endpoint"
headers={'Content-Type':'application/xml','Accept':'application/xml'}
connection = Http(".cache", disable_ssl_certificate_validation=True)
#Set correct credentials
connection.add_credentials("ersadmin", "BNbn1234")

#Set endpoint description and MAC address
i = 0
for  x in range(n):
        endpoint_mac = endpointdata[i][0]
        endpoint_des = endpointdata[i][1]
        i=i+1
        body = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns3:endpoint description="'\
        + endpoint_des + \
        '" xmlns:ns2="ers.ise.cisco.com" xmlns:ns3="identity.ers.ise.cisco.com"><mac>' \
        + endpoint_mac + \
        '</mac><staticGroupAssignment>true</staticGroupAssignment><staticProfileAssignment>false</staticProfileAssignment></ns3:endpoint>'
        response = connection.request(url, "POST", body, headers)
        print response
        print '\n'

print "Successfully add "+str(i)+ " endpoints!"
