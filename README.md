# Selenium Test Framework for Python

Download WebFriver for Chome from [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Create API Keys for SendGrid [here](https://docs.sendgrid.com/ui/account-and-settings/api-keys)

Install depencies: `pip install selenium python_dotenv sendgrid`

Receive alerts by
- Email (free)
- Slack (free)
- Text message (~$0.09 / alert, first 1 000 alerts in month for free)
- WhatsApp message (~$0,14 / alert, first 1 000 alerts in month for free)

## Test types

### Google Search

Product cards
```python
 # search term displays product
domain_in_products('best earbuds for sleeping', 'quieton.com')
```

Ads
```python
# search term displays ads
domain_in_ads('b2b markkinointitoimisto', 'valve.fi')
```

Results
```python
# search term displays result
domain_in_results('b2b markkinointitoimisto', 'myynninmaailma.fi')
```

Position in results
```python
# domain position in search results for search term
domain_position_in_results('b2b markkinointitoimisto', 'myynninmaailma.fi')
```

### Lighthouse

Performance
```python
 # Get performance score
performance('https://myynninmaailma.fi')
```