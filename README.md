# wolne_lektury
A REST API client for Wolne Lektury with additional utils

## Usage 
```python
import wolne_lektury as wl

wl.get_authors()

# Query is automatically slugified, so 
wl.get_books(authors = "Juliusz Słowacki")

```
