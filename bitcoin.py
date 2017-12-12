"""Check Bitcoin price and my current holdings.

Usage:
    bitcoin.py [--bc=AMOUNT]
    
This tool does one thing. It prints the current price of bitcoin and (by 
default) how much I currently own in bitcoin.

Options:
    -h --help           Show this screen.
    --bc=AMOUNT         The amount of bitcoin to show in dollars
"""

from docopt import docopt
import urllib3
import json
import certifi

    
if __name__ == "__main__":
    args = docopt(__doc__, version = "1")
    
    # Pull current bitcoin price
    raw_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())
    response = http.request('GET', raw_url)
    json_object = json.loads(response.data.decode('utf-8'))
    price = json_object['bpi']['USD']['rate_float']
    
    # Change default value of bc if one was entered
    bc = 0.02922975
    if args["--bc"] is not None:
        bc = float(args["--bc"])
    
    # Print price and current value
    print(price)
    print(round(price*bc, 2))
