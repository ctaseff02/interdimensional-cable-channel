from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader
from PIL import Image
from six import BytesIO
from keywordcrawl import KeywordGoogleImageCrawler, KeywordNameDownloader

def crawl(keywords):

    for image in keywords:
        google_crawler = KeywordGoogleImageCrawler(
            downloader_cls=KeywordNameDownloader,
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=1,
            storage={'root_dir': r'main\bot\images'})

        google_crawler.crawl(keyword = image, max_num = 1, max_size=(1200, 1200))   