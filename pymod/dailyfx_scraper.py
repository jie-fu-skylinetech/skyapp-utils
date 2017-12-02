from selenium import webdriver
import json


class DFCurrencyScraper:
    '''
    Scrape 'dailyfx.com'
    '''

    def scrape(self):
        metal = {'dailyfx': {}}
        driver = webdriver.PhantomJS()
        driver.get('https://www.dailyfx.com/forex-rates')
        try:
            for x in range(3):
                print('Running for {} '.format(x))
                if self.build(driver.find_element_by_tag_name('html'), metal):
                    return (json.dumps(metal))
                else:
                    print('Waiting the page to load')
                    driver.implicitly_wait(0.5)
        finally:
            print('success.df')
            driver.quit()

    def build(self, root, target):
        bid_found = False
        ask_found = False
        spread_found = False

        for tag_table in root.find_elements_by_tag_name('table'):
            for tag_th in tag_table.find_elements_by_tag_name('th'):
                if (tag_th.text == 'Bid'):
                    bid_found = True
                if (tag_th.text == 'Ask'):
                    ask_found = True
                if (tag_th.text == 'Spread'):
                    spread_found = True
            if (bid_found & ask_found & spread_found):
                for tag_tr in tag_table.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr'):
                    data_market_id = tag_tr.get_attribute('data-market-id')
                    bid_value = ''
                    ask_value = ''
                    spread_value = ''
                    if (data_market_id):
                        for tag_span in tag_tr.find_elements_by_tag_name('span'):
                            if tag_span.get_attribute('data-type') == 'bid':
                                bid_value = tag_span.get_attribute(
                                    'data-value')
                            if tag_span.get_attribute('data-type') == 'ask':
                                ask_value = tag_span.get_attribute(
                                    'data-value')
                            if tag_span.get_attribute('id') == '{}-spread'.format(data_market_id):
                                spread_value = tag_span.text
                        if (bid_value == '') & (ask_value == '') & (spread_value == ''):
                            return False
                        else:
                            target['dailyfx'][data_market_id] = {
                                'bid': bid_value, 'ask': ask_value, 'spread': spread_value}
        return True
