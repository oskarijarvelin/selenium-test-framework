import search_term
import send

def main():

    # search term displays product
    search_term.in_products('best earbuds for sleeping', 'quieton.com')

    # search term displays ads
    search_term.in_ads('b2b markkinointitoimisto', 'valve.fi')

    # search term displays result
    search_term.in_results('b2b markkinointitoimisto', 'myynninmaailma.fi')

    # send email
    # send.email('matti.meikalainen@esimerkki.fi', 'Sähköpostin otsikko', 'Sähköpostin sisältö')

    # send slack message
    # send.slack('Viestin sisältö')

if __name__ == "__main__":
    main()