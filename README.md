# Selenium Test Framework for Python

Receive alerts by
- Email (free)
- Slack (free)
- Text message (pro)
- WhatsApp message (pro)

## Test types

### Domain in search when using spesific phrase in Google

Product cards
```python
 # search term displays product
search_term.in_products('best earbuds for sleeping', 'quieton.com')
```

Ads
```python
# search term displays ads
search_term.in_ads('b2b markkinointitoimisto', 'valve.fi')
```

Results
```python
# search term displays result
search_term.in_results('b2b markkinointitoimisto', 'myynninmaailma.fi')
```