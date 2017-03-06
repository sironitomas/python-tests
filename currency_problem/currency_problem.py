#!/usr/bin/python
# pylint: disable=I0011,C0103,C0111
__author__ = "Tomás Sironi"
__email__ = "sironitomas@gmail.com"
__license__ = "GPL"
__version__ = "1.0.0"

import json
import re
import urllib.request


# Function to fetch HTML data, search value with regex, and return curency
# ratio.
def to_USD(currency):
    url = 'https://www.google.com/finance/converter?a=1&from=USD&to=' + currency
    with urllib.request.urlopen(url) as response:
        html = response.read()

    regex = '1 USD = <.*?>(.*) ' + currency
    for line in html.splitlines():
        result = re.search(regex, str(line))
        if result:
            n = result.group(1)
            return float(n)
    exit('Couldn\'t convert currency')


# Function to calculate profit.
def calc_profit(c):
    ratio = to_USD(c['currency'])
    return (c['revenue'] - c['cost']) * c['conversions'] / ratio


if __name__ == "__main__":
    try:
        with open('campaigns.json') as data:
            campaigns = json.load(data)
    except FileNotFoundError:
        exit('Json file not found')
    except ValueError:
        exit('Json file is invalid')

    del data
    all_profits = []

    for camp in campaigns:
        temp = {}
        temp['id'] = camp['id']
        temp['name'] = camp['name']
        temp['total_profit'] = calc_profit(camp)
        all_profits.append(temp)

    print(json.dumps(all_profits, indent=4, sort_keys=True))
