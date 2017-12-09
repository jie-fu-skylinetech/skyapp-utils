import requests

running_on_gcp = False
running_on_aws = False
try:
	metadata_server = "http://metadata.google.internal"
	metadata_flavor = {'Metadata-Flavor' : 'Google'}
	r = requests.get(metadata_server)
	if (r.headers['Metadata-Flavor']=='Google'):
		running_on_gcp = True
except Exception:
	pass

try:
	metadata_server = 'http://169.254.169.254/latest/meta-data/ami-id'
	r = requests.get(metadata_server)
	if 'ami' in r.text:
		running_on_aws = True
except :
	pass

print("Running on GCP : {}".format(running_on_gcp))
print("Running on AWS : {}".format(running_on_aws))
if running_on_gcp:	
	print('Running on GCP')
	from gcp_scraper import  GCPScraper
	GCPScraper().scrape()
else:
	if running_on_aws:	
		print('Running on AWS')
		from aws_scraper import  AWSScraper
		AWSScraper().scrape()
	else:	
		print('Running on other')
