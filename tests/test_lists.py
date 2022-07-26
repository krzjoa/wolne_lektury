#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:31:01 2022

@author: krzysztof
"""

import unittest
import numpy as np
import math
import wolne_lektury as wl

class TestLists(unittest.TestCase):
    
    def test_get_books(self):
        
        # Author
        slowacki_non_slug = wl.get_books(author = "Juliusz Słowacki")
        slowacki_slug = wl.get_books(author='juliusz-slowacki')
        
        assert len(slowacki_non_slug.compare(slowacki_slug)) == 0
        
        # Epochs
        romantism = wl.get_books(epoch="Romantyzm")
        assert "Konrad Wallenrod" in romantism.title.tolist()
        
        # Genres
        fable = wl.get_books(genre="Bajka")
        assert "Ptaszki w klatce" in fable.title.tolist()
        
        # Kinds
        drama = wl.get_books(kind="Dramat")
        assert "Zemsta" in drama.title.tolist()

    def test_authors(self):
        authors = wl.get_authors()
        assert 'adam-asnyk' in authors.slug.tolist()
    
    def test_epochs(self):
        epochs = wl.get_epochs()
        assert 'Barok' in epochs.name.tolist()
    
    def test_genres(self):
        genres = wl.get_genres()
        assert 'Aforyzm' in genres.name.tolist()
    
    def test_kinds(self):
        kinds = wl.get_kinds()
        assert 'Aforyzm' in kinds.name.tolist()

    def test_themes(self):
        themes = wl.get_themes()
        assert 'Miłość' in themes.name.tolist()
    
    def test_collections(self):
        collections = wl.get_collections()
        assert 'Biblioteczka antyczna' in collections.title.tolist()
