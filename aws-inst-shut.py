#!/usr/bin/python3.6
#import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
di=ec2.describe_instances()['Reservations']
ec2_inst_details = []

def ec2_details():    
    for inst in range(len(di)):
        inst_id=di[inst]['Instances'][0]['InstanceId']
        if not 'Tags' in di[inst]['Instances'][0]: inst_name = 'None'
        else: inst_name=di[inst]['Instances'][0]['Tags'][0]['Value']
        inst_status=di[inst]['Instances'][0]['State']['Name']
        ec2_inst_details.append({
            'ec2_inst_id': str(inst_id),
            'ec2_inst_name': inst_name,
            'ec2_inst_status': inst_status
        })
        #print("%s - %s - %s" % (inst_id,inst_name,inst_status))
    return ec2_inst_details

print(">>> PRE shutdown status:")
for iter in ec2_details():
    print("%s - %s - %s" % (iter['ec2_inst_id'],iter['ec2_inst_name'],iter['ec2_inst_status']))

## Stop all instances:
# Do a dryrun first to verify permissions
for inst in ec2_inst_details:
    print("%s - 'running'" % inst['ec2_inst_status'])
    if inst['ec2_inst_status'] in 'running':
        try:
            ec2.stop_instances(InstanceIds=[inst['ec2_inst_id']], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, call stop_instances without dryrun
        try:
            response = ec2.stop_instances(InstanceIds=[inst['ec2_inst_id']], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)

'''
print(">>> Post shutdown status:")
for iter in ec2_details():
    print("%s - %s - %s" % (iter['ec2_inst_id'],iter['ec2_inst_name'],iter['ec2_inst_status']))
'''
