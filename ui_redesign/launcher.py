import boto3
import botocore

aws_access_key_id = 'AKIAJQPLZ5WBON7CVBLA'
aws_secret_access_key = '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'
region_name = 'us-east-1'

s3 = boto3.resource('s3',
                     aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key,
                     region_name=region_name)

data = None

version = s3.Object('laughing-waddle', 'release/version.txt').get()['Body'].read().decode()

if version > "0.03":
    print("New Version Available: "+version)
    key = ("release/v"+version+"/hsapp.exe")
    print(key)
    pause=input("")
    s3.Bucket('laughing-waddle').download_file(key, 'hsapp.exe')