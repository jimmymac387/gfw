# --------------------------------------------------------------
# TO DO
# Think about how to use related searches section of page
# - Use CSS selector: 'div.gs_qsuggest > ul' (and select all li)
# --------------------------------------------------------------
# from network_analysis import BASE_URL
import re

BASE_URL = 'https://scholar.google.com/scholar'

def get_title_section(search_result):
    title_section_selectors = '.gs_r > .gs_ri > .gs_rt > a'  # make dict of selectors instead of this dumb stuff
    title_section = search_result.select_one(title_section_selectors)
    return title_section

def get_author_section(search_result):
    author_section_selectors = 'div.gs_a'
    author_section = search_result.select_one(author_section_selectors)
    return author_section

def get_citation_section(search_result):
    citation_section_selectors = 'div.gs_rs + div.gs_fl'
    citation_section = search_result.select_one(citation_section_selectors)
    return citation_section

def get_title(title_section):
    title = title_section.get_text()
    print('Found title...')
    return title

def get_title_link(title_section):
    title_link = title_section.attrs['href']
    print('Found title link...')
    return title_link
    
def get_authors(author_section):
    author_list = author_section.select('a')
    authors = [author.string for author in author_list]
    print('Found authors...')
    return authors
    
def get_year(author_section):
    search_string = author_section.contents[-1]
    year = re.search('\d{4}', search_string).group(0)
    print('Found year...')
    return int(year)

def get_pdf_link(search_result):
    pdf_link = search_result.select_one('div.gs_or_ggsm a')
    if pdf_link:
        print('Found pdf link...')
        return pdf_link.attrs['href']
    
def get_cited_count(citation_section):
    # find a way to make the citation_section.select('a') call once
    search_string = citation_section.select('a')[2].string
    cited_count = re.search('\d+', search_string).group(0)
    print('Found cited count...')
    return int(cited_count)
    
def get_cited_by_link(citation_section):
    cited_by_clip = citation_section.select('a')[2].attrs['href']
    cited_by_link = BASE_URL[:-8] + re.search('^[^&]+', cited_by_clip).group(0)
    return cited_by_link
    
def get_related_link(citation_section):
    related_clip = citation_section.select('a')[3]['href']
    related_link = BASE_URL[:-8] + related_clip
    return related_link


class SearchResult:
    def __init__(self, search_result):
        # get sections
        title_section = get_title_section(search_result)
        author_section = get_author_section(search_result)
        citation_section = get_citation_section(search_result)

        # extract values
        self.title = get_title(title_section)
        self.title_link = get_title_link(title_section)
        self.authors = get_authors(author_section)
        self.year = get_year(author_section)
        self.pdf_link = get_pdf_link(search_result)
        # self.citation_link = self.get_citation_link(citation_section)
        self.cited_by_count = get_cited_count(citation_section)
        self.cited_by_link = get_cited_by_link(citation_section)
        self.related_link = get_related_link(citation_section)

    def peak(self):
        return (
            f'Title: {self.title}/n'
            f'Title Link: {self.title_link}/n'
            f'Authors: {self.authors}/n'
            f'Year: {self.year}/n'
            f'PDF Link: {self.pdf_link}/n'
            f'Number of times cited: {self.cited_by_count}'
            f'Cited by link: {self.cited_by_link}/n'
            f'Related articles link: {self.related_link}/n'
        )

    # this one is surprisingly difficult (hid behind some javascript)
    # come back and update
    # def get_citation_link(search_result):
    #     search_result.select_one('div.gs_fl > a.gs_nph')
    #     if pdf_link:
    #         return pdf_link

#---------------------------------------------------------------------#
# class JournalArticle:
#     def __init__(self, title, journal, year):
#         self.title = title
#         self.authors = []
#         self.keywords = []
#         self.citations = []
#         self.journal = journal
#         self.publish_year = year
#         self.cited_by = []
#         # self.affiliations = dict()  # figure out how to implement later
    
#     def add_abstract(self, abstract):
#         self.abstract = abstract

#     def add_author(self, author):
#         self.authors.append(author)

#     def add_keyword(self, keyword):
#         self.keywords.append(keyword)

#     def add_citation(self, citation):
#         self.citations.append(citation)
    
#     def add_cited_by(self, article):
#         self.cited_by.append(article)

#     # def set_authors(self, authors, affiliations):
#     #     self.authors = authors
    
#     # def set_keywords(self, keywords):
#     #     self.keywords = keywords