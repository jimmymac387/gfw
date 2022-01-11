from time import sleep
from classes import SearchResult
from utils import SEARCH_LIST, get_search_results, search_term_url



# def select_search_results(page):
#     return page.select('.gs_or.gs_scl')

# def convert_search_results(search_result_list):
#     return [SearchResult(search_result) for search_result in search_result_list]
# def get_all_search_results():
#     pass

# run search for one search term at a time
search_term = SEARCH_LIST[0]
search_link = search_term_url(search_term)
# returns list of search result objects
search_results, nav_links = get_search_results(search_link, first_page=True)

while nav_links:
    nav_link = nav_links.pop()
    search_results += get_search_results(nav_link)
    sleep(2)


# search_link = search(search_term)

# def get_search_results(link):
#     r = requests.get(link, headers=HEADERS)
#     soup = BeautifulSoup(r.text), 'lxml')
#     search_results = get_search_results(soup)

# get first page of search results
# first_page = BeautifulSoup(search_link), 'lxml')

# create list of search results from first page
# search_result_list = select_search_results(first_page)
# search_result = search_results[1]
# search_result
# t = SearchResult(search_results[1])

# convert the search results to a result object
# search_results = convert_search_results(search_result_list)
# get all the navigation links
# nav_links = get_nav_links(first_page)
# nav_links.reverse()

while nav_links:
    nav_link = nav_links.pop()
    search_results += get_search_results(nav_link)

# for nav_link in nav_links:
#     r = requests.get(nav_link, headers=HEADERS)
#     next_page = BeautifulSoup(r.text, 'lxml')
#     search_results = get_search_results(next_page)
#     t3 = [SearchResult(search_result) for search_result in search_results]
#     t2 + t3

# nav_links.reverse()
# while t2:
#     nav_link = nav_links.pop()
#     r = requests.get(nav_link, headers=HEADERS)
#     return r.text

#
# search_results_page = 

# get a list of search results for each page
