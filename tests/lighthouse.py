import requests
import os
import json
import csv
from dotenv import load_dotenv

load_dotenv()

def performance(url):
    """Run Lighthouse tests to url
    :param url: url to test
    :return: performance score
    """

    params = { 'url': url,
        'key': os.getenv('LIGHTHOUSE_API_KEY') ,
        'strategy': 'DESKTOP',
        'category':['PERFORMANCE','ACCESSIBILITY','BEST_PRACTICES','SEO'],
        'locale': 'fi' }

    r = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed', params=params)
    if (r.status_code==200):
        data = json.loads(r.text)

        with open(r'lighthouse.csv', 'a', newline='') as csvfile:
            fields=[
                data['analysisUTCTimestamp'],
                data['id'],
                int(float(data['lighthouseResult']['categories']['performance']['score'])*100),
                int(float(data['lighthouseResult']['categories']['accessibility']['score'])*100),
                int(float(data['lighthouseResult']['categories']['best-practices']['score'])*100),
                int(float(data['lighthouseResult']['categories']['seo']['score'])*100)
            ]
            writer = csv.writer(csvfile)
            writer.writerow(fields)

        return int(float(data['lighthouseResult']['categories']['performance']['score'])*100)