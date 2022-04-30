# AUTHOR: Giovanni Aratico
# FILE: local_methods.py
# CREATED: 01-11-2022
# UPDATED: 04-29-2022
import os
import datetime
from src.platform_methods import *
from bs4 import BeautifulSoup

''' HTML BASED METHODS '''

# Iterates thru local file array and parses to soup objects
def local_soup_build(local_set_arr, local_soup_arr):
    for file in local_set_arr:
        game_soup = BeautifulSoup(file, 'lxml')
        local_soup_arr.append(game_soup)

# OPENS FILE LOCALLY
def open_local_file(path, platform, file_count, local_set_arr):
    path = path + f'/local/{platform}/{platform}-{file_count}.html'
    try:
        with open(path, 'rb') as f:
            local_set_arr.append(f.read())
    except FileNotFoundError:
        print('File ' + str(path) + ' not found!')


def open_multiple_local_fileset(path, consoles, start_file, end_file, local_set_arr):
    for g in consoles:
        open_local_fileset(path, g, start_file, end_file, local_set_arr)

# OPENS SET OF LOCAL FILES
def open_local_fileset(path, platform, start_file, end_file, local_set_arr):
    end_file += 1
    for file in range(start_file, end_file):
        open_local_file(path, platform, file, local_set_arr)

# LOCAL PAGE SAVING FUNCTIONS
def if_page_has_content(temp_soup):
    content = temp_soup.find('div', id="main_content")
    content2 = content.find('div', class_="title_bump")
    content3 = content2.text
    content3 = content3.replace('\n', '')
    content3 = content3.replace(' ', '')
    if "Nogamesfound." in content3: 
        return False
    else:
        return True
# USED TO SAVE ONLY THE TEXT OUTPUT OF THE PAGE
def to_local_parser(pwd, page, page_html):
    print('LOCAL PARSER REACHED')
    parser_path = path_name_builder('test', page, pwd)
    test_soup = BeautifulSoup(page_html.text, 'lxml')
    
    # GETS THE CURRENT THE CURRENT DATE AND TIME TO RECORD
    scrape_datetime = datetime.datetime.now()
    
    # INSERTS DATE TIME LOG INTO HTML
    date_log_tag = test_soup.new_tag("p")
    date_log_tag.string = str(scrape_datetime)
    test_soup.div.insert_before(date_log_tag)

    test_soup_encoded = bytes(test_soup.text, 'UTF-8')
    with open(parser_path, 'wb') as output:
        output.write(test_soup_encoded)
# USED TO SAVE A LOCAL COPY OF THE HTML FOR PARSING
def to_local_copy(soup, path):
    # GETS THE CURRENT THE CURRENT DATE AND TIME TO RECORD
    scrape_datetime = datetime.datetime.now()
     # INSERTS DATE TIME LOG INTO HTML
    date_log_tag = soup.new_tag("p")
    date_log_tag.string = str(scrape_datetime)
    soup.div.insert_before(date_log_tag)
    # COVERTS SOUP OBJECT TO BYTES FOR STORAGE
    page = soup.encode('utf-8')
    # SAVES THE FILES
    with open(path, 'wb') as output:
        output.write(page)
# BUILDS FILE NAME TO SAVE LOCAL FILES
def page_name_builder(platform, page_number):
    return f'{platform}-{page_number}.html'

def page_name_individual_builder(platform, game):
    return f'{game}-{platform}.html'

# BUILDS PATH TO SAVE LOCAL FILES
def path_name_builder(platform, page_number, pwd):
    local_path = 'local'
    # Checks if directory for platform exists
    new_path_check = os.path.isdir(pwd + f'/{local_path}/{platform}/')
    page_filename = page_name_builder(platform, page_number)

    if (not new_path_check):
        os.mkdir(os.path.join(pwd, local_path, platform))
        return path_name_builder(platform, page_number, pwd)
    elif (new_path_check):
        new_path_push = os.path.join(pwd, local_path, platform, page_filename)
        return new_path_push


def path_name_builder_individual(platform, game, page_number, pwd):
    local_path = 'local'
    individual = 'individual'
    # Checks if directory for platform exists
    new_path_check = os.path.isdir(pwd + f'/{local_path}/{individual}/{platform}/')
    page_filename = page_name_individual_builder(platform, game)
    if (not new_path_check):
        os.mkdir(os.path.join(pwd, local_path, individual, platform))
        return path_name_builder_individual(platform, page_number, pwd)
    elif (new_path_check):
        new_path_push = os.path.join(pwd, local_path, individual, platform, page_filename)
        return new_path_push