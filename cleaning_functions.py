#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: margaritabozhinova
"""


def clean_article_text(article_text):
    """
    Take in a nested list of article paragraphs, clean and return the
    list of articles.

    """
    import re

    remove_html = [
        ["".join(re.findall(r"(?:.+?>)(.*?)(?:<.+?)", par)) for par in article]
        for article in article_text
    ]

    all_str = [string for elem in remove_html for string in elem]

    # Identify common strings that are not article content
    str_count_dict = {
        common_str: all_str.count(common_str) for common_str in set(all_str)
    }
    common_str_dict = {key: value for key, value in str_count_dict.items() if value > 2}
    common_str = list(common_str_dict.keys())

    # Remove common strings from each article
    clean_text = [
        [par for par in article if par not in common_str] for article in remove_html
    ]

    # Combine each article into a single string
    return ["".join(par for par in article) for article in clean_text]


def check_common_str(article_text):
    import re
    import pandas as pd

    remove_html = [
        ["".join(re.findall(r"(?:.+?>)(.*?)(?:<.+?)", par)) for par in article]
        for article in article_text
    ]

    all_str = [string for elem in remove_html for string in elem]

    # Identify common strings that are not article content
    str_count_dict = {
        common_str: all_str.count(common_str) for common_str in set(all_str)
    }
    common_str_dict = {key: value for key, value in str_count_dict.items() if value > 2}
    
    return pd.DataFrame(common_str_dict.items(), columns = ["string", "frequency"])
