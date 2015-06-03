__author__ = 'RunzeZhao'
import pymongo
from pymongo import MongoClient
import sys
import pycrunchbase
import requests
import json
import urllib
import re
from datetime import date, datetime
import google_search_vc

#database create and delete collections
# client = MongoClient()
# db = client.vc_analysis
# cb = pycrunchbase.CrunchBase('your_crunchbase_api_access_code_here')
# new_posts = []
# # collection = pymongo.collection.Collection(db, 'testing',True) -create a new collection
# collection = db.testing
# collection.drop()#drop a collection
#end database create and delete collections

#         error_count += 1
#         print error_count
# print error_count

# github = cb.organization('idg-ventures-usa')
# in_the_news = github.news
# try:
#     more_news = cb.more(in_the_news)
#     all_news_urls = [news.url for news in more_news]
# except urllib2.HTTPError, err:
#     if err.code == 404:
#         print 'Page not found'

# from google_search_vc import *
# number_of_google_search_results()

from pygoogle import pygoogle

g = pygoogle('quake 3 arena')
g.pages = 5
print '*Found %s results*'%(g.get_result_count())
g.get_urls()

