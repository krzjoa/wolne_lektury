#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 23:18:39 2022

@author: krzysztof
"""

import os
import pandas as pd
from tqdm import tqdm
import urllib.request
import warnings

import urls
#from . import urls
from lists import get_books


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


def download_file(url: str, output_dir: str):
    try:
        output_path = os.path.basename(url.rstrip("/"))
        output_path = os.path.join(output_dir, output_path)
        urllib.request.urlretrieve(url, output_path) 
    except:
        warning = f"Cannot download {url}"
        warnings.warn(warning)


def download(output_dir: str,
             book_list: pd.DataFrame = None,
             book: str = None,
             author: str = None, 
             epoch: str = None, 
             genre: str = None,
             kind: str = None,
             book_type: str = urls.BOOK,
             book_format: str = urls.TXT):
    """Download files from wolnelektury.com"""
    
    if not book_list:
        book_list = get_books(
                book=book,
                author=author,
                epoch=epoch,
                genre=genre,
                kind=kind
            )
    
    book_url_list = book_list['url'].tolist()
    
    for book in tqdm(book_url_list):
        url = _get_media_url(book, 
                             book_type = book_type, 
                             book_format = book_format)
        download_file(url, output_dir)
        
        
if __name__ == '__main__':
    download("out", author="Adam Mickiewicz")
