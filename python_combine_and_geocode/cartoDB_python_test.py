from cartodb import CartoDBOAuth, CartoDBException
from secret import *

cl = CartoDBOAuth(CONSUMER_KEY, CONSUMER_SECRET, user, password, cartodb_domain)
try:
    print cl.sql("select * from basicinfo where site_id='DC20687'")
except CartoDBException as e:
    print ("some error ocurred", e)