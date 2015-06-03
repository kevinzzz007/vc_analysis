__author__ = 'RunzeZhao'
import pymongo
from pymongo import MongoClient
import requests
import re
from grab_articles_from_cb import *
from google_search_vc import *

o2 = open('vc_article_count_error_log.txt','w')
o2.write('vc\n')
client = MongoClient()
db = client.vc_analysis
collection = db.vc_test
collection.drop()
new_collection = pymongo.collection.Collection(db, 'vc_test',True)
cb = pycrunchbase.CrunchBase('your_crunchbase_api_access_code_here')
new_posts = []
collection = db.vc_list
input_collection = db.vc_test
error_count = 0
count = 0
for each_vc in collection.find():
    print count
    count +=1
    try:
        first_vc = each_vc
        new_vc_dict =search_cb_db_for_this_vc(first_vc)
        new_posts.append(new_vc_dict)
    except requests.exceptions.HTTPError, err:
        try:
            print err.message
            if err.response.status_code == 404:
                search_query_for_vc = new_vc_dict['vc'] + ' crunchbase'
                first_url = google_search(search_query_for_vc)
                found = re.finditer('https://www.crunchbase.com/organization/', first_url)
                for each in found:
                    vc_name_in_crunchbase_db = first_url[each.end(0):]
                vc_404_error = cb.organization(vc_name_in_crunchbase_db)
                print 'found vc name through google search'
                print vc_404_error
                search_cb_db_for_this_vc(vc_404_error)
            else:
                print new_vc_dict['vc']
        except:
            print 'weirdo'
            o2.write(new_vc_dict['vc'] + '\n')
            o2.flush()
    except:
        print 'org', new_vc_dict['vc']
        print new_vc_dict['number_of_articles_in_cb']
        o2.write(new_vc_dict['vc'] + '\n')
        o2.flush()

results = input_collection.insert_many(new_posts)
print results.inserted_ids