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




class mongodemo(CrawlSpider):
    name = "mongodemo"


    def __init__(self, *args, **kwargs):
        super(mongodemo, self).__init__(*args, **kwargs)

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
                # for lnk in link.url:
                # req_list=set([link.url])
                # if req_list:



                item = MongodemoItem()
                val=defaultdict(list)
                met=defaultdict(list)
                di=defaultdict(list)
                fom=defaultdict(list)
                val['projecturl'] = allowed_domain
                val['title'] = response.xpath('//title/text()').extract()
                met['meta_property'] = response.xpath('//meta/@property').extract()
                met['meta_content'] = response.xpath('//meta/@content').extract()
                met['meta_charset'] = response.xpath('//meta/@charset').extract()
                met['meta_httpequiv'] = response.xpath('//meta/@http-equiv').extract()
                met['meta_name'] = response.xpath('//meta/@name').extract()
                met['meta_scheme'] = response.xpath('//meta/@scheme').extract()
                val['link_a'] = response.xpath('//a/@href').extract()
                di['div_id'] = response.xpath('//div/@id').extract()
                di['div_class'] = response.xpath('//div/@class').extract()
                di['div_align'] = response.xpath('//div/@align').extract()
                di['div_form'] = response.xpath('//div/@form').extract()
                di['div_input'] = response.xpath('//div/@input').extract()
                di['div_input_accept'] = response.xpath('//div/input/@accept').extract()
                di['div_input_align'] = response.xpath('//div/input/@align').extract()
                di['div_input_alt'] = response.xpath('//div/input/@alt').extract()
                di['div_input_autocomplete'] = response.xpath('//div/input/@autocomplete').extract()
                di['div_input_autofocus'] = response.xpath('//div/input/@autofocus').extract()
                di['div_input_checked'] = response.xpath('//div/input/@checked').extract()
                di['div_input_dirname'] = response.xpath('//div/input/@dirname').extract()
                di['div_input_disabled'] = response.xpath('//div/input/@disabled').extract()
                di['div_input_form'] = response.xpath('//div/input/@form').extract()
                di['div_input_formaction'] = response.xpath('//div/input/@formaction').extract()
                di['div_input_formenctype'] = response.xpath('//div/input/@formenctype').extract()
                di['div_input_formmethod'] = response.xpath('//div/input/@formmethod').extract()
                di['div_input_formnodiidate'] = response.xpath('//div/input/@formnodiidate').extract()
                di['div_input_formtarget'] = response.xpath('//div/input/@formtarget').extract()
                di['div_input_height'] = response.xpath('//div/input/@height').extract()
                di['div_input_list'] = response.xpath('//div/input/@list').extract()
                di['div_input_max'] = response.xpath('//div/input/@max').extract()
                di['div_input_maxlenght'] = response.xpath('//div/input/@maxlenght').extract()
                di['div_input_min'] = response.xpath('//div/input/@min').extract()
                di['div_input_multiple'] = response.xpath('//div/input/@multiple').extract()
                di['div_input_name'] = response.xpath('//div/input/@name').extract()
                di['div_input_pattern'] = response.xpath('//div/input/@pattern').extract()
                di['div_input_placeholder'] = response.xpath('//div/input/@placeholder').extract()
                di['div_input_readonly'] = response.xpath('//div/input/@readonly').extract()
                di['div_input_required'] = response.xpath('//div/input/@required').extract()
                di['div_input_size'] = response.xpath('//div/input/@size').extract()
                di['div_input_src'] = response.xpath('//div/input/@src').extract()
                di['div_input_step'] = response.xpath('//div/input/@step').extract()
                di['div_input_type'] = response.xpath('//div/input/@type').extract()
                di['div_input_diue'] = response.xpath('//div/input/@diue').extract()
                di['div_input_id'] = response.xpath('//div/input/@id').extract()
                di['div_input_class'] = response.xpath('//div/input/@class').extract()
                di['div_input_width'] = response.xpath('//div/input/@width').extract()
                di['div_input_role'] = response.xpath('//div/input/@role').extract()
                di['div_textarea'] = response.xpath('//div/textarea').extract()
                di['div_textarea_autofocus'] = response.xpath('//div/textarea/@autofocus').extract()
                di['div_textarea_cols'] = response.xpath('//div/textarea/@cols').extract()
                di['div_textarea_dirname'] = response.xpath('//div/textarea/@dirname').extract()
                di['div_textarea_disabled'] = response.xpath('//div/textarea/@disabled').extract()
                di['div_textarea_form'] = response.xpath('//div/textarea/@form').extract()
                di['div_textarea_maxlenght'] = response.xpath('//div/textarea/@maxlenght').extract()
                di['div_textarea_name'] = response.xpath('//div/textarea/@name').extract()
                di['div_textarea_id'] = response.xpath('//div/textarea/@id').extract()
                di['div_textarea_class'] = response.xpath('//div/textarea/@class').extract()
                di['div_textarea_placeholder'] = response.xpath('//div/textarea/@placeholder').extract()
                di['div_textarea_readonly'] = response.xpath('//div/textarea/@readonly').extract()
                di['div_textarea_rows'] = response.xpath('//div/textarea/@rows').extract()
                di['div_textarea_required'] = response.xpath('//div/textarea/@required').extract()
                di['div_textarea_wrap'] = response.xpath('//div/textarea/@wrap').extract()
                di['div_button'] = response.xpath('//div/button').extract()
                di['div_button_form'] = response.xpath('//div/button/@form').extract()
                di['div_button_formaction'] = response.xpath('//div/button/@formaction').extract()
                di['div_button_formenctype'] = response.xpath('//div/button/@formenctype').extract()
                di['div_button_formmethod'] = response.xpath('//div/button/@formmethod').extract()
                di['div_button_formnodiidate'] = response.xpath('//div/button/@formnodiidate').extract()
                di['div_button_formtarget'] = response.xpath('//div/button/@formtarget').extract()
                di['div_button_name'] = response.xpath('//div/button/@name').extract()
                di['div_button_type'] = response.xpath('//div/button/@type').extract()
                di['div_button_diue'] = response.xpath('//div/button/@diue').extract()
                di['div_button_id'] = response.xpath('//div/button/@id').extract()
                di['div_button_class'] = response.xpath('//div/button/@class').extract()
                di['div_button_autofocus'] = response.xpath('//div/button/@autofocus').extract()
                di['div_button_disabled'] = response.xpath('//div/button/@disabled').extract()
                di['div_select'] = response.xpath('//div/button/@disabled').extract()
                di['div_select_form'] = response.xpath('//div/select/@form').extract()
                di['div_select_name'] = response.xpath('//div/select/@name').extract()
                di['div_select_type'] = response.xpath('//div/select/@type').extract()
                di['div_select_diue'] = response.xpath('//div/select/@diue').extract()
                di['div_select_autofocus'] = response.xpath('//div/select/@autofocus').extract()
                di['div_select_disabled'] = response.xpath('//div/select/@disabled').extract()
                di['div_select_multiple'] = response.xpath('//div/select/@multiple').extract()
                di['div_select_size'] = response.xpath('//div/select/@size').extract()
                di['div_select_required'] = response.xpath('//div/select/@required').extract()
                di['div_select_id'] = response.xpath('//div/select/@id').extract()
                di['div_select_class'] = response.xpath('//div/select/@class').extract()
                di['div_select_option'] = response.xpath('//div/select/@option').extract()
                di['div_select_option_disabled'] = response.xpath('//div/select/option/@disabled').extract()
                di['div_select_option_label'] = response.xpath('//div/select/option/@label').extract()
                di['div_select_option_selected'] = response.xpath('//div/select/option/@selected').extract()
                di['div_select_option_id'] = response.xpath('//div/select/option/@id').extract()
                di['div_select_option_class'] = response.xpath('//div/select/option/@class').extract()
                di['div_select_optgroup_label'] = response.xpath('//div/select/optgroup/@label').extract()
                di['div_select_optgroup_id'] = response.xpath('//div/select/optgroup/@id').extract()
                di['div_select_optgroup_class'] = response.xpath('//div/select/optgroup/@class').extract()
                di['div_fieldset'] = response.xpath('//div/@fieldset').extract()
                di['div_fieldset_disabled'] = response.xpath('//div/fieldset/@disabled').extract()
                di['div_fieldset_id'] = response.xpath('//div/fieldset/@id').extract()
                di['div_fieldset_class'] = response.xpath('//div/fieldset/@class').extract()
                di['div_fieldset_name'] = response.xpath('//div/fieldset/@name').extract()
                di['div_label'] = response.xpath('//div/@label').extract()
                di['div_label_for'] = response.xpath('//div/label/@for').extract()
                di['div_label_id'] = response.xpath('//div/label/@id').extract()
                di['div_label_class'] = response.xpath('//div/label/@class').extract()
                di['div_label_form'] = response.xpath('//div/label/@form').extract()
                di['div_a'] = response.xpath('//div/@a').extract()
                di['div_a_charset'] = response.xpath('//div/a/@charset').extract()
                di['div_a_coords'] = response.xpath('//div/a/@coords').extract()
                di['div_a_download'] = response.xpath('//div/a/@download').extract()
                di['div_a_href'] = response.xpath('//div/a/@href').extract()
                di['div_a_hreflang'] = response.xpath('//div/a/@hreflang').extract()
                di['div_a_media'] = response.xpath('//div/a/@media').extract()
                di['div_a_name'] = response.xpath('//div/a/@name').extract()
                di['div_a_rel'] = response.xpath('//div/a/@rel').extract()
                di['div_a_shape'] = response.xpath('//div/a/@shape').extract()
                di['div_a_target'] = response.xpath('//div/a/@target').extract()
                di['div_a_type'] = response.xpath('//div/a/@type').extract()
                di['div_a_role'] = response.xpath('//div/a/@role').extract()
                di['div_a_id'] = response.xpath('//div/a/@id').extract()
                di['div_a_class'] = response.xpath('//div/a/@class').extract()
                di['div_a_form'] = response.xpath('//div/a/@form').extract()

                fom['form_id'] = response.xpath('//form/@id').extract()
                fom['form_class'] = response.xpath('//form/@class').extract()
                fom['form_accept'] = response.xpath('//form/@accept').extract()
                fom['form_action'] = response.xpath('//form/@action').extract()
                fom['form_autocomplete'] = response.xpath('//form/@autocomplete').extract()
                fom['form_method'] = response.xpath('//form/@method').extract()
                fom['form_name'] = response.xpath('//form/@name').extract()
                fom['form_nofomidate'] = response.xpath('//form/@nofomidate').extract()
                fom['form_target'] = response.xpath('//form/@target').extract()
                fom['form_enctype'] = response.xpath('//form/@enctype').extract()
                fom['form_accept_charset'] = response.xpath('//form/@accept-charset').extract()

                fom['form_input_form'] = response.xpath('//form/input/@form').extract()
                fom['form_input_formaction'] = response.xpath('//form/input/@formaction').extract()
                fom['form_input_formenctype'] = response.xpath('//form/input/@formenctype').extract()
                fom['form_input_formmethod'] = response.xpath('//form/input/@formmethod').extract()
                fom['form_input_formnofomidate'] = response.xpath('//form/input/@formnofomidate').extract()
                fom['form_input_formtarget'] = response.xpath('//form/input/@formtarget').extract()
                fom['form_input'] = response.xpath('//form/@input').extract()
                fom['form_input_accept'] = response.xpath('//form/input/@accept').extract()
                fom['form_input_align'] = response.xpath('//form/input/@align').extract()
                fom['form_input_alt'] = response.xpath('//form/input/@alt').extract()
                fom['form_input_autocomplete'] = response.xpath('//form/input/@autocomplete').extract()
                fom['form_input_autofocus'] = response.xpath('//form/input/@autofocus').extract()
                fom['form_input_checked'] = response.xpath('//form/input/@checked').extract()
                fom['form_input_dirname'] = response.xpath('//form/input/@dirname').extract()
                fom['form_input_disabled'] = response.xpath('//form/input/@disabled').extract()
                fom['form_input_height'] = response.xpath('//form/input/@height').extract()
                fom['form_input_list'] = response.xpath('//form/input/@list').extract()
                fom['form_input_max'] = response.xpath('//form/input/@max').extract()
                fom['form_input_maxlenght'] = response.xpath('//form/input/@maxlenght').extract()
                fom['form_input_min'] = response.xpath('//form/input/@min').extract()
                fom['form_input_multiple'] = response.xpath('//form/input/@multiple').extract()
                fom['form_input_name'] = response.xpath('//form/input/@name').extract()
                fom['form_input_pattern'] = response.xpath('//form/input/@pattern').extract()
                fom['form_input_placeholder'] = response.xpath('//form/input/@placeholder').extract()
                fom['form_input_readonly'] = response.xpath('//form/input/@readonly').extract()
                fom['form_input_required'] = response.xpath('//form/input/@required').extract()
                fom['form_input_size'] = response.xpath('//form/input/@size').extract()
                fom['form_input_src'] = response.xpath('//form/input/@src').extract()
                fom['form_input_step'] = response.xpath('//form/input/@step').extract()
                fom['form_input_type'] = response.xpath('//form/input/@type').extract()
                fom['form_input_fomue'] = response.xpath('//form/input/@fomue').extract()
                fom['form_input_id'] = response.xpath('//form/input/@id').extract()
                fom['form_input_class'] = response.xpath('//form/input/@class').extract()
                fom['form_input_width'] = response.xpath('//form/input/@width').extract()
                fom['form_input_role'] = response.xpath('//form/input/@role').extract()

                fom['form_textarea_form'] = response.xpath('//form/textarea/@form').extract()
                fom['form_textarea'] = response.xpath('//form/textarea').extract()
                fom['form_textarea_autofocus'] = response.xpath('//form/textarea/@autofocus').extract()
                fom['form_textarea_cols'] = response.xpath('//form/textarea/@cols').extract()
                fom['form_textarea_dirname'] = response.xpath('//form/textarea/@dirname').extract()
                fom['form_textarea_disabled'] = response.xpath('//form/textarea/@disabled').extract()

                fom['form_textarea_maxlenght'] = response.xpath('//form/textarea/@maxlenght').extract()
                fom['form_textarea_name'] = response.xpath('//form/textarea/@name').extract()
                fom['form_textarea_id'] = response.xpath('//form/textarea/@id').extract()
                fom['form_textarea_class'] = response.xpath('//form/textarea/@class').extract()
                fom['form_textarea_placeholder'] = response.xpath('//form/textarea/@placeholder').extract()
                fom['form_textarea_readonly'] = response.xpath('//form/textarea/@readonly').extract()
                fom['form_textarea_rows'] = response.xpath('//form/textarea/@rows').extract()
                fom['form_textarea_required'] = response.xpath('//form/textarea/@required').extract()
                fom['form_textarea_wrap'] = response.xpath('//form/textarea/@wrap').extract()

                fom['form_button'] = response.xpath('//form/button').extract()
                fom['form_button_form'] = response.xpath('//form/button/@form').extract()
                fom['form_button_formaction'] = response.xpath('//form/button/@formaction').extract()
                fom['form_button_formenctype'] = response.xpath('//form/button/@formenctype').extract()
                fom['form_button_formmethod'] = response.xpath('//form/button/@formmethod').extract()
                fom['form_button_formnofomidate'] = response.xpath('//form/button/@formnofomidate').extract()
                fom['form_button_formtarget'] = response.xpath('//form/button/@formtarget').extract()
                fom['form_button_name'] = response.xpath('//form/button/@name').extract()
                fom['form_button_type'] = response.xpath('//form/button/@type').extract()
                fom['form_button_fomue'] = response.xpath('//form/button/@fomue').extract()
                fom['form_button_id'] = response.xpath('//form/button/@id').extract()
                fom['form_button_class'] = response.xpath('//form/button/@class').extract()
                fom['form_button_autofocus'] = response.xpath('//form/button/@autofocus').extract()
                fom['form_button_disabled'] = response.xpath('//form/button/@disabled').extract()
                fom['form_select'] = response.xpath('//form/button/@disabled').extract()
                fom['form_select_form'] = response.xpath('//form/select/@form').extract()
                fom['form_select_name'] = response.xpath('//form/select/@name').extract()
                fom['form_select_type'] = response.xpath('//form/select/@type').extract()
                fom['form_select_fomue'] = response.xpath('//form/select/@fomue').extract()
                fom['form_select_autofocus'] = response.xpath('//form/select/@autofocus').extract()
                fom['form_select_disabled'] = response.xpath('//form/select/@disabled').extract()
                fom['form_select_multiple'] = response.xpath('//form/select/@multiple').extract()
                fom['form_select_size'] = response.xpath('//form/select/@size').extract()
                fom['form_select_required'] = response.xpath('//form/select/@required').extract()
                fom['form_select_id'] = response.xpath('//form/select/@id').extract()
                fom['form_select_class'] = response.xpath('//form/select/@class').extract()
                fom['form_select_option'] = response.xpath('//form/select/@option').extract()
                fom['form_select_option_disabled'] = response.xpath('//form/select/option/@disabled').extract()
                fom['form_select_option_label'] = response.xpath('//form/select/option/@label').extract()
                fom['form_select_option_selected'] = response.xpath('//form/select/option/@selected').extract()
                fom['form_select_option_id'] = response.xpath('//form/select/option/@id').extract()
                fom['form_select_option_class'] = response.xpath('//form/select/option/@class').extract()
                fom['form_select_optgroup_label'] = response.xpath('//form/select/optgroup/@label').extract()
                fom['form_select_optgroup_id'] = response.xpath('//form/select/optgroup/@id').extract()
                fom['form_select_optgroup_class'] = response.xpath('//form/select/optgroup/@class').extract()
                fom['form_fieldset'] = response.xpath('//form/@fieldset').extract()
                fom['form_fieldset_disabled'] = response.xpath('//form/fieldset/@disabled').extract()
                fom['form_fieldset_id'] = response.xpath('//form/fieldset/@id').extract()
                fom['form_fieldset_class'] = response.xpath('//form/fieldset/@class').extract()
                fom['form_fieldset_name'] = response.xpath('//form/fieldset/@name').extract()
                fom['form_label'] = response.xpath('//form/@label').extract()
                fom['form_label_for'] = response.xpath('//form/label/@for').extract()
                fom['form_label_id'] = response.xpath('//form/label/@id').extract()
                fom['form_label_class'] = response.xpath('//form/label/@class').extract()
                fom['form_label_form'] = response.xpath('//form/label/@form').extract()
                fom['form_a'] = response.xpath('//form/@a').extract()
                fom['form_a_charset'] = response.xpath('//form/a/@charset').extract()
                fom['form_a_coords'] = response.xpath('//form/a/@coords').extract()
                fom['form_a_download'] = response.xpath('//form/a/@download').extract()
                fom['form_a_href'] = response.xpath('//form/a/@href').extract()
                fom['form_a_hreflang'] = response.xpath('//form/a/@hreflang').extract()
                fom['form_a_media'] = response.xpath('//form/a/@media').extract()
                fom['form_a_name'] = response.xpath('//form/a/@name').extract()
                fom['form_a_rel'] = response.xpath('//form/a/@rel').extract()
                fom['form_a_shape'] = response.xpath('//form/a/@shape').extract()
                fom['form_a_target'] = response.xpath('//form/a/@target').extract()
                fom['form_a_type'] = response.xpath('//form/a/@type').extract()
                fom['form_a_role'] = response.xpath('//form/a/@role').extract()
                fom['form_a_id'] = response.xpath('//form/a/@id').extract()
                fom['form_a_class'] = response.xpath('//form/a/@class').extract()
                fom['form_a_form'] = response.xpath('//form/a/@form').extract()

                val['a'] = response.xpath('//@a').extract()
                val['a_charset'] = response.xpath('//a/@charset').extract()
                val['a_coords'] = response.xpath('//a/@coords').extract()
                val['a_download'] = response.xpath('//a/@download').extract()
                val['a_href'] = response.xpath('//a/@href').extract()
                val['a_hreflang'] = response.xpath('//a/@hreflang').extract()
                val['a_media'] = response.xpath('//a/@media').extract()
                val['a_name'] = response.xpath('//a/@name').extract()
                val['a_rel'] = response.xpath('//a/@rel').extract()
                val['a_shape'] = response.xpath('//a/@shape').extract()
                val['a_target'] = response.xpath('//a/@target').extract()
                val['a_type'] = response.xpath('//a/@type').extract()
                val['a_role'] = response.xpath('//a/@role').extract()
                val['a_id'] = response.xpath('//a/@id').extract()
                val['a_class'] = response.xpath('//a/@class').extract()
                val['a_form'] = response.xpath('//a/@form').extract()

                val['input_form'] = response.xpath('//input/@form').extract()
                val['input_formaction'] = response.xpath('//input/@formaction').extract()
                val['input_formenctype'] = response.xpath('//input/@formenctype').extract()
                val['input_formmethod'] = response.xpath('//input/@formmethod').extract()
                val['input_formnovalidate'] = response.xpath('//input/@formnovalidate').extract()
                val['input_formtarget'] = response.xpath('//input/@formtarget').extract()
                val['input'] = response.xpath('//@input').extract()
                val['input_accept'] = response.xpath('//input/@accept').extract()
                val['input_align'] = response.xpath('//input/@align').extract()
                val['input_alt'] = response.xpath('//input/@alt').extract()
                val['input_autocomplete'] = response.xpath('//input/@autocomplete').extract()
                val['input_autofocus'] = response.xpath('//input/@autofocus').extract()
                val['input_checked'] = response.xpath('//input/@checked').extract()
                val['input_dirname'] = response.xpath('//input/@dirname').extract()
                val['input_disabled'] = response.xpath('//input/@disabled').extract()
                val['input_height'] = response.xpath('//input/@height').extract()
                val['input_list'] = response.xpath('//input/@list').extract()
                val['input_max'] = response.xpath('//input/@max').extract()
                val['input_maxlenght'] = response.xpath('//input/@maxlenght').extract()
                val['input_min'] = response.xpath('//input/@min').extract()
                val['input_multiple'] = response.xpath('//input/@multiple').extract()
                val['input_name'] = response.xpath('//input/@name').extract()
                val['input_pattern'] = response.xpath('//input/@pattern').extract()
                val['input_placeholder'] = response.xpath('//input/@placeholder').extract()
                val['input_readonly'] = response.xpath('//input/@readonly').extract()
                val['input_required'] = response.xpath('//input/@required').extract()
                val['input_size'] = response.xpath('//input/@size').extract()
                val['input_src'] = response.xpath('//input/@src').extract()
                val['input_step'] = response.xpath('//input/@step').extract()
                val['input_type'] = response.xpath('//input/@type').extract()
                val['input_value'] = response.xpath('//input/@value').extract()
                val['input_id'] = response.xpath('//input/@id').extract()
                val['input_class'] = response.xpath('//input/@class').extract()
                val['input_width'] = response.xpath('//input/@width').extract()
                val['input_role'] = response.xpath('//input/@role').extract()

                val['textarea_form'] = response.xpath('//textarea/@form').extract()
                val['textarea'] = response.xpath('//textarea').extract()
                val['textarea_autofocus'] = response.xpath('//textarea/@autofocus').extract()
                val['textarea_cols'] = response.xpath('//textarea/@cols').extract()
                val['textarea_dirname'] = response.xpath('//textarea/@dirname').extract()
                val['textarea_disabled'] = response.xpath('//textarea/@disabled').extract()

                val['textarea_maxlenght'] = response.xpath('//textarea/@maxlenght').extract()
                val['textarea_name'] = response.xpath('//textarea/@name').extract()
                val['textarea_id'] = response.xpath('//textarea/@id').extract()
                val['textarea_class'] = response.xpath('//textarea/@class').extract()
                val['textarea_placeholder'] = response.xpath('//textarea/@placeholder').extract()
                val['textarea_readonly'] = response.xpath('//textarea/@readonly').extract()
                val['textarea_rows'] = response.xpath('//textarea/@rows').extract()
                val['textarea_required'] = response.xpath('//textarea/@required').extract()
                val['textarea_wrap'] = response.xpath('//textarea/@wrap').extract()

                val['button'] = response.xpath('//button').extract()
                val['button_form'] = response.xpath('//button/@form').extract()
                val['button_formaction'] = response.xpath('//button/@formaction').extract()
                val['button_formenctype'] = response.xpath('//button/@formenctype').extract()
                val['button_formmethod'] = response.xpath('//button/@formmethod').extract()
                val['button_formnovalidate'] = response.xpath('//button/@formnovalidate').extract()
                val['button_formtarget'] = response.xpath('//button/@formtarget').extract()
                val['button_name'] = response.xpath('//button/@name').extract()
                val['button_type'] = response.xpath('//button/@type').extract()
                val['button_value'] = response.xpath('//button/@value').extract()
                val['button_id'] = response.xpath('//button/@id').extract()
                val['button_class'] = response.xpath('//button/@class').extract()
                val['button_autofocus'] = response.xpath('//button/@autofocus').extract()
                val['button_disabled'] = response.xpath('//button/@disabled').extract()
                val['select'] = response.xpath('//button/@disabled').extract()
                val['select_form'] = response.xpath('//select/@form').extract()
                val['select_name'] = response.xpath('//select/@name').extract()
                val['select_type'] = response.xpath('//select/@type').extract()
                val['select_value'] = response.xpath('//select/@value').extract()
                val['select_autofocus'] = response.xpath('//select/@autofocus').extract()
                val['select_disabled'] = response.xpath('//select/@disabled').extract()
                val['select_multiple'] = response.xpath('//select/@multiple').extract()
                val['select_size'] = response.xpath('//select/@size').extract()
                val['select_required'] = response.xpath('//select/@required').extract()
                val['select_id'] = response.xpath('//select/@id').extract()
                val['select_class'] = response.xpath('//select/@class').extract()
                val['select_option'] = response.xpath('//select/@option').extract()
                val['select_option_disabled'] = response.xpath('//select/option/@disabled').extract()
                val['select_option_label'] = response.xpath('//select/option/@label').extract()
                val['select_option_selected'] = response.xpath('//select/option/@selected').extract()
                val['select_option_id'] = response.xpath('//select/option/@id').extract()
                val['select_option_class'] = response.xpath('//select/option/@class').extract()
                val['select_optgroup_label'] = response.xpath('//select/optgroup/@label').extract()
                val['select_optgroup_id'] = response.xpath('//select/optgroup/@id').extract()
                val['select_optgroup_class'] = response.xpath('//select/optgroup/@class').extract()
                val['fieldset'] = response.xpath('//@fieldset').extract()
                val['fieldset_disabled'] = response.xpath('//fieldset/@disabled').extract()
                val['fieldset_id'] = response.xpath('//fieldset/@id').extract()
                val['fieldset_class'] = response.xpath('//fieldset/@class').extract()
                val['fieldset_name'] = response.xpath('//fieldset/@name').extract()
                val['label'] = response.xpath('//@label').extract()
                val['label_for'] = response.xpath('//label/@for').extract()
                val['label_id'] = response.xpath('//label/@id').extract()
                val['label_class'] = response.xpath('//label/@class').extract()
                val['label_form'] = response.xpath('//label/@form').extract()
                val['url'] = response.url

                item['project'] = []
                # item['div']=[]
                # item['form']=[]
                # item['value']=[]
                a = defaultdict(list)
                b = defaultdict(list)
                c = defaultdict(list)
                d = defaultdict(list)
                a['meta'].append(met)
                b['div'].append(di)
                c['form'].append(fom)
                d['value'].append(val)
                item['project'].append(d)
                item['project'].append(a)
                item['project'].append(b)
                item['project'].append(c)

                # item['project'].append(val)
                # item['meta'].append(met)
                # item['div'].append(di)
                # item['form'].append(fom)
                # item['project'].append(met)
                items.append(item)



                # item['url_to'] = link.url

                # with open('at.json', 'r') as f:
                #     dis_dict = json.load(f)
                #     for i in dis_dict:
                #         try:
                #                 #driver.get(response.url)
                #                 #next = driver.find_element_by_name(i['Name'])
                #                 next = response.xpath('//input[@type="text"]|//input[@type="email"]|//input[@type="password"]').extract()
                #                 chk = response.xpath(
                #                     '//input[@type="checkbox"]|//input[@type="radio"]').extract()
                #                 if next:
                #                     options = Options()
                #                     options.add_argument('--headless')
                #                     options.add_argument('--disable-gpu')
                #                     driver = webdriver.Chrome("C:\\Users\\Virus\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe",chrome_options=options)
                #
                #                     # driver = webdriver.PhantomJS("C:\\Users\\Virus\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs")
                #                     driver.get(response.url)
                #
                #                     inp = driver.find_elements_by_css_selector('input')
                #                     for el in inp:
                #                         #driver.find_element_by_name(distro['Name']
                #                         for distro in dis_dict:
                #                             if el.get_attribute('name')==distro['Name']:
                #                                 if chk:
                #                                     el.find_element_by_value(distro['value']).click()
                #                                 el.send_keys(distro['value'])
                #                     #for distro in dis_dict:
                #                         #driver.find_element_by_name(distro['Name']).send_keys(distro['value'])
                #                     #driver.find_element_by_class_name("wsite-button").click()
                #                     bt=driver.find_element_by_css_selector('input')
                #                     for ele in bt:
                #                         if ele.getAttribute('type')== 'submit':
                #                             ele.click()
                #                     #page = response.url.split("/")[-1]
                #                     #if page == '':
                #                     #    filename = 'quotes-Home%s.html' % page
                #                     #else:
                #                     #    filename = 'quotes-%s.html' % page
                #                     #print("FileName: ", filename)
                #
                #                     #with open(filename, 'wb') as f:
                #                     #    f.write(response.body)
                #                     #self.log('Saved file %s' % filename)
                #                     driver.close()
                #         except:
                #                 driver.close()
                #                 break
                return items
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