__author__ = 'RunzeZhao'
import urllib
import json
import time
from TorCtl import TorCtl


def google_search(search_this):
    #search_this is just a query
    query = urllib.urlencode({'q': search_this})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    # print 'Total results: %s' % data['cursor']['estimatedResultCount']
    hits = data['results']
    # print data
    # print 'hits '
    # print len(hits)
    # print hits[0]
    # print 'Top %d hits:' % len(hits)
    top_url = ''

    for h in hits:
        top_url = h['url']
        print ' ', h['url']
        break
    return top_url

def number_of_google_search_results(vc_name):
    time.sleep(50)
    try:
        query = urllib.urlencode({'q': vc_name})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        search_response = urllib.urlopen(url)
        search_results = search_response.read()
        results = json.loads(search_results)
        data = results['responseData']
        print vc_name
        print data
        print 'Total results: %s' % data['cursor']['estimatedResultCount']
        total_results = data['cursor']['estimatedResultCount']
        hits = data['results']
        # print data
        # print 'hits '
        # print len(hits)
        # print hits[0]
        # print 'Top %d hits:' % len(hits)
        top_url = ''

        for h in hits:
            top_url = h['url']
            print ' ', h['url']
            break
    except:
        time.sleep(30)
        total_results = number_of_google_search_results(vc_name)
    return total_results