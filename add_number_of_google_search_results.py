__author__ = 'RunzeZhao'
import pymongo
from pymongo import MongoClient
import sys
from google_search_vc import *

client = MongoClient()
db = client.vc_analysis
collection = db.vc_test

for each_vc in collection.find():
    print each_vc
    # collection.update({'_id':each_vc['_id']}, {'$set': {'google_results_count':60}})
    vc_name = each_vc['vc']
    google_result_count = int(number_of_google_search_results(vc_name))
    if google_result_count!= 0:
        collection.update({'_id':each_vc['_id']}, {'$set': {'google_results_count':google_result_count}})
        #comment