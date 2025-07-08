#retrieve library to interact with aws
import boto3

#connect to ec2
ec2 = boto3.resource('ec2')

#input instance ID for which I want to terminate
instance_id = 'i-05eae16ab58f0e8f4'

#retrieve the instance by the id
instance = ec2.Instance(instance_id)

#Terminatorrrrr!
response = instance.terminate()

#confirm termination initiated in console log
print(f"Terminating instance {instance_id}...")

#give time to complete action
instance.wait_until_terminated()

#display termination success to console log
print(f"Instance {instance_id} terminated.")
