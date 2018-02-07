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
                        # is_allowed = True


            # if is_allowed:
                # for lnk in link.url:
                # req_list=set([link.url])
                # if req_list:
                        item = MongodemoItem()
                        item['projecturl'] = allowed_domain
                        item['title'] = response.xpath('//title/text()').extract()
                        item['meta_property'] = response.xpath('//meta/@property').extract()
                        item['meta_content'] = response.xpath('//meta/@content').extract()
                        item['meta_charset'] = response.xpath('//meta/@charset').extract()
                        item['meta_httpequiv'] = response.xpath('//meta/@http-equiv').extract()
                        item['meta_name'] = response.xpath('//meta/@name').extract()
                        item['meta_scheme'] = response.xpath('//meta/@scheme').extract()
                        item['link_a'] = response.xpath('//a/@href').extract()
                        item['div_id'] = response.xpath('//div/@id').extract()
                        item['div_class'] = response.xpath('//div/@class').extract()
                        item['div_align'] = response.xpath('//div/@align').extract()
                        item['div_form'] = response.xpath('//div/@form').extract()
                        item['div_input'] = response.xpath('//div/@input').extract()
                        item['div_input_accept'] = response.xpath('//div/input/@accept').extract()
                        item['div_input_align'] = response.xpath('//div/input/@align').extract()
                        item['div_input_alt'] = response.xpath('//div/input/@alt').extract()
                        item['div_input_autocomplete'] = response.xpath('//div/input/@autocomplete').extract()
                        item['div_input_autofocus'] = response.xpath('//div/input/@autofocus').extract()
                        item['div_input_checked'] = response.xpath('//div/input/@checked').extract()
                        item['div_input_dirname'] = response.xpath('//div/input/@dirname').extract()
                        item['div_input_disabled'] = response.xpath('//div/input/@disabled').extract()
                        item['div_input_form'] = response.xpath('//div/input/@form').extract()
                        item['div_input_formaction'] = response.xpath('//div/input/@formaction').extract()
                        item['div_input_formenctype'] = response.xpath('//div/input/@formenctype').extract()
                        item['div_input_formmethod'] = response.xpath('//div/input/@formmethod').extract()
                        item['div_input_formnovalidate'] = response.xpath('//div/input/@formnovalidate').extract()
                        item['div_input_formtarget'] = response.xpath('//div/input/@formtarget').extract()
                        item['div_input_height'] = response.xpath('//div/input/@height').extract()
                        item['div_input_list'] = response.xpath('//div/input/@list').extract()
                        item['div_input_max'] = response.xpath('//div/input/@max').extract()
                        item['div_input_maxlenght'] = response.xpath('//div/input/@maxlenght').extract()
                        item['div_input_min'] = response.xpath('//div/input/@min').extract()
                        item['div_input_multiple'] = response.xpath('//div/input/@multiple').extract()
                        item['div_input_name'] = response.xpath('//div/input/@name').extract()
                        item['div_input_pattern'] = response.xpath('//div/input/@pattern').extract()
                        item['div_input_placeholder'] = response.xpath('//div/input/@placeholder').extract()
                        item['div_input_readonly'] = response.xpath('//div/input/@readonly').extract()
                        item['div_input_required'] = response.xpath('//div/input/@required').extract()
                        item['div_input_size'] = response.xpath('//div/input/@size').extract()
                        item['div_input_src'] = response.xpath('//div/input/@src').extract()
                        item['div_input_step'] = response.xpath('//div/input/@step').extract()
                        item['div_input_type'] = response.xpath('//div/input/@type').extract()
                        item['div_input_value'] = response.xpath('//div/input/@value').extract()
                        item['div_input_id'] = response.xpath('//div/input/@id').extract()
                        item['div_input_class'] = response.xpath('//div/input/@class').extract()
                        item['div_input_width'] = response.xpath('//div/input/@width').extract()
                        item['div_input_role'] = response.xpath('//div/input/@role').extract()
                        item['div_textarea'] = response.xpath('//div/textarea').extract()
                        item['div_textarea_autofocus'] = response.xpath('//div/textarea/@autofocus').extract()
                        item['div_textarea_cols'] = response.xpath('//div/textarea/@cols').extract()
                        item['div_textarea_dirname'] = response.xpath('//div/textarea/@dirname').extract()
                        item['div_textarea_disabled'] = response.xpath('//div/textarea/@disabled').extract()
                        item['div_textarea_form'] = response.xpath('//div/textarea/@form').extract()
                        item['div_textarea_maxlenght'] = response.xpath('//div/textarea/@maxlenght').extract()
                        item['div_textarea_name'] = response.xpath('//div/textarea/@name').extract()
                        item['div_textarea_id'] = response.xpath('//div/textarea/@id').extract()
                        item['div_textarea_class'] = response.xpath('//div/textarea/@class').extract()
                        item['div_textarea_placeholder'] = response.xpath('//div/textarea/@placeholder').extract()
                        item['div_textarea_readonly'] = response.xpath('//div/textarea/@readonly').extract()
                        item['div_textarea_rows'] = response.xpath('//div/textarea/@rows').extract()
                        item['div_textarea_required'] = response.xpath('//div/textarea/@required').extract()
                        item['div_textarea_wrap'] = response.xpath('//div/textarea/@wrap').extract()
                        item['div_button'] = response.xpath('//div/button').extract()
                        item['div_button_form'] = response.xpath('//div/button/@form').extract()
                        item['div_button_formaction'] = response.xpath('//div/button/@formaction').extract()
                        item['div_button_formenctype'] = response.xpath('//div/button/@formenctype').extract()
                        item['div_button_formmethod'] = response.xpath('//div/button/@formmethod').extract()
                        item['div_button_formnovalidate'] = response.xpath('//div/button/@formnovalidate').extract()
                        item['div_button_formtarget'] = response.xpath('//div/button/@formtarget').extract()
                        item['div_button_name'] = response.xpath('//div/button/@name').extract()
                        item['div_button_type'] = response.xpath('//div/button/@type').extract()
                        item['div_button_value'] = response.xpath('//div/button/@value').extract()
                        item['div_button_id'] = response.xpath('//div/button/@id').extract()
                        item['div_button_class'] = response.xpath('//div/button/@class').extract()
                        item['div_button_autofocus'] = response.xpath('//div/button/@autofocus').extract()
                        item['div_button_disabled'] = response.xpath('//div/button/@disabled').extract()
                        item['div_select'] = response.xpath('//div/button/@disabled').extract()
                        item['div_select_form'] = response.xpath('//div/select/@form').extract()
                        item['div_select_name'] = response.xpath('//div/select/@name').extract()
                        item['div_select_type'] = response.xpath('//div/select/@type').extract()
                        item['div_select_value'] = response.xpath('//div/select/@value').extract()
                        item['div_select_autofocus'] = response.xpath('//div/select/@autofocus').extract()
                        item['div_select_disabled'] = response.xpath('//div/select/@disabled').extract()
                        item['div_select_multiple'] = response.xpath('//div/select/@multiple').extract()
                        item['div_select_size'] = response.xpath('//div/select/@size').extract()
                        item['div_select_required'] = response.xpath('//div/select/@required').extract()
                        item['div_select_id'] = response.xpath('//div/select/@id').extract()
                        item['div_select_class'] = response.xpath('//div/select/@class').extract()
                        item['div_select_option'] = response.xpath('//div/select/@option').extract()
                        item['div_select_option_disabled'] = response.xpath('//div/select/option/@disabled').extract()
                        item['div_select_option_label'] = response.xpath('//div/select/option/@label').extract()
                        item['div_select_option_selected'] = response.xpath('//div/select/option/@selected').extract()
                        item['div_select_option_id'] = response.xpath('//div/select/option/@id').extract()
                        item['div_select_option_class'] = response.xpath('//div/select/option/@class').extract()
                        item['div_select_optgroup_label'] = response.xpath('//div/select/optgroup/@label').extract()
                        item['div_select_optgroup_id'] = response.xpath('//div/select/optgroup/@id').extract()
                        item['div_select_optgroup_class'] = response.xpath('//div/select/optgroup/@class').extract()
                        item['div_fieldset'] = response.xpath('//div/@fieldset').extract()
                        item['div_fieldset_disabled'] = response.xpath('//div/fieldset/@disabled').extract()
                        item['div_fieldset_id'] = response.xpath('//div/fieldset/@id').extract()
                        item['div_fieldset_class'] = response.xpath('//div/fieldset/@class').extract()
                        item['div_fieldset_name'] = response.xpath('//div/fieldset/@name').extract()
                        item['div_label'] = response.xpath('//div/@label').extract()
                        item['div_label_for'] = response.xpath('//div/label/@for').extract()
                        item['div_label_id'] = response.xpath('//div/label/@id').extract()
                        item['div_label_class'] = response.xpath('//div/label/@class').extract()
                        item['div_label_form'] = response.xpath('//div/label/@form').extract()
                        item['div_a'] = response.xpath('//div/@a').extract()
                        item['div_a_charset'] = response.xpath('//div/a/@charset').extract()
                        item['div_a_coords'] = response.xpath('//div/a/@coords').extract()
                        item['div_a_download'] = response.xpath('//div/a/@download').extract()
                        item['div_a_href'] = response.xpath('//div/a/@href').extract()
                        item['div_a_hreflang'] = response.xpath('//div/a/@hreflang').extract()
                        item['div_a_media'] = response.xpath('//div/a/@media').extract()
                        item['div_a_name'] = response.xpath('//div/a/@name').extract()
                        item['div_a_rel'] = response.xpath('//div/a/@rel').extract()
                        item['div_a_shape'] = response.xpath('//div/a/@shape').extract()
                        item['div_a_target'] = response.xpath('//div/a/@target').extract()
                        item['div_a_type'] = response.xpath('//div/a/@type').extract()
                        item['div_a_role'] = response.xpath('//div/a/@role').extract()
                        item['div_a_id'] = response.xpath('//div/a/@id').extract()
                        item['div_a_class'] = response.xpath('//div/a/@class').extract()
                        item['div_a_form'] = response.xpath('//div/a/@form').extract()

                        item['form_id'] = response.xpath('//form/@id').extract()
                        item['form_class'] = response.xpath('//form/@class').extract()
                        item['form_accept'] = response.xpath('//form/@accept').extract()
                        item['form_action'] = response.xpath('//form/@action').extract()
                        item['form_autocomplete'] = response.xpath('//form/@autocomplete').extract()
                        item['form_method'] = response.xpath('//form/@method').extract()
                        item['form_name'] = response.xpath('//form/@name').extract()
                        item['form_novalidate'] = response.xpath('//form/@novalidate').extract()
                        item['form_target'] = response.xpath('//form/@target').extract()
                        item['form_enctype'] = response.xpath('//form/@enctype').extract()
                        item['form_accept_charset'] = response.xpath('//form/@accept-charset').extract()

                        item['form_input_form'] = response.xpath('//form/input/@form').extract()
                        item['form_input_formaction'] = response.xpath('//form/input/@formaction').extract()
                        item['form_input_formenctype'] = response.xpath('//form/input/@formenctype').extract()
                        item['form_input_formmethod'] = response.xpath('//form/input/@formmethod').extract()
                        item['form_input_formnovalidate'] = response.xpath('//form/input/@formnovalidate').extract()
                        item['form_input_formtarget'] = response.xpath('//form/input/@formtarget').extract()
                        item['form_input'] = response.xpath('//form/@input').extract()
                        item['form_input_accept'] = response.xpath('//form/input/@accept').extract()
                        item['form_input_align'] = response.xpath('//form/input/@align').extract()
                        item['form_input_alt'] = response.xpath('//form/input/@alt').extract()
                        item['form_input_autocomplete'] = response.xpath('//form/input/@autocomplete').extract()
                        item['form_input_autofocus'] = response.xpath('//form/input/@autofocus').extract()
                        item['form_input_checked'] = response.xpath('//form/input/@checked').extract()
                        item['form_input_dirname'] = response.xpath('//form/input/@dirname').extract()
                        item['form_input_disabled'] = response.xpath('//form/input/@disabled').extract()
                        item['form_input_height'] = response.xpath('//form/input/@height').extract()
                        item['form_input_list'] = response.xpath('//form/input/@list').extract()
                        item['form_input_max'] = response.xpath('//form/input/@max').extract()
                        item['form_input_maxlenght'] = response.xpath('//form/input/@maxlenght').extract()
                        item['form_input_min'] = response.xpath('//form/input/@min').extract()
                        item['form_input_multiple'] = response.xpath('//form/input/@multiple').extract()
                        item['form_input_name'] = response.xpath('//form/input/@name').extract()
                        item['form_input_pattern'] = response.xpath('//form/input/@pattern').extract()
                        item['form_input_placeholder'] = response.xpath('//form/input/@placeholder').extract()
                        item['form_input_readonly'] = response.xpath('//form/input/@readonly').extract()
                        item['form_input_required'] = response.xpath('//form/input/@required').extract()
                        item['form_input_size'] = response.xpath('//form/input/@size').extract()
                        item['form_input_src'] = response.xpath('//form/input/@src').extract()
                        item['form_input_step'] = response.xpath('//form/input/@step').extract()
                        item['form_input_type'] = response.xpath('//form/input/@type').extract()
                        item['form_input_value'] = response.xpath('//form/input/@value').extract()
                        item['form_input_id'] = response.xpath('//form/input/@id').extract()
                        item['form_input_class'] = response.xpath('//form/input/@class').extract()
                        item['form_input_width'] = response.xpath('//form/input/@width').extract()
                        item['form_input_role'] = response.xpath('//form/input/@role').extract()

                        item['form_textarea_form'] = response.xpath('//form/textarea/@form').extract()
                        item['form_textarea'] = response.xpath('//form/textarea').extract()
                        item['form_textarea_autofocus'] = response.xpath('//form/textarea/@autofocus').extract()
                        item['form_textarea_cols'] = response.xpath('//form/textarea/@cols').extract()
                        item['form_textarea_dirname'] = response.xpath('//form/textarea/@dirname').extract()
                        item['form_textarea_disabled'] = response.xpath('//form/textarea/@disabled').extract()

                        item['form_textarea_maxlenght'] = response.xpath('//form/textarea/@maxlenght').extract()
                        item['form_textarea_name'] = response.xpath('//form/textarea/@name').extract()
                        item['form_textarea_id'] = response.xpath('//form/textarea/@id').extract()
                        item['form_textarea_class'] = response.xpath('//form/textarea/@class').extract()
                        item['form_textarea_placeholder'] = response.xpath('//form/textarea/@placeholder').extract()
                        item['form_textarea_readonly'] = response.xpath('//form/textarea/@readonly').extract()
                        item['form_textarea_rows'] = response.xpath('//form/textarea/@rows').extract()
                        item['form_textarea_required'] = response.xpath('//form/textarea/@required').extract()
                        item['form_textarea_wrap'] = response.xpath('//form/textarea/@wrap').extract()

                        item['form_button'] = response.xpath('//form/button').extract()
                        item['form_button_form'] = response.xpath('//form/button/@form').extract()
                        item['form_button_formaction'] = response.xpath('//form/button/@formaction').extract()
                        item['form_button_formenctype'] = response.xpath('//form/button/@formenctype').extract()
                        item['form_button_formmethod'] = response.xpath('//form/button/@formmethod').extract()
                        item['form_button_formnovalidate'] = response.xpath('//form/button/@formnovalidate').extract()
                        item['form_button_formtarget'] = response.xpath('//form/button/@formtarget').extract()
                        item['form_button_name'] = response.xpath('//form/button/@name').extract()
                        item['form_button_type'] = response.xpath('//form/button/@type').extract()
                        item['form_button_value'] = response.xpath('//form/button/@value').extract()
                        item['form_button_id'] = response.xpath('//form/button/@id').extract()
                        item['form_button_class'] = response.xpath('//form/button/@class').extract()
                        item['form_button_autofocus'] = response.xpath('//form/button/@autofocus').extract()
                        item['form_button_disabled'] = response.xpath('//form/button/@disabled').extract()
                        item['form_select'] = response.xpath('//form/button/@disabled').extract()
                        item['form_select_form'] = response.xpath('//form/select/@form').extract()
                        item['form_select_name'] = response.xpath('//form/select/@name').extract()
                        item['form_select_type'] = response.xpath('//form/select/@type').extract()
                        item['form_select_value'] = response.xpath('//form/select/@value').extract()
                        item['form_select_autofocus'] = response.xpath('//form/select/@autofocus').extract()
                        item['form_select_disabled'] = response.xpath('//form/select/@disabled').extract()
                        item['form_select_multiple'] = response.xpath('//form/select/@multiple').extract()
                        item['form_select_size'] = response.xpath('//form/select/@size').extract()
                        item['form_select_required'] = response.xpath('//form/select/@required').extract()
                        item['form_select_id'] = response.xpath('//form/select/@id').extract()
                        item['form_select_class'] = response.xpath('//form/select/@class').extract()
                        item['form_select_option'] = response.xpath('//form/select/@option').extract()
                        item['form_select_option_disabled'] = response.xpath('//form/select/option/@disabled').extract()
                        item['form_select_option_label'] = response.xpath('//form/select/option/@label').extract()
                        item['form_select_option_selected'] = response.xpath('//form/select/option/@selected').extract()
                        item['form_select_option_id'] = response.xpath('//form/select/option/@id').extract()
                        item['form_select_option_class'] = response.xpath('//form/select/option/@class').extract()
                        item['form_select_optgroup_label'] = response.xpath('//form/select/optgroup/@label').extract()
                        item['form_select_optgroup_id'] = response.xpath('//form/select/optgroup/@id').extract()
                        item['form_select_optgroup_class'] = response.xpath('//form/select/optgroup/@class').extract()
                        item['form_fieldset'] = response.xpath('//form/@fieldset').extract()
                        item['form_fieldset_disabled'] = response.xpath('//form/fieldset/@disabled').extract()
                        item['form_fieldset_id'] = response.xpath('//form/fieldset/@id').extract()
                        item['form_fieldset_class'] = response.xpath('//form/fieldset/@class').extract()
                        item['form_fieldset_name'] = response.xpath('//form/fieldset/@name').extract()
                        item['form_label'] = response.xpath('//form/@label').extract()
                        item['form_label_for'] = response.xpath('//form/label/@for').extract()
                        item['form_label_id'] = response.xpath('//form/label/@id').extract()
                        item['form_label_class'] = response.xpath('//form/label/@class').extract()
                        item['form_label_form'] = response.xpath('//form/label/@form').extract()
                        item['form_a'] = response.xpath('//form/@a').extract()
                        item['form_a_charset'] = response.xpath('//form/a/@charset').extract()
                        item['form_a_coords'] = response.xpath('//form/a/@coords').extract()
                        item['form_a_download'] = response.xpath('//form/a/@download').extract()
                        item['form_a_href'] = response.xpath('//form/a/@href').extract()
                        item['form_a_hreflang'] = response.xpath('//form/a/@hreflang').extract()
                        item['form_a_media'] = response.xpath('//form/a/@media').extract()
                        item['form_a_name'] = response.xpath('//form/a/@name').extract()
                        item['form_a_rel'] = response.xpath('//form/a/@rel').extract()
                        item['form_a_shape'] = response.xpath('//form/a/@shape').extract()
                        item['form_a_target'] = response.xpath('//form/a/@target').extract()
                        item['form_a_type'] = response.xpath('//form/a/@type').extract()
                        item['form_a_role'] = response.xpath('//form/a/@role').extract()
                        item['form_a_id'] = response.xpath('//form/a/@id').extract()
                        item['form_a_class'] = response.xpath('//form/a/@class').extract()
                        item['form_a_form'] = response.xpath('//form/a/@form').extract()

                        item['a'] = response.xpath('//@a').extract()
                        item['a_charset'] = response.xpath('//a/@charset').extract()
                        item['a_coords'] = response.xpath('//a/@coords').extract()
                        item['a_download'] = response.xpath('//a/@download').extract()
                        item['a_href'] = response.xpath('//a/@href').extract()
                        item['a_hreflang'] = response.xpath('//a/@hreflang').extract()
                        item['a_media'] = response.xpath('//a/@media').extract()
                        item['a_name'] = response.xpath('//a/@name').extract()
                        item['a_rel'] = response.xpath('//a/@rel').extract()
                        item['a_shape'] = response.xpath('//a/@shape').extract()
                        item['a_target'] = response.xpath('//a/@target').extract()
                        item['a_type'] = response.xpath('//a/@type').extract()
                        item['a_role'] = response.xpath('//a/@role').extract()
                        item['a_id'] = response.xpath('//a/@id').extract()
                        item['a_class'] = response.xpath('//a/@class').extract()
                        item['a_form'] = response.xpath('//a/@form').extract()

                        item['input_form'] = response.xpath('//input/@form').extract()
                        item['input_formaction'] = response.xpath('//input/@formaction').extract()
                        item['input_formenctype'] = response.xpath('//input/@formenctype').extract()
                        item['input_formmethod'] = response.xpath('//input/@formmethod').extract()
                        item['input_formnovalidate'] = response.xpath('//input/@formnovalidate').extract()
                        item['input_formtarget'] = response.xpath('//input/@formtarget').extract()
                        item['input'] = response.xpath('//@input').extract()
                        item['input_accept'] = response.xpath('//input/@accept').extract()
                        item['input_align'] = response.xpath('//input/@align').extract()
                        item['input_alt'] = response.xpath('//input/@alt').extract()
                        item['input_autocomplete'] = response.xpath('//input/@autocomplete').extract()
                        item['input_autofocus'] = response.xpath('//input/@autofocus').extract()
                        item['input_checked'] = response.xpath('//input/@checked').extract()
                        item['input_dirname'] = response.xpath('//input/@dirname').extract()
                        item['input_disabled'] = response.xpath('//input/@disabled').extract()
                        item['input_height'] = response.xpath('//input/@height').extract()
                        item['input_list'] = response.xpath('//input/@list').extract()
                        item['input_max'] = response.xpath('//input/@max').extract()
                        item['input_maxlenght'] = response.xpath('//input/@maxlenght').extract()
                        item['input_min'] = response.xpath('//input/@min').extract()
                        item['input_multiple'] = response.xpath('//input/@multiple').extract()
                        item['input_name'] = response.xpath('//input/@name').extract()
                        item['input_pattern'] = response.xpath('//input/@pattern').extract()
                        item['input_placeholder'] = response.xpath('//input/@placeholder').extract()
                        item['input_readonly'] = response.xpath('//input/@readonly').extract()
                        item['input_required'] = response.xpath('//input/@required').extract()
                        item['input_size'] = response.xpath('//input/@size').extract()
                        item['input_src'] = response.xpath('//input/@src').extract()
                        item['input_step'] = response.xpath('//input/@step').extract()
                        item['input_type'] = response.xpath('//input/@type').extract()
                        item['input_value'] = response.xpath('//input/@value').extract()
                        item['input_id'] = response.xpath('//input/@id').extract()
                        item['input_class'] = response.xpath('//input/@class').extract()
                        item['input_width'] = response.xpath('//input/@width').extract()
                        item['input_role'] = response.xpath('//input/@role').extract()

                        item['textarea_form'] = response.xpath('//textarea/@form').extract()
                        item['textarea'] = response.xpath('//textarea').extract()
                        item['textarea_autofocus'] = response.xpath('//textarea/@autofocus').extract()
                        item['textarea_cols'] = response.xpath('//textarea/@cols').extract()
                        item['textarea_dirname'] = response.xpath('//textarea/@dirname').extract()
                        item['textarea_disabled'] = response.xpath('//textarea/@disabled').extract()

                        item['textarea_maxlenght'] = response.xpath('//textarea/@maxlenght').extract()
                        item['textarea_name'] = response.xpath('//textarea/@name').extract()
                        item['textarea_id'] = response.xpath('//textarea/@id').extract()
                        item['textarea_class'] = response.xpath('//textarea/@class').extract()
                        item['textarea_placeholder'] = response.xpath('//textarea/@placeholder').extract()
                        item['textarea_readonly'] = response.xpath('//textarea/@readonly').extract()
                        item['textarea_rows'] = response.xpath('//textarea/@rows').extract()
                        item['textarea_required'] = response.xpath('//textarea/@required').extract()
                        item['textarea_wrap'] = response.xpath('//textarea/@wrap').extract()

                        item['button'] = response.xpath('//button').extract()
                        item['button_form'] = response.xpath('//button/@form').extract()
                        item['button_formaction'] = response.xpath('//button/@formaction').extract()
                        item['button_formenctype'] = response.xpath('//button/@formenctype').extract()
                        item['button_formmethod'] = response.xpath('//button/@formmethod').extract()
                        item['button_formnovalidate'] = response.xpath('//button/@formnovalidate').extract()
                        item['button_formtarget'] = response.xpath('//button/@formtarget').extract()
                        item['button_name'] = response.xpath('//button/@name').extract()
                        item['button_type'] = response.xpath('//button/@type').extract()
                        item['button_value'] = response.xpath('//button/@value').extract()
                        item['button_id'] = response.xpath('//button/@id').extract()
                        item['button_class'] = response.xpath('//button/@class').extract()
                        item['button_autofocus'] = response.xpath('//button/@autofocus').extract()
                        item['button_disabled'] = response.xpath('//button/@disabled').extract()
                        item['select'] = response.xpath('//button/@disabled').extract()
                        item['select_form'] = response.xpath('//select/@form').extract()
                        item['select_name'] = response.xpath('//select/@name').extract()
                        item['select_type'] = response.xpath('//select/@type').extract()
                        item['select_value'] = response.xpath('//select/@value').extract()
                        item['select_autofocus'] = response.xpath('//select/@autofocus').extract()
                        item['select_disabled'] = response.xpath('//select/@disabled').extract()
                        item['select_multiple'] = response.xpath('//select/@multiple').extract()
                        item['select_size'] = response.xpath('//select/@size').extract()
                        item['select_required'] = response.xpath('//select/@required').extract()
                        item['select_id'] = response.xpath('//select/@id').extract()
                        item['select_class'] = response.xpath('//select/@class').extract()
                        item['select_option'] = response.xpath('//select/@option').extract()
                        item['select_option_disabled'] = response.xpath('//select/option/@disabled').extract()
                        item['select_option_label'] = response.xpath('//select/option/@label').extract()
                        item['select_option_selected'] = response.xpath('//select/option/@selected').extract()
                        item['select_option_id'] = response.xpath('//select/option/@id').extract()
                        item['select_option_class'] = response.xpath('//select/option/@class').extract()
                        item['select_optgroup_label'] = response.xpath('//select/optgroup/@label').extract()
                        item['select_optgroup_id'] = response.xpath('//select/optgroup/@id').extract()
                        item['select_optgroup_class'] = response.xpath('//select/optgroup/@class').extract()
                        item['fieldset'] = response.xpath('//@fieldset').extract()
                        item['fieldset_disabled'] = response.xpath('//fieldset/@disabled').extract()
                        item['fieldset_id'] = response.xpath('//fieldset/@id').extract()
                        item['fieldset_class'] = response.xpath('//fieldset/@class').extract()
                        item['fieldset_name'] = response.xpath('//fieldset/@name').extract()
                        item['label'] = response.xpath('//@label').extract()
                        item['label_for'] = response.xpath('//label/@for').extract()
                        item['label_id'] = response.xpath('//label/@id').extract()
                        item['label_class'] = response.xpath('//label/@class').extract()
                        item['label_form'] = response.xpath('//label/@form').extract()





                        item['url'] = response.url
                        # item['url_to'] = link.url
                        items.append(item)
        with open('at.json', 'r') as f:
            dis_dict = json.load(f)
        for i in dis_dict:
            try:
                #driver.get(response.url)
                #next = driver.find_element_by_name(i['Name'])
                next = response.xpath('//input[@type="text"]|//input[@type="email"]|//input[@type="password"]').extract()
                if next:
                    options = Options()
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                    driver = webdriver.Chrome("C:\\Users\\Virus\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe",chrome_options=options)

                    # driver = webdriver.PhantomJS("C:\\Users\\Virus\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs")
                    driver.get(response.url)

                    inp = driver.find_elements_by_css_selector('input')
                    for el in inp:
                        #driver.find_element_by_name(distro['Name']
                        for distro in dis_dict:
                            if el.get_attribute('name')==distro['Name']:
                                el.send_keys(distro['value'])

                    #for distro in dis_dict:
                        #driver.find_element_by_name(distro['Name']).send_keys(distro['value'])
                    #driver.find_element_by_class_name("wsite-button").click()
                    bt=driver.find_element_by_css_selector('input')
                    for ele in bt:
                        if ele.getAttribute('type')== 'submit':
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
        return items