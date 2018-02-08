# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class MongodemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project = Field()
    form = Field()
    div = Field()
    meta = Field()
    url = Field()
    value = Field()
    _id=Field()
    # url_to = Field()
    title = Field()
    projecturl = Field()
    meta_property = Field()
    meta_content = Field()
    meta_charset = Field()
    meta_httpequiv = Field()
    meta_name = Field()
    meta_scheme = Field()
    link_a = Field()
    div_id = Field()
    div_class = Field()
    div_align = Field()
    div_form = Field()
    div_input = Field()
    div_input_accept = Field()
    div_input_align = Field()
    div_input_alt = Field()
    div_input_autocomplete = Field()
    div_input_autofocus = Field()
    div_input_checked = Field()
    div_input_dirname = Field()
    div_input_disabled = Field()
    div_input_form = Field()
    div_input_formaction = Field()
    div_input_formenctype = Field()
    div_input_formmethod = Field()
    div_input_formnovalidate = Field()
    div_input_formtarget = Field()
    div_input_height = Field()
    div_input_list = Field()
    div_input_max = Field()
    div_input_maxlenght = Field()
    div_input_min = Field()
    div_input_multiple = Field()
    div_input_name = Field()
    div_input_pattern = Field()
    div_input_placeholder = Field()
    div_input_readonly = Field()
    div_input_required = Field()
    div_input_size = Field()
    div_input_src = Field()
    div_input_step = Field()
    div_input_type = Field()
    div_input_value = Field()
    div_input_id = Field()
    div_input_class = Field()
    div_input_width = Field()
    div_input_role = Field()
    div_textarea = Field()
    div_textarea_autofocus = Field()
    div_textarea_cols = Field()
    div_textarea_dirname = Field()
    div_textarea_disabled = Field()
    div_textarea_form = Field()
    div_textarea_maxlenght = Field()
    div_textarea_name = Field()
    div_textarea_id = Field()
    div_textarea_class = Field()
    div_textarea_placeholder = Field()
    div_textarea_readonly = Field()
    div_textarea_rows = Field()
    div_textarea_required = Field()
    div_textarea_wrap = Field()
    div_button = Field()
    div_button_form = Field()
    div_button_formaction = Field()
    div_button_formenctype = Field()
    div_button_formmethod = Field()
    div_button_formnovalidate = Field()
    div_button_formtarget = Field()
    div_button_name = Field()
    div_button_type = Field()
    div_button_value = Field()
    div_button_id = Field()
    div_button_class = Field()
    div_button_autofocus = Field()
    div_button_disabled = Field()
    div_select = Field()
    div_select_form = Field()
    div_select_name = Field()
    div_select_type = Field()
    div_select_value = Field()
    div_select_autofocus = Field()
    div_select_disabled = Field()
    div_select_multiple = Field()
    div_select_size = Field()
    div_select_required = Field()
    div_select_id = Field()
    div_select_class = Field()
    div_select_option = Field()
    div_select_option_disabled = Field()
    div_select_option_label = Field()
    div_select_option_selected = Field()
    div_select_option_id = Field()
    div_select_option_class = Field()
    div_select_optgroup_label = Field()
    div_select_optgroup_id = Field()
    div_select_optgroup_class = Field()
    div_fieldset = Field()
    div_fieldset_disabled = Field()
    div_fieldset_id = Field()
    div_fieldset_class = Field()
    div_fieldset_name = Field()
    div_label = Field()
    div_label_for = Field()
    div_label_id = Field()
    div_label_class = Field()
    div_label_form = Field()
    div_a = Field()
    div_a_charset = Field()
    div_a_coords = Field()
    div_a_download = Field()
    div_a_href = Field()
    div_a_hreflang = Field()
    div_a_media = Field()
    div_a_name = Field()
    div_a_rel = Field()
    div_a_shape = Field()
    div_a_target = Field()
    div_a_type = Field()
    div_a_role = Field()
    div_a_id = Field()
    div_a_class = Field()
    div_a_form = Field()

    form_input = Field()

    form_id=Field()
    form_class=Field()
    form_accept=Field()
    form_action=Field()
    form_autocomplete=Field()
    form_method=Field()
    form_name=Field()
    form_novalidate=Field()
    form_target=Field()
    form_enctype=Field()
    form_accept_charset=Field()
    form_input_accept = Field()
    form_input_align = Field()
    form_input_alt = Field()
    form_input_autocomplete = Field()
    form_input_autofocus = Field()
    form_input_checked = Field()
    form_input_dirname = Field()
    form_input_disabled = Field()
    form_input_form = Field()
    form_input_formaction = Field()
    form_input_formenctype = Field()
    form_input_formmethod = Field()
    form_input_formnovalidate = Field()
    form_input_formtarget = Field()
    form_input_height = Field()
    form_input_list = Field()
    form_input_max = Field()
    form_input_maxlenght = Field()
    form_input_min = Field()
    form_input_multiple = Field()
    form_input_name = Field()
    form_input_pattern = Field()
    form_input_placeholder = Field()
    form_input_readonly = Field()
    form_input_required = Field()
    form_input_size = Field()
    form_input_src = Field()
    form_input_step = Field()
    form_input_type = Field()
    form_input_value = Field()
    form_input_id = Field()
    form_input_class = Field()
    form_input_width = Field()
    form_input_role = Field()
    form_textarea = Field()
    form_textarea_autofocus = Field()
    form_textarea_cols = Field()
    form_textarea_dirname = Field()
    form_textarea_disabled = Field()
    form_textarea_form = Field()
    form_textarea_maxlenght = Field()
    form_textarea_name = Field()
    form_textarea_id = Field()
    form_textarea_class = Field()
    form_textarea_placeholder = Field()
    form_textarea_readonly = Field()
    form_textarea_rows = Field()
    form_textarea_required = Field()
    form_textarea_wrap = Field()
    form_button = Field()
    form_button_form = Field()
    form_button_formaction = Field()
    form_button_formenctype = Field()
    form_button_formmethod = Field()
    form_button_formnovalidate = Field()
    form_button_formtarget = Field()
    form_button_name = Field()
    form_button_type = Field()
    form_button_value = Field()
    form_button_id = Field()
    form_button_class = Field()
    form_button_autofocus = Field()
    form_button_disabled = Field()
    form_select = Field()
    form_select_form = Field()
    form_select_name = Field()
    form_select_type = Field()
    form_select_value = Field()
    form_select_autofocus = Field()
    form_select_disabled = Field()
    form_select_multiple = Field()
    form_select_size = Field()
    form_select_required = Field()
    form_select_id = Field()
    form_select_class = Field()
    form_select_option = Field()
    form_select_option_disabled = Field()
    form_select_option_label = Field()
    form_select_option_selected = Field()
    form_select_option_id = Field()
    form_select_option_class = Field()
    form_select_optgroup_label = Field()
    form_select_optgroup_id = Field()
    form_select_optgroup_class = Field()
    form_fieldset = Field()
    form_fieldset_disabled = Field()
    form_fieldset_id = Field()
    form_fieldset_class = Field()
    form_fieldset_name = Field()
    form_label = Field()
    form_label_for = Field()
    form_label_id = Field()
    form_label_class = Field()
    form_label_form = Field()
    form_a = Field()
    form_a_charset = Field()
    form_a_coords = Field()
    form_a_download = Field()
    form_a_href = Field()
    form_a_hreflang = Field()
    form_a_media = Field()
    form_a_name = Field()
    form_a_rel = Field()
    form_a_shape = Field()
    form_a_target = Field()
    form_a_type = Field()
    form_a_role = Field()
    form_a_id = Field()
    form_a_class = Field()
    form_a_form = Field()

    a = Field()
    a_charset = Field()
    a_coords = Field()
    a_download = Field()
    a_href = Field()
    a_hreflang = Field()
    a_media = Field()
    a_name = Field()
    a_rel = Field()
    a_shape = Field()
    a_target = Field()
    a_type = Field()
    a_role = Field()
    a_id = Field()
    a_class = Field()
    a_form = Field()
    input=Field()
    input_accept = Field()
    input_align = Field()
    input_alt = Field()
    input_autocomplete = Field()
    input_autofocus = Field()
    input_checked = Field()
    input_dirname = Field()
    input_disabled = Field()
    input_form = Field()
    input_formaction = Field()
    input_formenctype = Field()
    input_formmethod = Field()
    input_formnovalidate = Field()
    input_formtarget = Field()
    input_height = Field()
    input_list = Field()
    input_max = Field()
    input_maxlenght = Field()
    input_min = Field()
    input_multiple = Field()
    input_name = Field()
    input_pattern = Field()
    input_placeholder = Field()
    input_readonly = Field()
    input_required = Field()
    input_size = Field()
    input_src = Field()
    input_step = Field()
    input_type = Field()
    input_value = Field()
    input_id = Field()
    input_class = Field()
    input_width = Field()
    input_role = Field()
    textarea = Field()
    textarea_autofocus = Field()
    textarea_cols = Field()
    textarea_dirname = Field()
    textarea_disabled = Field()
    textarea_form = Field()
    textarea_maxlenght = Field()
    textarea_name = Field()
    textarea_id = Field()
    textarea_class = Field()
    textarea_placeholder = Field()
    textarea_readonly = Field()
    textarea_rows = Field()
    textarea_required = Field()
    textarea_wrap = Field()
    button = Field()
    button_form = Field()
    button_formaction = Field()
    button_formenctype = Field()
    button_formmethod = Field()
    button_formnovalidate = Field()
    button_formtarget = Field()
    button_name = Field()
    button_type = Field()
    button_value = Field()
    button_id = Field()
    button_class = Field()
    button_autofocus = Field()
    button_disabled = Field()
    select = Field()
    select_form = Field()
    select_name = Field()
    select_type = Field()
    select_value = Field()
    select_autofocus = Field()
    select_disabled = Field()
    select_multiple = Field()
    select_size = Field()
    select_required = Field()
    select_id = Field()
    select_class = Field()
    select_option = Field()
    select_option_disabled = Field()
    select_option_label = Field()
    select_option_selected = Field()
    select_option_id = Field()
    select_option_class = Field()
    select_optgroup_label = Field()
    select_optgroup_id = Field()
    select_optgroup_class = Field()
    fieldset = Field()
    fieldset_disabled = Field()
    fieldset_id = Field()
    fieldset_class = Field()
    fieldset_name = Field()
    label = Field()
    label_for = Field()
    label_id = Field()
    label_class = Field()
    label_form = Field()


pass
