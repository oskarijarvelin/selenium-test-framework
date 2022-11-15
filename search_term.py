from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.parse

def in_products(searchPhrase, targetDomain):
    """Run Google search with search phrase and check if search results has product card for wanted domain
    :param searchPhrase: search phrase in plain text
    :param targetDomain: domain we look for in ads
    :return: boolean whether product ad for domain has been found
    """
    
    driver = webdriver.Chrome()

    encodedSearchPhrase = urllib.parse.quote(searchPhrase.replace(" ", "-"))

    driver.get("https://www.google.com/search?q=" + encodedSearchPhrase)

    if driver.find_elements(By.CSS_SELECTOR, 'a.clickable-card[href*="' + targetDomain + '"]'):
        print('Search phrase "' + searchPhrase + '" contains product card for the website ' + targetDomain)
        return True
    else:
        print('Search phrase "' + searchPhrase + '" DOES NOT contain product card for the website ' + targetDomain)
        return False

    driver.quit()

def in_ads(searchPhrase, targetDomain):
    """Run Google search with search phrase and check if any ads for wanted domain. Does not include search results
    :param searchPhrase: search phrase in plain text
    :param targetDomain: domain we look for in ads
    :return: boolean whether results for domain has been found
    """
    
    driver = webdriver.Chrome()

    encodedSearchPhrase = urllib.parse.quote(searchPhrase.replace(" ", "-"))

    driver.get("https://www.google.com/search?q=" + encodedSearchPhrase)

    if driver.find_elements(By.CSS_SELECTOR, 'div[role="region"] a[href*="' + targetDomain + '"]'):
        print('Search phrase "' + searchPhrase + '" contains ads for the website ' + targetDomain)
        return True
    else:
        print('Search phrase "' + searchPhrase + '" DOES NOT contain ads for the website ' + targetDomain)
        return False

    driver.quit()

def in_results(searchPhrase, targetDomain):
    """Run Google search with search phrase and check if any search results for wanted domain. Does not include ads
    :param searchPhrase: search phrase in plain text
    :param targetDomain: domain we look for in ads
    :return: boolean whether results for domain has been found
    """
    
    driver = webdriver.Chrome()

    encodedSearchPhrase = urllib.parse.quote(searchPhrase.replace(" ", "-"))

    driver.get("https://www.google.com/search?q=" + encodedSearchPhrase)

    if driver.find_elements(By.CSS_SELECTOR, 'div[role="main"] link[href*="' + targetDomain + '"]'):
        print('Search phrase "' + searchPhrase + '" contains results for the website ' + targetDomain)
        return True
    else:
        print('Search phrase "' + searchPhrase + '" DOES NOT contain results for the website ' + targetDomain)
        return False

    driver.quit()