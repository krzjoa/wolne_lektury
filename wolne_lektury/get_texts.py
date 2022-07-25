#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:35:38 2022

@author: krzysztof
"""

import os
import re
import pandas as pd
import urllib.request
import warnings

import urls
from get_lists import get_books


def _get_media_url(book_name: str, 
                   book_type: str, 
                   book_format: str):
    
    book_name = os.path.basename(book_name.rstrip("/"))
    book_name = f"{book_name}.{book_format}"
    return os.path.join(urls.MAIN, 
                        urls.MEDIA,
                        book_type,
                        book_format,
                        book_name)


def read_remote(url: str):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8") 
    except:
        return None
    
def trim_text(text):
    # Remove author and title
    text = re.sub(r'^.*\r\n\r\n\r\n\r\n?', "", text)
    
    # Remove info at the end
    # Last 1263, but it may change
    text = text[:-1264]
    
    # Trailing \r\n ???
    
    return text
    
    
        

def get_texts(book_list: pd.DataFrame = None,
              author: str = None, 
              epoch: str = None, 
              genre: str = None,
              kind: str = None, 
              theme: str = None, 
              collection: str = None, 
              trim: bool = True):
    """Get texts according to the defined query of passed book list"""
    
    # TODO: add tqdm
    # TODO: encoding
    
    if not book_list:
        book_list = get_books(
                author=author,
                epoch=epoch,
                genre=genre,
                kind=kind,
                theme=theme,
                collection=collection
            )
        
    text_list = []
    book_url_list = book_list['url'].tolist()
    
    for book in book_url_list:
        url = _get_media_url(book, 
                             book_type = urls.BOOK, 
                             book_format = urls.TXT)
        text = read_remote(url)
        
        if text:
            if trim:
                text = trim_text(text)
            text_list.append(text)
        else:
            warnings.warn(f"{url} not found and skipped.")
    
    
    return text_list
    
    
if __name__ == '__main__':
    texts = get_texts(author="Juliusz Słowacki")
    