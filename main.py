import requests
metadata_server = "http://metadata.google.internal"
metadata_flavor = {'Metadata-Flavor' : 'Google'}
r = requests.get(metadata_server)
if (r.headers['Metadata-Flavor']=='Google'):
	print('Running on GCP')
	from gcp_scraper import  GCPScraper
	GCPScraper().scrape()
else:
	print('Running on other')
