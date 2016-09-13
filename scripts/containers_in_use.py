#!/usr/bin/env python

"""Report number of containers in use to AWS CloudWatch as a custom
metric.  For use in setting AutoScaling policies.  Best run with
cron:
    * * * * * /home/ec2-user/containers_in_use.py > /dev/null 2>&1
Note the dependency on requests."""


from datetime import datetime
from subprocess import call

import requests


if __name__ == '__main__':
    try:
        r = requests.get('http://localhost:8000/api/stats')
        d = r.json()
        containers_available = d['available']
    except:
        # assume host is still starting up; will report 0
        containers_in_use = 0
    containers_in_use = str(20 - containers_available)
    utc_now = datetime.utcnow()
    w3c_stamp = utc_now.strftime('%Y-%m-%dT%H:%M:%SZ')
    call_list = ['aws', 'cloudwatch', 'put-metric-data',
         '--metric-name', 'ContainersInUse',
         '--namespace', 'DataNotebook',
         '--value', containers_in_use,
         '--timestamp', w3c_stamp]
    call(call_list)
