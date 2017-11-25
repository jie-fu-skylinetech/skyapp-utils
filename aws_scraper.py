import os, tempfile
from pymod.dailyfx_scraper import DFCurrencyScraper
from pymod.trading_economics_scraper import TECurrencyScraper, TECountryScraper
from pymod.aws import AWS

json = TECountryScraper().scrape()

fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
fp.write(json)
fp.seek(0)
fp.close()

AWS().upload_file("st-country",  fp.name, 'te.country.json')
os.remove(fp.name)

print ("success.aws.te.country")
