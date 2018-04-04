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




class demo(CrawlSpider):
    name = "values"


    def __init__(self, *args, **kwargs):
        super(demo, self).__init__(*args, **kwargs)

        self.start_urls = [kwargs.get('start_url')]

        self.allowed_domains = []

        # start_urls = ["http://muditasol.weebly.com/"]
        url = self.start_urls[0]
        final = defaultdict(list)

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
                # for lnk in link.url:
                # req_list=set([link.url])
                # if req_list:



                # item['url_to'] = link.url

                with open('at.json', 'r') as f:
                    dis_dict = json.load(f)
                for i in dis_dict:
                        try:
                                #driver.get(response.url)
                                #next = driver.find_element_by_name(i['Name'])
                                next = response.xpath('//input[@type="text"]|//input[@type="email"]|//input[@type="password"]').extract()
                                chk = response.xpath(
                                    '//input[@type="checkbox"]|//input[@type="radio"]').extract()
                                if next:
                                    # options = Options()
                                    # options.add_argument('--headless')
                                    # options.add_argument('--disable-gpu')  ,chrome_options=options
                                    driver = webdriver.Chrome("C:\\Users\\Virus\\Downloads\\chromedriver.exe")

                                    # driver = webdriver.PhantomJS("C:\\Users\\Virus\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs")
                                    driver.get(response.url)

                                    inp = driver.find_elements_by_css_selector('input')
                                    bt = driver.find_element_by_css_selector('input')
                                    for el in inp:
                                        #driver.find_element_by_name(distro['Name']
                                        for distro in dis_dict:
                                            if el.get_attribute('name')==distro['Name']:
                                                ink=ink+1
                                                if chk:
                                                    check=check+1
                                                    el.find_element_by_value(distro['value']).click()

                                                el.send_keys(distro['value'])
                                    #for distro in dis_dict:
                                        #driver.find_element_by_name(distro['Name']).send_keys(distro['value'])
                                    #driver.find_element_by_class_name("wsite-button").click()

                                                for ele in bt:
                                                    if ele.getAttribute('type')== 'submit':
                                                        button=button+1
                                                        ele.click()
                                    #page = response.url.split("/")[-1]
                                    #if page == '':
                                    #    filename = 'quotes-Home%s.html' % page
                                    #else:
                                    #    filename = 'quotes-%s.html' % page
                                    #print("FileName: ", filename)

                                    #with open(filename, 'wb') as f:
                                    #    f.write(response.body)
                                    #self.log('Saved file %s' % filename)
                                    driver.close()
                                    self.final["input found"]=ink
                                    # self.final["checkbox or radiobutton"]=check
                                    # self.final["button clicked"]=button
                                    with open('values.json', 'w+') as outfile:
                                        json.dump(self.final, outfile)
                        except:
                                driver.close()
                                break

                    # page = response.url.split("/")[-1]
                    # if page == '':
                    #     string = 'Home%s.html' % page
                    #     filename = ''.join(e for e in string if e.isalnum())
                    #
                    #
                    # else:
                    #     string = '%s.html' % page
                    #     filename = ''.join(e for e in string if e.isalnum())
                    #
                    # print("FileName: ", filename)
                    #
                    # with open(filename, 'wb') as f:
                    #     f.write(items)
                    #     # f.write("%s\n" % items)
                    #
                    # self.log('Saved file %s' % filename)

        # yield item
        #print(response.xpath("//label/text()|//div/text()|//p/text|//h2/text()|//span/text()").re(r'(?!\s)[\w]+'))

        #driver = webdriver.Chrome("C:\\Users\\Virus\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")

        #print(response.xpath("//label/text()|//div/text()|//p/text|//h2/text()|//span/text()").re(r'(?!\s)[\w]+'))
                            # return items