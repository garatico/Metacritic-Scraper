# AUTHOR: Giovanni Aratico
# FILE: title_methods.py
# CREATED: 01-04-2022
# UPDATED: 01-04-2022

from time import *
from random import randint
import requests
from bs4 import BeautifulSoup

'''
Denotes the section of functions 
that scrape a piece of info from each 
game in their critic reviews page
'''


# Gets the game's critic reviews from the URL array and gets the publisher
def publisher_find_and_append(title_soup, publisher_arr):
        publisher = title_soup.find('li', {'class' : 'summary_detail publisher'})
        publisher2 = publisher.find('span', {'class' : 'data'})
        publisher3 = publisher2.text
        publisher4 = str(publisher3)
        publisher5 = publisher4.strip()
        publisher_arr.append(publisher5)      
# Gets the game's critic reviews from the URL array and gets the ESRB rating
def esrb_find_and_append(title_soup, esrb_arr):
    esrb1 = title_soup.find('li', {'class' : 'summary_detail product_rating'})
    esrb2 = esrb1.find('span', {'class' : 'data'})
    esrb3 = esrb2.text
    esrb4 = str(esrb3)
    esrb5 = esrb4.strip()
    esrb_arr.append(esrb5)
# Gets the game's critic reviews from the URL array and gets the developer
def developer_find_and_append(title_soup, developer_arr):
    developer1 = title_soup.find('li', {'class' : 'summary_detail developer'})
    developer2 = developer1.find('span', {'class' : 'data'})
    developer3 = developer2.text
    developer4 = str(developer3)
    developer5 = developer4.strip()
    developer_arr.append(developer5)


def local_individual_append(local_soup_arr, each_game_dict):
    for soup in local_soup_arr:
        publisher_find_and_append(soup, each_game_dict['publisher'])
        esrb_find_and_append(soup, each_game_dict['esrb'])
        developer_find_and_append(soup, each_game_dict['developer'])


