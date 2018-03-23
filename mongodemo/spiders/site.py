from collections import defaultdict

import scrapy
import re
import json

from scrapy import Selector
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from mongodemo.items import MongodemoItem
from tldextract import extract


class site(CrawlSpider):
    name = "sitemap"
    val = defaultdict(list)
    va = defaultdict(list)
    abc = defaultdict(list)
    def __init__(self, *args, **kwargs):
        super(site, self).__init__(*args, **kwargs)

        self.start_urls = [kwargs.get('start_url')]

        self.allowed_domains = []

        # start_urls = ["http://muditasol.weebly.com/"]
        url = self.start_urls[0]
        chk=url.split("//")[-1].split("/")[0]
        # tsd, td, tsu = extract(self.start_urls[0])  # prints abc, hostname, com
        # url = td + '.' + tsu
        self.allowed_domains.append(chk)
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_items(self, response):
        items = []
        url=[]
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        for link in links:
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    url.append(response.url)
                    ul = set(url)
                    # lt = list(ul)
                    if link.url in ul:
                        is_allowed = True


            if is_allowed:

                # ---------------------------------------------------------------------------------------
                ak = set(response.xpath('//a/@href').extract())
                # lnk[response.url] = set(response.xpath('//a/@href').extract())
                # val = defaultdict(list)
                # .rstrip('/')
                # empty = {'/'}
                # aaa= [x.discard(empty) for x in ak]
                # ak.remove('/')
                aa = list(ak)
                for start in self.start_urls:
                    ab = [start + suit.lstrip('/') for suit in aa]
                    self.val[response.url] = ab

                    # st = str(aa)
                for start in self.start_urls:
                    for key in self.val.keys():
                        if key != start:
                            aek = self.val.get(start)
                            mk = self.val.get(key)
                            for i in aek:
                                if i in mk:
                                    # print "found " + i
                                    mk.remove(i)

                for keey in self.val.keys():
                    ark = self.val.get(keey)
                    if keey in ark:
                        ark.remove(keey)

                final_list = []
                for keys, num in self.val.items():
                    if num not in final_list:
                        final_list.append(num)
                    else:
                        ann = keys
                # for it in final_list:
                #      for num in ann:
                #          ann.remove(num)

                if ann:
                    for k, v in self.val.items():
                        if ann in k:
                            vk = self.val.get(k)
                            for vt in final_list:
                                if vt in vk:
                                    vk.remove(v)
                # for start in self.start_urls:
                #     for key in self.val.keys():
                #         if key == start:
                #             self.va[start]=self.val.get(start)
                            # self.val.pop(start, None)
                            # self.abc["text"]=start

                        # if self.val[start]:
                            # self.val.pop(start,self.val.get(start))
                        #     self.val.pop(start)

                # self.abc["children"]={k: self.va.get(v, v) for k, v in self.val.items()}
#-----------------------------------------
                k_list = []
                for ke, nu in self.val.items():
                    if ke not in k_list:
                        k_list.append(ke)
                ll=len(k_list)
                for ii in range(0,ll):
                    for keyss in self.val.keys():
                            ae = self.val.get(k_list[ii])
                            mkd = self.val.get(keyss)
                            for i in ae:
                                if i in mkd:
                                    # print "found " + i
                                    mkd.remove(i)
#----------------------------------------
                for ii in range(0,ll):
                    for kk in self.val.keys():
                        tt = self.val.get(k_list[ii])
                        if kk in tt:
                            tt.remove(kk)

#-----------------------------------------
                for start in self.start_urls:
                    man=start


                for kk,vv in self.val.items():
                    if kk != start:
                        self.va[kk]=vv



                # for kk,vv in self.val.items():
                #     if kk != start:
                #         for aaa in abk:
                self.abc[man]=self.va

                with open('tst.json', 'w+') as outfile:
                    json.dump(self.abc, outfile)
