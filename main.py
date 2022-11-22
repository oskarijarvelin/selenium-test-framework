from tests.lighthouse import performance
from tests.google_search import domain_in_products
from tests.google_search import domain_in_ads
from tests.google_search import domain_in_results
from tests.google_search import domain_position_in_results
import send

def main():

    # performance('https://myynninmaailma.fi')

    # search term displays product
    # domain_in_products('best earbuds for sleeping', 'quieton.com')

    # search term displays ads
    # domain_in_ads('b2b markkinointitoimisto', 'valve.fi')

    # search term displays result
    # domain_in_results('b2b markkinointitoimisto', 'myynninmaailma.fi')

    # search term position in search results
    domain_position_in_results('b2b markkinointitoimisto', 'myynninmaailma.fi')

    # send email
    # send.email('matti.meikalainen@esimerkki.fi', 'Sähköpostin otsikko', 'Sähköpostin sisältö')

    # send slack message
    # send.slack('Viestin sisältö')

if __name__ == "__main__":
    main()