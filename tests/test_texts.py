#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 22:22:00 2022

@author: krzysztof
"""

import unittest
import numpy as np
import math
import wolne_lektury as wl
from collections import OrderedDict

class TestTexts(unittest.TestCase):
    
    def get_texts(self):
        mickiewicz_texts = wl.get_texts(author="Adam Mickiewicz")
        assert type(mickiewicz_texts) == OrderedDict
        assert len(mickiewicz_texts) > 10
    
    def test_trim_text(self):
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
        wl.trim_text(text)
