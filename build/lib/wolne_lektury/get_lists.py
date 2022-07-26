#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:19:37 2022

@author: krzysztof
"""

import requests
import pandas as pd
import os
from slugify import slugify

from . import urls

def _get_list(url: str, normalize: bool = False) -> pd.DataFrame:
    url = os.path.join(urls.API, url)
    response = requests.get(url).json()
    # if normalize:
    #     response = pd.json_normalize(response)
    return pd.DataFrame.from_records(response)


def _q(path_type: str, query: str):
    """Prepare query"""
    return "" if not query else os.path.join(path_type, slugify(query))


def _chained_book_query(book: str = None,
                        author: str = None, 
                        epoch: str = None, 
                        genre: str = None,
                        kind: str = None, 
                        theme: str = None, 
                        collection: str = None, 
                        book_type: str = 'books'):
    
    available_book_types = [urls.BOOKS, urls.AUDIOBOOKS, urls.DAISY]
    
    if book_type not in available_book_types:
        raise ValueError(f"You passed {book_type} as book type, which is none" \
                         f"of {*available_book_types,}")
    
    if book:
        query = os.path.join(urls.BOOKS, slugify(book))
        normalize = True
    else:
        query = os.path.join(
                _q(urls.AUTHORS, author),
                _q(urls.EPOCHS, epoch),
                _q(urls.GENRES, genre),
                _q(urls.KINDS, kind),
                _q(urls.THEMES, theme),
                _q(urls.COLLECTIONS, collection),
                book_type
            )
        normalize = False
        
    return _get_list(query, normalize=normalize)
    
    
def get_books(book: str = None,
              author: str = None, 
              epoch: str = None, 
              genre: str = None,
              kind: str = None, 
              theme: str = None, 
              collection: str = None) -> pd.DataFrame:
    """Get list of books"""
    return _chained_book_query(book, author, epoch, genre, 
                               kind, theme, collection, 
                               book_type=urls.BOOKS)

def get_audiobooks(book: str = None, 
                   author: str = None, 
                   epoch: str = None, 
                   genre: str = None,
                   kind: str = None, 
                   theme: str = None, 
                   collection: str = None) -> pd.DataFrame:
    """Get list of audiobooks"""
    return _chained_book_query(book, author, epoch, genre, 
                               kind, theme, collection, 
                               book_type=urls.AUDIOBOOKS)

def get_daisy(book: str = None,
              author: str = None, 
              epoch: str = None, 
              genre: str = None,
              kind: str = None, 
              theme: str = None, 
              collection: str = None) -> pd.DataFrame:
    """Get list of books in DAISY version"""
    return _chained_book_query(book, author, epoch, genre, 
                               kind, theme, collection, 
                               book_type=urls.DAISY)


# TODO: define specific author, epoch etc.

def get_authors() -> pd.DataFrame:
    """Get list of authors"""
    return _get_list(urls.AUTHORS)


def get_epochs() -> pd.DataFrame:
    """Get list of epochs"""
    return _get_list(urls.EPOCHS)


def get_genres() -> pd.DataFrame:
    """Get list of genres"""
    return _get_list(urls.GENRES)


def get_kinds() -> pd.DataFrame:
    """Get list of kinds"""
    return _get_list(urls.KINDS)


def get_themes() -> pd.DataFrame:
    """Get list of themes"""
    return _get_list(urls.THEMES)


def get_collections() -> pd.DataFrame:
    """Get list of collections"""
    return _get_list(urls.COLLECTIONS)


if __name__ == '__main__':
    book = get_books(book="Pan Tadeusz") 
    # books = get_books(author="Juliusz Słowacki") 
    # print(get_books(author="Juliusz Słowacki"))
    