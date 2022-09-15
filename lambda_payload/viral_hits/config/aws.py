import logging
import boto3
from botocore.exceptions import ClientError
import os

BUCKET_REGION = 'ap-southeast-1'

def create_bucket(bucket_name):
    """Create an S3 bucket in the ap-southeast-1 region

    :param bucket_name: Bucket to create
    :return: True if bucket created, else False
    """
    region = BUCKET_REGION

    # Create bucket
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False

    print(f'Bucket {bucket_name} successfully created!')
    return True


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    
    print(f'File {file_name} was successfully uploaded to {object_name} in {bucket} bucket!')
    return True