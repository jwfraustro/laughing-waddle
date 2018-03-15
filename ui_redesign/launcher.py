import boto3
import botocore

aws_access_key_id = 'AKIAIIRZ7G422KH7UMNQ'
aws_secret_access_key = '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'
region_name = 'us-east-1'

s3 = boto3.resource('s3',
                     aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key,
                     region_name=region_name)

data = None

version = s3.Object('laughing-waddle', 'release/v0.03/version.txt').get()['Body'].read().decode()

print(version)