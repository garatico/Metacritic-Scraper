# AUTHOR: Giovanni Aratico
# FILE: local_methods.py
# CREATED: 02-02-2022
# UPDATED: 02-03-2022

from src.local_methods import *
from src.platform_methods import *
from src.title_methods import *


# Runs the main scraping function for a list of consoles
def main_combined_multiple(start_page, end_page, game_headers, consoles):
    for g in consoles:
        print(g + " starting scrape.")
        main_combined_timed(start_page, end_page, game_headers, g)

# Saves the ranked games by platform original pages for one platform
def main_combined_timed(start_page, end_page, game_headers, platform):
    # Scrapes from all pages inside and including range
    end_page += 1
    # Iterates throught the pages and generates a request using the parameters
    for page in range(start_page, end_page):
        # TEST METHOD FOR SIZING DOWN FILE
        game_soup = request_and_build(pwd, platform, page, headers = game_headers)
        # Checks if page contains content, halts process if there is no content
        if_content = if_page_has_content(game_soup)
        path_name = path_name_builder(platform, page, pwd)

        if (if_content):
            to_local_copy(game_soup, path_name)
            pass
        elif (not if_content):
            break
        # Timer to ensure pages not scraped too fast
        sleep(randint(2,10))


def individual_combined_timed(start_page, end_page, individual_headers, url_arr):
    for page in range (start_page, end_page):
        # REQUESTS INDIVIDUAL TITLES
        title_page_html = requests.get(url_arr[page], headers = individual_headers)
        title_soup = BeautifulSoup(title_page_html.text, 'lxml')

        platform_substring = url_arr[page].split('/')
        platform = platform_substring[4]
        game = platform_substring[5]

        # Checks if page contains content, halts process if there is no content
        path_name = path_name_builder_individual(platform, game, page, pwd)
        to_local_copy(title_soup, path_name)

        # Timer to ensure pages not scraped too fast
        sleep(randint(2,10))
