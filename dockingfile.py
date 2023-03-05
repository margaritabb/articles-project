#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 09:19:35 2023

@author: margaritabozhinova

This file combines the three module that scrape, process and
load the articles data to a SQLite database. 
"""

import os
import pandas as pd

os.chdir("/Users/margaritabozhinova/Desktop/ArticlesProject/Pipeline/")

# Scrape

import scraping_functions

links = scraping_functions.get_links("https://nationalpost.com/")

ids = scraping_functions.get_article_ids(links)

urls = scraping_functions.get_article_urls(links)

articles_text = scraping_functions.get_article_text(urls)

# Transform

import cleaning_functions

clean_text = cleaning_functions.clean_article_text(articles_text)

article_df = pd.DataFrame(
    list(zip(ids, urls, clean_text)), columns=["id", "url", "text"]
)

# Load to SQLite database

import loading_functions

dbfilepath = "/Users/margaritabozhinova/Desktop/ArticlesProject/Database/dbfile.db"

if not os.path.isfile(dbfilepath):
    loading_functions.create_table(dbfilepath)

loading_functions.load_data(dbfilepath, article_df)
