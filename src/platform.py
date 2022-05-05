import os
from sys import platform
from time import *
from random import randint

import requests
from bs4 import BeautifulSoup
from src.local import *

pwd = os.getcwd()

'''
Denotes the section of functions 
that scrape a piece of info from each 
game in the top games list
'''
# REQUESTS METHOD
def request_and_build(pwd, platform, page, headers):
    game_page = platform_url_builder(platform, page)
    game_page_html = requests.get(game_page, headers=headers)
    game_soup = BeautifulSoup(game_page_html.text, 'lxml')
    return game_soup
# Builds the URL of the platform page to index
def platform_url_builder(platform, page):
    platform_page = f'https://www.metacritic.com/browse/games/score/metascore/all/{platform}/filtered?page={page}'
    return platform_page

# Finds all title elements from passed in soup object and appends them to array
def title_find_and_append(game_soup, title_arr):
    for title in game_soup.find_all('a', class_ = "title"):
        game_title = title.text
        title_arr.append(game_title)
# Finds all score elements and appends them to array
def score_find_and_append(game_soup, score_arr):
    for score in game_soup.find_all('div', class_ = 'clamp-score-wrap'):
            game_score = score.text
            game_score = game_score.replace('\n', '')
            score_arr.append(game_score)
# Finds all rank elements and appends them to array
def rank_find_and_append(game_soup, rank_arr):
    for rank in game_soup.find_all('span', {'class' : 'title numbered'}):
        game_rank = rank.text
        game_rank = game_rank.strip()
        rank_arr.append(game_rank)
# Finds all URL elements and appends them to array
def url_find_and_append(game_soup, url_arr):
    for url in game_soup.find_all('td', {'class' : 'clamp-summary-wrap'}):
        game_url2 = url.find('a')
        game_url3 = game_url2.get('href')
        game_url4 = game_url3.replace('critic-reviews', '')
        game_url5 = 'https://www.metacritic.com' + game_url4
        url_arr.append(game_url5)
# Finds all platform elements and appends them to array
def platform_find_and_append(game_soup, platform_arr):
    for platform in game_soup.find_all('div', {'class' : 'clamp-details'}):
        platform2 = platform.find('span', {'class' : 'data'})
        platform3 = platform2.text
        platform4 = str(platform3).strip()
        platform_arr.append(platform4)
# Finds all release date elements and appends them to array
def release_date_find_and_append(game_soup, release_date_arr):
    for date in game_soup.find_all('div', {'class' : 'clamp-details'}):
        date2 = date.find('div', {'class' : 'platform'})
        date3 = date2.find_next_sibling()
        date4 = date3.text
        release_date_arr.append(date4)

# Finds all information from local files to append to dictionary elements
def local_platform_append(local_soup_arr, platform_main_dict):
    for soup in local_soup_arr:
        title_find_and_append(soup, platform_main_dict['title'])
        score_find_and_append(soup, platform_main_dict['score'])
        rank_find_and_append(soup, platform_main_dict['rank'])
        url_find_and_append(soup, platform_main_dict['url'])
        platform_find_and_append(soup, platform_main_dict['platform'])
        release_date_find_and_append(soup, platform_main_dict['release_date'])

