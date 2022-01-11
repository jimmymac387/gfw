# import beautiful soup to scrape web text
import requests
from bs4 import BeautifulSoup
from classes import SearchResult

BASE_URL = 'https://scholar.google.com/scholar'

HEADERS = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
}

SEARCH_LIST = [
    'wildfires+climate+change', 'wildfire+frequency', 'wildfire+intensity',
    'wildfire+management', 'wildfire+monitoring', 'wildfire+response'
]


# --------------- TO DO LIST -------------------
# identify common countries and regions in articles
# identify common researchers and affiliations in articles
# Think about how to use related searches section of page
# - Use CSS selector: 'div.gs_qsuggest > ul' (and select all li)

# This block of code scrapes title, link to an article, publication info,
# snippet, cited by results, link to related articles, link to different 
# versions of articles

def get_search_results(link, first_page=False):
    r = requests.get(link, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    search_results = soup.select('.gs_or.gs_scl')
    results_list = [SearchResult(search_result) for search_result in search_results]
    if first_page:
        nav_links = get_nav_links(soup)
        nav_links.reverse()
        return results_list, nav_links
    else:
        return results_list

def search_term_url(search_term, language='en'):
    url = BASE_URL + f'?q={search_term}&hl={language}'
    return url

def construct_nav_url(nav_item):
    return BASE_URL[:-8] + nav_item.attrs['href']

def get_nav_links(first_page):
    nav_menu = first_page.select_one('div#gs_nml')
    nav_items = nav_menu.select('.gs_nma')
    nav_links = [construct_nav_url(nav_item) for nav_item in nav_items[1:]]  # skip first (current) page
    return nav_links

# can also use SerpAPI (https://serpapi.com/dashboard)
# up to 100 searches a month
# code available here: https://python.plainenglish.io/scrape-google-scholar-with-python-fc6898419305
