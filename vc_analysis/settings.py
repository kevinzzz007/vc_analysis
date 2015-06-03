# -*- coding: utf-8 -*-

# Scrapy settings for vc_analysis project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'vc_analysis'

SPIDER_MODULES = ['vc_analysis.spiders']
NEWSPIDER_MODULE = 'vc_analysis.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'vc_analysis (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['vc_analysis.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "vc_analysis"
MONGODB_COLLECTION = "vc_list"