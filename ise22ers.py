import json
import os
import re
import urllib3

import requests
import xmltodict

class ERS(object):
    def __init__(self, ise_node, ers_user, ers_pass, verify=False, disable_warnings=False, timeout=2):

        self.ise_node = ise_node
        self.user_name = ers_user
        self.user_pass = ers_pass
        self.url_base = 'https://{0}:9060/ers'.format(self.ise_node)
        self.ise = requests.session()
        self.ise.auth = (self.user_name, self.user_pass)
        self.ise.verify = verify  # http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
        self.disable_warnings = disable_warnings
        self.timeout = timeout
        self.ise.headers.update({'Connection': 'keep_alive'})
        urllib3.disable_warnings()


    def get_endpoints(self):

        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/endpoint'.format(self.url_base))
        print(resp.status_code)
        print(resp.text)

    def get_endpoint_groups(self):
        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/endpointgroup'.format(self.url_base))
        print(resp.status_code)
        print(resp.text)

    def get_endpoint_group(self, group):
        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/endpointgroup?filter=name.EQ.{1}'.format(self.url_base, group))
        print(resp.status_code)
        print(resp.text)

    def get_identity_groups(self):
        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/identitygroup'.format(self.url_base))
        print(resp.status_code)
        print(resp.text)

    def get_identity_group(self, group):
        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/identitygroup?filter=name.EQ.{1}'.format(self.url_base, group))
        print(resp.status_code)
        print(resp.text)

    def get_users(self):
        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/internaluser'.format(self.url_base))
        print(resp.status_code)
        print(resp.text)

    def get_user(self, user_name):
        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/internaluser?filter=name.EQ.{1}'.format(self.url_base, user_name))
        print(resp.status_code)
        print(resp.text)

    def get_device_groups(self):
        self.ise.headers.update({'Content-Type': 'application/json', 'Accept': 'application/json'})
        resp = self.ise.get('{0}/config/networkdevicegroup'.format(self.url_base))
        print(resp.status_code)
        print(resp.text)

    def add_user(self,user_name,password,first_name='',enable='',last_name='',email='',description=''):
        self.ise.headers.update({'Content-Type': 'application/xml', 'Accept': 'application/json'})
        data = open('user_add.xml', 'r').read().format(user_name, password, enable, first_name, last_name, email, description)
        resp = self.ise.post('{0}/config/internaluser'.format(self.url_base), data=data, timeout=self.timeout)
        if resp.status_code == 201:
            print ('User {0} Added Successfully'.format(user_name))

    def add_endpoint(self,macaddress,description):
        self.ise.headers.update({'Content-Type': 'application/xml', 'Accept': 'application/json'})
        data = open('endpoint_add.xml', 'r').read().format(macaddress, description)
        resp = self.ise.post('{0}/config/endpoint'.format(self.url_base), data=data, timeout=self.timeout)
        if resp.status_code == 201:
            print ('Endpoint {0} Added Successfully'.format(macaddress))


ise = ERS(ise_node='10.70.82.204', ers_user='ersadmin', ers_pass='BNbn1234', verify=False, disable_warnings=True)

ise.get_endpoints()
