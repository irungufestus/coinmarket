from requests import get
import json
from datetime import datetime
import time

url='https://production.api.coindesk.com/v2/tb/price/ticker?assets='

def scraper(args):
    if len (args)== 0:
        raise Exception ("missinf args...")
    symbols=args[0]
    final_url=url+symbols
    individual_symbol=symbols.split(',')
    results={}
    i=0
    while i< 20:
        result=get(final_url)
        json_data=result.json()
        
        
        for s in individual_symbol:
            if s not in results:
                results[s]=[]
            coin_data=json_data['data'][s]
            result.append( {
                "iso":coin_data['iso'],
                "name":coin_data['name'],
                "current_price":coin_data["ohlc"]["c"],
                "time":datetime.fromtimestamp(int(coin_data['ts']/1000)).isoformat()
            })
            time.sleep(15)
            i=i+1
    return results
d
    
    
    