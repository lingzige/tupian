# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']
    link1 = LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*')
    rules = (
        Rule(link1, callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//h1[@class="title"]/text()').get()
        author = response.xpath('//span[@class="name"]/text()').get()
        avatar = response.xpath('//a[@class="avatar"]/img/@src').get()
        # https://www.jianshu.com/p/23d323a4327c
        # https://www.jianshu.com/p/f65127b11d51?utm_campaign=maleskine&utm_content=note&utm_medium=pc_all_hots&utm_source=recommendation
        original_url = response.url
        url1 = original_url.split('?')[0]
        artical_id = url1.split('/')[-1]
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get()
        content = response.xpath('//div[@class="show-content-free"]').get()
        item = JianshuItem()
        item['title'] = title
        item['author'] = author
        item['avatar'] = avatar
        item['original_url'] = original_url
        item['artical_id'] = artical_id
        item['pub_time'] = pub_time
        item['content'] = content
        yield item