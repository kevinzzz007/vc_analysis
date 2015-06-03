__author__ = 'RunzeZhao'
import pycrunchbase
import time

def search_cb_db_for_this_vc(vc_org):
    time.sleep(1)
    cb = pycrunchbase.CrunchBase('your_crunchbase_api_access_code_here')
    first_vc_title_without_hyphen = ''.join(vc_org['title'])
    first_vc_title_with_hyphen = '-'.join(first_vc_title_without_hyphen.split(' '))
    org = cb.organization(first_vc_title_with_hyphen)
    org_founding_time = org.founded_on
    in_the_news = org.news
    more_news = cb.more(in_the_news)
    all_news_urls = [news.url for news in more_news]
    # o1.write(first_vc_title_without_hyphen + '\t' + str(len(all_news_urls)) + '\t' + str(org_founding_time)[0:10] +'\n')
    new_vc_dict = {'vc':first_vc_title_without_hyphen,'number_of_articles_in_cb':len(all_news_urls),
                      'founded_date':str(org_founding_time)[0:10]}
    return new_vc_dict
