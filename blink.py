#!/usr/bin/python

import sys
import json
import urllib2
import re
import time
import datetime
import httplib, urllib

def open_port():
    pass

def close_port():
    pass


class Domoticz():
    
    def __init__(self, url):
        
        self.baseurl = url
        
    def __execute__(self, url):

        req = urllib2.Request(url)
        return urllib2.urlopen(req, timeout=5)
       
    def set_device_on(self, xid):
        """
        Get the Domoticz device information.
        """
        url = "%s/json.htm?type=command&param=switchlight&idx=%s&switchcmd=On" % (self.baseurl, xid)
        data = json.load(self.__execute__(url))
        return data

    def set_device_off(self, xid):
        """
        Get the Domoticz device information.
        """
        url = "%s/json.htm?type=command&param=switchlight&idx=%s&switchcmd=Off" % (self.baseurl, xid)
        data = json.load(self.__execute__(url))
        return data

def flashing(url, device_id):

    	stop = time.time()+600
	while time.time() < stop: 
		on = Domoticz(url).set_device_on(device_id)
    		time.sleep(5)
    		off = Domoticz(url).set_device_off(device_id)
		time.sleep(5)

domoticzurl = "http://192.168.99.100:8080"
domoticzdeviceid_kaku = 167

flash = flashing(domoticzurl, domoticzdeviceid_kaku)
