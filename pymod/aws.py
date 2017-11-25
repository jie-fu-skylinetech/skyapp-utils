import boto3
import botocore

class AWS:
    '''
    AWS
    '''
    def download_file(self, bucket_name, storage_key, local_file):
        '''
        download_file
        '''
        # Create an S3 client
        s3 = boto3.client('s3')

        try:
            s3.download_file(bucket_name, storage_key, local_file)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    def upload_file(self, bucket_name, local_file, storage_key):
        '''
        upload_file
        '''
        s3 = boto3.client('s3')

        try:
            s3.upload_file(local_file, bucket_name, storage_key)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    def list_buckets(self):
        s3 = boto3.client('s3')
        print(s3.list_buckets())