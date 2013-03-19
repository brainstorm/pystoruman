# Scrapy settings for pystoruman project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'storuman.se'

SPIDER_MODULES = ['pystoruman.spiders']
NEWSPIDER_MODULE = 'pystoruman.spiders'

STORUMAN_USER = ""
STORUMAN_PASSWORD = ""

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pystoruman (+http://www.yourdomain.com)'
