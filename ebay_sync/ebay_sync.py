from ebaysdk.trading import Connection as Trading
import datetime
import json

api = Trading(config_file='ebay.yaml')
response = api.execute('GetSellerList', {'GranularityLevel':'Coarse','EndTimeFrom':datetime.datetime.now(),'EndTimeTo':(datetime.timedelta(weeks=1)+datetime.datetime.now()),'Pagination':{'EntriesPerPage':'10'}})
print(response.dict())

items = response.dict().get('ItemArray').get('Item')

try:
    for item in items:
        print(item['Title'])
        print(item['SKU'])
        print(item['ConditionDisplayName'])
        print(item['ConditionDescription'])
        print(item['SellingStatus']['CurrentPrice']['value'])
except Exception as e:
    print(e)