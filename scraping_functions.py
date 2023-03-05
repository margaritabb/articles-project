#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: margaritabozhinova
"""


def get_links(homepage):
    """
    Take the homepage link, return a list of article links to scrape.

    """

    import requests
    from scrapy import Selector

    # Retrieve links from home page
    response_homepage = requests.get("https://nationalpost.com/")
    html_homepage = response_homepage.text
    sel_homepage = Selector(text=html_homepage)

    return sel_homepage.xpath('//article[contains(@class, "article-card")]').extract()


def get_article_ids(links):
    """
    Take list of article links to scrape, return the article IDs.

    """
    import re

    ids = []
    regex_id = re.compile('(?:"target_article_id": ")([a-z0-9-]*)(?:")')

    for article in links:
        if regex_id.search(article) is not None:
            ids.append(regex_id.search(article).group(1))

    return ids


def get_article_urls(links):
    """
    Take list of article links to scrape, return the article URLs.

    """
    import re

    urls = []
    regex_url = re.compile('(?:"target_url": ")(https.+?)(?:")')

    for article in links:
        if regex_url.search(article) is not None:
            urls.append(regex_url.search(article).group(1))

    return urls


def get_article_text(urls):
    """
    Take list of article URLs to scrape and scrape the articles' text.
    Return nested list of article paragraphs. 
    Each article's text is a list
    item containing a list of paragraphs.

    """
    from scrapy import Selector

    import requests

    article_text = []

    for url in urls:
        response = requests.get(url)
        html = response.text
        sel = Selector(text=html)

        scraped_text = sel.xpath("//p[not(@class)]").extract()
        article_text.append(scraped_text)

    return article_text
