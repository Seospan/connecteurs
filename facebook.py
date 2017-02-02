#!/usr/bin/python
# https://developers.facebook.com/docs/marketing-api/insights-api/getting-started/v2.8
# https://developers.facebook.com/docs/marketing-api/sdks

#Add to header of your file
from facebookads.api import FacebookAdsApi
from facebookads import FacebookAdsApi
from facebookads import objects
from facebookads.objects import AdUser, Campaign, AdAccount

#Initialize a new Session and instantiate an API object:


# VILLAGEMAP
my_app_id = '218109678382842'
my_app_secret = '98ede9f8eabff3b486f53274e78f1ef5'
# my_access_token = 'EAADGXp3m7voBADS07Q9HANwXa5r9bxFSfQDN8fNP48mS3BQKqyNMBAHZC4O39x2mmiBESlM4ufZBfoDZCQT2z2PSy0v66ZA0SoOEGNWgnH50u79PH5fZC1jJTMVDEvvbviV1QWULOupDfOZBHKdSO7wRmMZAuxTN6agJaq1vMBRZB8tHZA7K4efTPPlhVyZAxnVZCgZD'
my_access_token = 'EAADGXp3m7voBABmZBPmOYGTpu2F8XBERWUUxnN1adEhozMdAFFNNEqtG0PoDH5hVxBZBJGRqwFgiNJNjZBZBqiJkBsmJWHaZBsJfryK0SRZByg0332PPYLCZByHq3ExZBhZAjG5HjGYwyOvX804ogPd9ZBfNXX0cZBst3ouJsHZAjs03q8snmOyMyRRepPlM5lkxazUZD'

# SOIREE GEEK
#my_app_id = '225503937640668'
#my_app_secret = '6026c941442393db03eabe507e8c1b3c'
#my_access_token = 'EAADNGDoZAONwBADZByURWqqmSZCzZBiQuQgNe1NVuwbZAjWCLC7JkMN5HDZAtAWpBerZCo7DHZBYEwwY5Owwpg3VozAFJQqAn2Da9ZCZCNGMLbZAyyw2joX5NwKM0XB0Dl5ZASpsuu83UyqT3XQ06o2unqJvrjTZC0fM43AT2NAzZAkeGmKwJmIEXDRZBLU'

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = AdUser(fbid='me')
my_accounts = list(me.get_ad_accounts())

print("Account id : "+my_accounts[1]["id"])

#Ad account
account = objects.AdAccount(my_accounts[1]["id"])
#account = objects.AdAccount("act_1456884277904147")
campaigns = account.get_campaigns(fields=[Campaign.Field.name, Campaign.Field.objective])

print(campaigns)
#for obj in objects:
#    print(obj[Campaign.Field.name])
