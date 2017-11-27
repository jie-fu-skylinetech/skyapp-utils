from google.cloud import storage

class GCP:
	'''
	GCP
	'''
	def download_file(self, bucket_name, storage_key, local_file):
		'''
		download_file
		'''
		client = storage.Client()
		bucket = client.get_bucket(bucket_name)
		blob = bucket.blob(storage_key)
		blob.download_to_filename(local_file)

	def upload_file(self, bucket_name, local_file, storage_key):
		'''
		upload_file
		'''
		client = storage.Client()
		bucket = client.get_bucket(bucket_name)
		blob = bucket.blob(storage_key)
		blob.upload_from_filename(local_file)


'''
    def list_buckets(self):
	return  0
'''


