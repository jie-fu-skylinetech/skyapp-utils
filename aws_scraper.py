import os, sys, tempfile
from pymod.dailyfx_scraper import DFCurrencyScraper
from pymod.trading_economics_scraper import TECurrencyScraper, TECountryScraper
from pymod.aws import AWS

class AWSScraper:
    def scrape(self):
        fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
        fp.write(TECountryScraper().scrape())
        fp.seek(0)
        fp.close()
        AWS().upload_file("st-country", fp.name , 'te.country.json')
        os.remove(fp.name)

        fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
        fp.write(TECurrencyScraper().scrape())
        fp.seek(0)
        fp.close()
        AWS().upload_file("st-currency", fp.name , 'te.currency.json')
        os.remove(fp.name)

        fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
        fp.write(DFCurrencyScraper().scrape())
        fp.seek(0)
        fp.close()
        AWS().upload_file("st-currency", fp.name , 'df.currency.json')
        os.remove(fp.name)

        print ("success.aws.te.country")

