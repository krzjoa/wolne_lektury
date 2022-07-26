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
from typing import Union

from . import urls
from .lists import get_books
from .media import _get_media_url


def read_remote_text(url: str):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8") 
    except:
        return None
    
def trim_text(text: str) -> str:
    """Trim raw text
    
    It removes:
        * author
        * title
        * wolnelektury.com info appended to each text
    
    Parameters
    ----------
    text: str
        An untrimmed string with text from wolnelektur.com
    
    Returns
    -------
    str
        A trimmed string
        
    
    """
     # TODO: remove both author and title in one query
    
    # Remove author
    # See: https://stackoverflow.com/questions/15433188/what-is-the-difference-between-r-n-r-and-n
    # See: https://stackoverflow.com/questions/20056306/match-linebreaks-n-or-r-n
    # regex .* ends when encounters \r\n
    text = re.sub(r'^.*', "", text) 

    # Remove info at the end
    text = text.split("-----\r\n")[0]
    text = text.strip()
    
    # Remove title
    text = re.sub(r'^.*', "", text) 
    text = text.lstrip()
    
    return text
        

def get_texts(book_list: pd.DataFrame = None,
              book: str = None,
              author: str = None, 
              epoch: str = None, 
              genre: str = None,
              kind: str = None,
              language: Union[str, bool] = None,
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
                language=language
            )
        
    text_list = OrderedDict()
    book_url_list = book_list['url'].tolist()
    
    for book in tqdm(book_url_list):
        url = _get_media_url(book, 
                             book_type = urls.BOOK, 
                             book_format = urls.TXT)
        text = read_remote_text(url)
        
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
    texts = get_texts(author="Juliusz Słowacki", language="pol")
    
    # Trim text
    text = "Juliusz Słowacki\r\n\r\nA jednak ja nie wątpię — bo się pora zbliża…" \
        "\r\n\r\n\r\n\r\nA jednak ja nie wątpię — bo się pora zbliża,\r\nŻe"\
        " się to wielkie światło na niebie zapali,\r\nI Polski Ty, o Boże, "\
        "nie odepniesz z krzyża,\r\nAż będziesz wiedział, że się jako trup"\
        " nie zwali.\r\n\r\nDzięki Ci więc, o Boże — że już byłeś blisko,\r\n"\
        "A jeszcześ Twojej złotej nie odsłonił twarzy,\r\nAleś nas, syny Twoje,"\
        " dał na pośmiewisko,\r\nByśmy rośli jak kłosy pod deszczem potwarzy."\
        "\r\n\r\nTakiej chwały od czasu, jak na wiatrach stoi\r\n"\
        "Glob ziemski — na żadnego nie włożyłeś ducha,\r\nŻe się cichości"\
        " naszej cała ziemia boi\r\nI sądzi się, że wolna jak dziecko, "\
        "a słucha.\r\n\r\nZaprawdę w ciałach naszych światłość jakaś wielka\r\n"\
        "Balsamująca ciało — formy żywicielka,\r\n  Uwiecznica… promienie swe"\
        " dawała złote\r\n  Przez alabastry ciała.\r\n\r\n\r\n\r\n\r\n-----\r\n"\
        "Ta lektura, podobnie jak tysiące innych, dostępna jest na stronie "\
        "wolnelektury.pl.\r\nWersja lektury w opracowaniu merytorycznym i krytycznym"\
        " (przypisy i motywy) dostępna jest na stronie"\
        " http://wolnelektury.pl/katalog/lektura/a-jednak-ja-nie-watpie-bo-sie-pora-zbliza.\r\n\r\n"\
        "Utwór opracowany został w ramach projektu Wolne Lektury przez "\
        "fundację Nowoczesna Polska.\r\n\r\nTen utwór nie jest objęty majątkowym"\
        " prawem autorskim i znajduje się w domenie publicznej, co oznacza że"\
        " możesz go swobodnie wykorzystywać, publikować i rozpowszechniać. "\
        "Jeśli utwór opatrzony jest dodatkowymi materiałami (przypisy, motywy literackie etc.),"\
        " które podlegają prawu autorskiemu, to te dodatkowe materiały udostępnione"\
        " są na licencji Creative Commons Uznanie Autorstwa – Na Tych Samych "\
        "Warunkach 3.0 PL (http://creativecommons.org/licenses/by-sa/3.0/).\r\n\r\nTekst "\
        "opracowany na podstawie: Juliusz Słowacki, Liryki i powieści poetyckie, "\
        "Zakład Narodowy im. Ossolińskich, Wrocław 1974\r\n\r\nWydawca: "\
        "Fundacja Nowoczesna Polska\r\n\r\nPublikacja zrealizowana w ramach "\
        "projektu Wolne Lektury (http://wolnelektury.pl). Reprodukcja cyfrowa "\
        "wykonana przez Bibliotekę Narodową z egzemplarza pochodzącego ze zbiorów BN."\
        "\r\n\r\nOpracowanie redakcyjne i przypisy: Marta Niedziałkowska, "\
        "Aleksandra Sekuła.\r\n"
        
    trim_text(text)


    
    