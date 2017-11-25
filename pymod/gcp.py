

class GCP:
    '''
    GCP
    '''
    def download_file(self, bucket_name, storage_key, local_file):
        '''
        download_file
        '''

    def upload_file(self, bucket_name, local_file, storage_key):
        '''
        upload_file
        '''

'''
    def list_buckets(self):
	return  0
'''

from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('st-country')
blob = bucket.blob('test.txt')
#blob.upload_from_string('this is test content!')
