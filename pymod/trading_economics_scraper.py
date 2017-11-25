from selenium import webdriver
import json

class TECurrencyScraper:
    '''
    Scrape 'https://tradingeconomics.com/currencies'
    '''

    def scrape(self):
        metal = {'TradingEconomics': {}}
        driver = webdriver.PhantomJS()
        driver.get('https://tradingeconomics.com/currencies')
        try:
            af, bf, cf, df, ef, ff = [False] * 6
            driver.implicitly_wait(1)
            for tag_table in driver.find_elements_by_tag_name('table'):
                for tag_th in tag_table.find_elements_by_tag_name('th'):
                    if (tag_th.text == 'Price'):
                        af = True
                    if (tag_th.text == 'Day'):
                        bf = True
                    if (tag_th.text == 'Weekly'):
                        cf = True
                    if (tag_th.text == 'Monthly'):
                        df = True
                    if (tag_th.text == 'Yearly'):
                        ef = True
                    if (tag_th.text == 'Date'):
                        ff = True
                if (af & bf & cf & df & ef & ff):
                    for tag_tr in tag_table.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr'):
                        data_symbol = tag_tr.get_attribute('data-symbol')
                        price, daily_change, weekly_change, monthly_change, yearly_change, date = [
                            None] * 6
                        if (data_symbol):
                            tag_tds = tag_tr.find_elements_by_tag_name('td')
                            price, daily_change, weekly_change, monthly_change, yearly_change, date = [
                                tag_tds[2].text,
                                tag_tds[3].text,
                                tag_tds[4].text,
                                tag_tds[5].text,
                                tag_tds[6].text,
                                tag_tds[7].text
                                ]
                            metal['TradingEconomics'][data_symbol] = {
                                'price': price, 'dayly_change': daily_change, 'weekly_change': weekly_change}
            return (json.dumps(metal))
        finally:
            print('success.te.currency')
            driver.quit()


class TECountryScraper:
    '''
    Scrape 'https://tradingeconomics.com/'
    '''
    def scrape(self):
        metal = {'TradingEconomicsCountry': {}}
        driver = webdriver.PhantomJS()
        driver.get('https://tradingeconomics.com/')
        try:
            af, bf, cf, df, ef, ff = [False] * 6
            driver.implicitly_wait(1)
            for tag_table in driver.find_elements_by_tag_name('table'):
                for tag_th in tag_table.find_elements_by_tag_name('th'):
                    for tag_a in tag_th.find_elements_by_tag_name('a'):
                        if (tag_a.text == 'GDP'):
                            af = True
                        if (tag_a.text == 'GDP YoY'):
                            bf = True
                        if (tag_a.text == 'GDP QoQ'):
                            cf = True
                        if (tag_a.text == 'Interest rate'):
                            df = True
                        if (tag_a.text == 'Inflation rate'):
                            ef = True
                        if (tag_a.text == 'Jobless rate'):
                            ff = True
                if (af & bf & cf & df & ef & ff):
                    for tag_tr in tag_table.find_elements_by_tag_name('tr'):
                        tag_tds = tag_tr.find_elements_by_tag_name('td')
                        if (len(tag_tds) > 0):
                            country, gdp, gdpYoY, gdpQoQ, interest_rate, inflation_rate, jobless_rate = [
                                tag_tds[0].find_element_by_tag_name('a').text,
                                tag_tds[1].find_element_by_tag_name('a').text,
                                tag_tds[2].find_element_by_tag_name('a').text,
                                tag_tds[3].find_element_by_tag_name('a').text,
                                tag_tds[4].find_element_by_tag_name('a').text,
                                tag_tds[5].find_element_by_tag_name('a').text,
                                tag_tds[6].find_element_by_tag_name('a').text
                            ]
                            metal['TradingEconomicsCountry'][country] = {
                                'gdp': gdp,
                                'gdpYoY': gdpYoY,
                                'gdpQoQ': gdpQoQ,
                                'interest_rate': interest_rate,
                                'inflation_rate': inflation_rate,
                                'jobless_rate': jobless_rate
                                }
                        '''
                        data_symbol = tag_tr.get_attribute('data-symbol')
                        price, daily_change, weekly_change, monthly_change, yearly_change, date = [
                            None] * 6
                        if (data_symbol):
                            tds = tag_tr.find_elements_by_tag_name('td')
                            price, daily_change, weekly_change, monthly_change, yearly_change, date = [
                                tds[2].text,
                                tds[3].text,
                                tds[4].text,
                                tds[5].text,
                                tds[6].text,
                                tds[7].text
                                ]
                            metal['DailyFX'][data_symbol] = {
                                'price': price, 'dayly_change': daily_change, 'weekly_change': weekly_change}
                        '''
            return (json.dumps(metal))
        finally:
            print('success.te.country')
            driver.quit()

