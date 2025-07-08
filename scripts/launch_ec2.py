#import library to communicate with aws
import boto3 

#grab ec2 instance variable
ec2 = boto3.resource('ec2') 

#define an ec2 instance using credentials
instances = ec2.create_instances(
    ImageId='ami-0c803b171269e2d72', #Amazon Linux option
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro', #free tier
    KeyName='BOTO3-SCRIPTING', 
    SecurityGroups=['launch-wizard-3']
)


#displays first (and only) instance id to the console log
instance = instances[0]
print(f"Launching EC2 instance {instance.id}...")

#give time for instance to start then refreshes
instance.wait_until_running()
instance.reload()

#confirmation instance is running to the console log
print(f"Instance {instance.id} is now running.")
print(f"Public DNS: {instance.public_dns_name}")
print(f"Public IP: {instance.public_ip_address}")
