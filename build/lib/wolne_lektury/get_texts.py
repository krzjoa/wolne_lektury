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
from collections import OrderedDict
from tqdm import tqdm

from . import urls
from .get_lists import get_books


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
    # Use regex, not working with Pan Tadeusz
    text = text[:-1264]
    
    # Trailing \r\n ???
    
    return text
        

def get_texts(book_list: pd.DataFrame = None,
              book: str = None,
              author: str = None, 
              epoch: str = None, 
              genre: str = None,
              kind: str = None, 
              theme: str = None, 
              collection: str = None, 
              trim: bool = True) -> OrderedDict:
    """Get texts according to the defined query of passed book list
    
    Parameters
    ----------
    book: str
        The book title. If specified, you should not pass any other options.
    author: str
        A selected author. Can be combined with other arguments (excluding book_list and book).
    epoch: str
        A selected epoch. Can be combined with other arguments (excluding book_list and book).
    genre: str
        A seleted genre. Can be combined with other arguments (excluding book_list and book).
    kind: str
        A selected kind. Can be combined with other arguments (excluding book_list and book).
    theme: str
        A selected theme. Can be combined with other arguments (excluding book_list and book).
    collection: str
        A selected theme. Can be combined with other arguments (excluding book_list and book).
    trim: bool
        Remove author, title and the "Wolne Lektury" info at the end.
        
    Returns
    -------
    OrderedDict
        An OrderedDict, where keys are urls an values are strings with book text
    
    """
    
    if not book_list:
        book_list = get_books(
                book=book,
                author=author,
                epoch=epoch,
                genre=genre,
                kind=kind,
                theme=theme,
                collection=collection
            )
        
    text_list = OrderedDict()
    book_url_list = book_list['url'].tolist()
    
    for book in tqdm(book_url_list):
        url = _get_media_url(book, 
                             book_type = urls.BOOK, 
                             book_format = urls.TXT)
        text = read_remote(url)
        
        if text:
            if trim:
                text = trim_text(text)
            text_list.update({url : text})
        else:
            warning = f"{url} not found and skipped."
            warnings.warn(warning)
     
    return text_list
    
    
if __name__ == '__main__':
    # pan_tadeusz = get_texts(book="Pan Tadeusz")
    texts = get_texts(author="Juliusz Słowacki")
    