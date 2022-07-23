#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:19:37 2022

@author: krzysztof
"""

# https://bhomnick.net/design-pattern-python-api-client/
# https://www.packt.com/elegant-restful-client-python-exposing-remote-resources/


import requests
import urls
import pandas as pd

def _get_list(url: str):
    response = requests.get(url).json()
    return pd.DataFrame.from_records(response)

def get_books():
    return _get_list(urls.BOOKS)

def get_audiobooks():
    return _get_list(urls.AUDIOBOOKS)

def get_daisy():
    return _get_list(urls.DAISY)

def get_authors():
    return _get_list(urls.AUTHORS)

def get_epochs():
    return _get_list(urls.EPOCHS)

def get_genres():
    return _get_list(urls.GENRES)

def get_themes():
    return _get_list(urls.THEMES)

def get_collections():
    return _get_list(urls.COLLECTIONS)


if __name__ == '__main__':
    print(get_books())
    