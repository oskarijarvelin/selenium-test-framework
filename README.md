# Selenium Test Framework for Python

Receive alerts by
- Email (free)
- Slack (free)
- Text message (pro)
- WhatsApp message (pro)

## Test types

### Search term in Google

```python
 # search term displays product
search_term.in_products('best earbuds for sleeping', 'quieton.com')
```

```python
# search term displays ads
search_term.in_ads('b2b markkinointitoimisto', 'valve.fi')
```

```python
# search term displays result
search_term.in_results('b2b markkinointitoimisto', 'myynninmaailma.fi')
```