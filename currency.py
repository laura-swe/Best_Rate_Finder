from lxml import html
import xml.etree.ElementTree as ET
import pandas as pd
import requests

#vbce
page = requests.get('https://www.vbce.ca/rates.html')
tree = html.fromstring(page._content)
rates = tree.xpath('//tr[@class="f32 major-rate"]//text()')
rates = [i.split('\n\t\t\t\t\t\t', 1)[0] for i in rates]
rates = filter(None, rates)
rates = [rates[x:x+5] for x in xrange(0, len(rates), 5)]
cols = ['code','country','unit', 'vbce_buys', 'vbce_sells']
df_vbce = pd.DataFrame(rates, columns=cols)
df_vbce = df_vbce.drop('country', axis=1)
df_vbce = df_vbce.set_index(['code'])

#kingmark
page = requests.get('http://www.kingmark.ca/exchange-rates')
tree = html.fromstring(page._content)
rates = tree.xpath('//table[@id="tablepress-1"]//tbody//text()')
rates = [i.split('\n', 1)[0] for i in rates]
rates = [i.split('\t', 1)[0] for i in rates]
rates = filter(None, rates)
rates = [rates[x:x+3] for x in xrange(0, len(rates), 3)]
cols = ['code', 'kingmark_buys', 'kingmark_sells']
df_kingmark = pd.DataFrame(rates, columns=cols)
df_kingmark = df_kingmark.set_index(['code'])

#scotia
page = requests.get('http://www.scotiabank.com/rates/fxrates.html')
tree = html.fromstring(page._content)
rates = tree.xpath('//table[@class="rates"]//text()')
rates = [i.split('\n', 1)[0] for i in rates]
rates = [i.split('\t', 1)[0] for i in rates]
rates = filter(None, rates)
rates = [rates[x:x+4] for x in xrange(6, len(rates), 4)]
cols = ['country', 'code', 'scotia_sells', 'scotia_buys']
df_scotia = pd.DataFrame(rates, columns=cols)
df_scotia['code'] = df_scotia['code'].apply(lambda x: x[x.find("(")+1:x.find(")")])
df_scotia = df_scotia.drop('country', axis=1)
df_scotia = df_scotia.set_index(['code'])
df_scotia = df_scotia[['scotia_buys', 'scotia_sells']]

#happy_currency
page = requests.get('http://www.happycurrency.com/rates')
tree = html.fromstring(page._content)
rates = tree.xpath('//table[@class="currencyTBL"]//tbody//text()')
rates = [i.split('\n', 1)[0] for i in rates]
rates = [i.split('\t', 1)[0] for i in rates]
rates = filter(None, rates)
rates = [rates[x:x+5] for x in xrange(5, len(rates), 5)]
cols = ['country', 'currency', 'code', 'happy_currency_buys', 'happy_currency_sells']
df_happy = pd.DataFrame(rates, columns=cols)
df_happy = df_happy.drop('country', axis=1)
df_happy = df_happy.drop('currency', axis=1)
df_happy = df_happy.set_index(['code'])

#charlie
page = requests.get('http://www.charliescurrency.ca/rateswithcss.xml')
tree = ET.fromstring(page._content)
codes =[]
sells = []
buys =[]
for element in tree.findall('RATE'):
    codes.append(element.find('ISO').text)
    sells.append(element.find('WESELL').text)
    buys.append(element.find('WEBUY').text)
df_charlie = pd.DataFrame({'code': codes, 'charlie_buys': buys, 'charlie_sells': sells})
df_charlie = df_charlie.set_index(['code'])
#flush expensive variables
del codes
del sells
del buys
del element

#gastown
page = requests.get('http://www.gciexchange.com/rates.php')
tree = html.fromstring(page._content)
rates = tree.xpath('//table[@class="col-md-12 table-striped table-condensed cf"]//tbody//text()')
rates = [i.split('\n', 1)[0] for i in rates]
rates = [i.split('\t', 1)[0] for i in rates]
rates = filter(None, rates)
rates = [rates[x:x+7] for x in xrange(0, len(rates), 7)]
cols = ['country', 'currency', 'code', 'gastown_buys', 'gastown_sells', 'inv1', 'inv2']
df_gastown = pd.DataFrame(rates, columns=cols)
df_gastown = df_gastown.drop('inv1', axis=1)
df_gastown = df_gastown.drop('inv2', axis=1)
df_gastown = df_gastown.drop('country', axis=1)
df_gastown = df_gastown.drop('currency', axis=1)
df_gastown = df_gastown.set_index(['code'])

#join dataframes
df = df_vbce.join(df_kingmark, how='outer')
df = df.join(df_scotia, how='outer')
df = df.join(df_happy, how='outer')
df =  df.join(df_charlie, how='outer')
df =  df.join(df_gastown, how='outer')

ls_currency = ['USD', 'AUD', 'GBP', 'CHF', 'COP', 'EUR', 'JPY', 'NZD', 'ZAR']
df = df.filter(ls_currency, axis=0)

ls_sells = ['vbce_sells', 'kingmark_sells', 'scotia_sells', 'happy_currency_sells', 'charlie_sells', 'gastown_sells']
ls_buys = ['vbce_buys', 'kingmark_buys', 'scotia_buys', 'happy_currency_buys', 'charlie_buys', 'gastown_buys']

df_sells = df.filter(ls_sells, axis=1)
df_buys = df.filter(ls_buys, axis=1)

eur = df_buys[df_buys.index=='EUR']
df_max = eur[eur.astype(float).idxmax(axis=1)]
writer = pd.ExcelWriter("output.xlsx")
eur.to_excel(writer, 'EUR Buys', index_label='Code')
df_buys.to_excel(writer, 'Buys', index_label='Code')
df_sells.to_excel(writer, 'Sells', index_label='Code')
df_max.to_excel(writer, 'Bet Buys', index_label='Code')

print(df_max)
pass