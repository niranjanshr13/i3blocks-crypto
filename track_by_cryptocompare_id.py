#!/usr/bin/env python3
import requests
import json
import os

#r = requests.get('https://www.cryptocompare.com/portfolio-public/?id=95918').text

if __name__ == '__main__':
    r = requests.get('https://www.cryptocompare.com/portfolio-public/?id=' + os.environ['CRYPTOCOMPARE_ID']).text
    for x in r.split('\n'):
        if 'portfolioManager.setPortfolioData' in x:
            scraped = x.replace('  ','').replace('portfolioManager.setPortfolioData({"Data":','').split('Success')[0].replace(',"Response":"','')
    j = json.loads(scraped)
    totalCrypto = j[0]['Members']
    for x in range(len(totalCrypto)):
        symb = totalCrypto[x]['Coin']['Symbol']
        val = totalCrypto[x]['Amount']
        print(symb + ': ' + str(val))
