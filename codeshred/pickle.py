#!/usr/bin/env python2

#import pickle, pprint
import cPickle, pprint

p = {"fabric_id": 2,
     "relay_vlan": None,
     "space": "undefined",
     "id": 5003,
     "external_dhcp": None,
     "secondary_rack": None,
     "fabric": "fabric-2",
     "primary_rack": "8x76yr",
     "resource_uri": "/MAAS/api/2.0/vlans/5003/",
     "vid": 0,
     "dhcp_on": True,
     "name": "untagged",
     "mtu": 1500,
     "fake-value": None}

output = open('data.pickle', 'wb')

pickle.dump(p, output)

output.close()

dill = open('data.pickle', 'rb')

data1 = pickle.load(dill)

pprint.pprint(data1)

dill.close()
