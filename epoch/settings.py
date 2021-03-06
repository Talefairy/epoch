# -*- coding: utf-8 -*-

# Scrapy settings for epoch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'epoch'

SPIDER_MODULES = ['epoch.spiders']
NEWSPIDER_MODULE = 'epoch.spiders'
FILES_STORE = 'E:/project/file'
IMAGES_STORE = 'E:/project/img'
FEED_EXPORT_ENCODING = 'utf-8'
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = False

ITEM_PIPELINES = {
    # 'epoch.pipelines.jiandan_img_pipelines.JiandanPipeline': 5,
    # 'epoch.pipelines.domubiji_txt_pipelines.DaomubijiPipeline': 2,
    # 'epoch.pipelines.pdf_pipelines.PdfdownloadPipeline': 3,
    # 'epoch.pipelines.mofcom_pipelines.MofcomPipeline': 4,
    # 'epoch.pipelines.csdn_pipelines.CSDNPipelines': 6,
    # 'epoch.pipelines.ip_proxy_pipelines.IPProxyPipelines': 1,
    # 'epoch.pipelines.zhugefang_pipelines.ZhugefangPipeline': 1,
    'epoch.pipelines.lianjia_pipelines.LianjiaPipeline': 1
}


DOWNLOADER_MIDDLEWARES = {
    # 'epoch.middlewares.random_user_agent.RandomUserAgent': 1,
    # 'epoch.middlewares.random_proxy.RandomProxy': 2,
}

# LOG_ENCODING = 'utf-8'
# LOG_FILE = 'E:/project/log'
# LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
# LOG_LEVEL = 'DEBUG'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'epoch (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'epoch.middlewares.EpochSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'epoch.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'epoch.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
