from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION
import boto3

ec2 = boto3.client(
    'ec2',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

print("✅ TEST SUCCESS:", ec2.describe_regions())