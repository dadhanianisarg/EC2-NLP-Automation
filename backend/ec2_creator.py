import boto3
from backend.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION


def create_ec2(config):
    ec2 = boto3.client(
        'ec2',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

    response = ec2.run_instances(
        ImageId='ami-0f5ee92e2d63afc18',  # Mumbai
        InstanceType=config["instance_type"],  # t3.micro
        MinCount=1,
        MaxCount=1,
        KeyName='my-key-pair'  # ⚠️ must exist
    )

    return response['Instances'][0]['InstanceId']