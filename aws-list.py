#!/usr/bin/python3.6
import boto3

ec2 = boto3.client('ec2')
#di = ec2.describe_instance_status()['InstanceStatuses']
di=ec2.describe_instances()['Reservations']

for inst in range(len(di)):
    inst_id=di[inst]['Instances'][0]['InstanceId']
    inst_name = 'None'
    if 'Tags' in di[inst]['Instances'][0]: 
        inst_name=di[inst]['Instances'][0]['Tags'][0]['Value']
    inst_status=di[inst]['Instances'][0]['State']['Name']
    inst_pub_ip = 'None'
    if 'PublicIpAddress' in di[inst]['Instances'][0]: inst_pub_ip=di[inst]['Instances'][0]['PublicIpAddress']
    print("%s - %s - %s - %s" % (inst_id,inst_name,inst_status,inst_pub_ip))


