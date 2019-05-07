import boto3
import json

ec2 = boto3.client('ec2')
#di = ec2.describe_instance_status()['InstanceStatuses']
di=ec2.describe_instances()

print(json.dumps(di['Reservations'][0]))
