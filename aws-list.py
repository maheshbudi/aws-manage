#!/usr/bin/python3.6
import boto3

ec2 = boto3.client('ec2')
#di = ec2.describe_instance_status()['InstanceStatuses']
di=ec2.describe_instances()['Reservations']

for inst in range(len(di)):
    inst_id=di[inst]['Instances'][0]['InstanceId']
    if not 'Tags' in di[inst]['Instances'][0]: inst_name = 'None'
    else: inst_name=di[inst]['Instances'][0]['Tags'][0]['Value']
    inst_status=di[inst]['Instances'][0]['State']['Name']
    print("%s - %s - %s" % (inst_id,inst_name,inst_status))



