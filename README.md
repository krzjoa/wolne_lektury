# wolne_lektury <img src='img/wl_logo.png' align="right" height="250" />
> An unofficial REST API client for [Wolne Lektury](wolnelektury.pl) 

## Installation

You can install this library from *PyPI*

```bash
# Not yet
~~pip install wolne_lektury~~
```

or from the GitHub repo:
 
```bash
pip install git+https://github.com/krzjoa/wolne_lektury.git
```

## Usage 
```python
import wolne_lektury as wl

wl.get_authors()

# Query is automatically slugified, so you can type author names in natural language
wl.get_books(authors = "Juliusz Słowacki")
wl.get_books(authors = "adam-mickiewicz")

# 

```
