# AUTHOR: Giovanni Aratico
# FILE: Metacritic.py
# CREATED: 11-15-2021
# UPDATED: 04-30-2022
import os
from time import *
from datetime import *
import sqlite3
# EXTERNAL LIBRARIES IMPORTING
import pandas as pd
import numpy as np
# METHODS FROM OTHER FILES
from src.platform_methods import *
from src.title_methods import *
from src.local_methods import *
from src.scrape_methods import *

# DIRECTORY REFERENCES
pwd = os.getcwd()

# Values to generate correct URLs / Headers
platform_list = ['switch', 'ps', 'ps2', 'ps3', 'ps4', 'ps5', 'xbox', 'xbox360', 'xboxone', 'xbox-series-x', 'pc']
platform_title_list = ['switch', 'playstation', 'playstation-2', 'playstation-3', 'playstation-4', 'playstation-5', 'xbox', 'xbox-360', 'xbox-one', 'xbox-series-x', 'pc']
game_headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'}
# List attributes per game
title_arr, score_arr, rank_arr, url_arr, platform_arr, release_date_arr = [], [], [], [], [], []
# Combined Array / Dictionary
platform_main_arr = [title_arr, score_arr, rank_arr, url_arr, platform_arr, release_date_arr]
platform_main_dict = {'title' : title_arr,'score' : score_arr,'rank': rank_arr,'url' : url_arr,'platform' : platform_arr,'release_date' : release_date_arr}
# Attributes from each game's URL
publisher_arr, esrb_arr, developer_arr = [], [], []
# Combined Array / Dictionary
each_game_arr = [publisher_arr, developer_arr, esrb_arr]
each_game_dict = {'developer' : developer_arr, 'publisher' : publisher_arr, 'esrb' : esrb_arr}
# Local File Set
local_set_arr, local_soup_arr = [], []

''' SCRAPING METHODS '''
#main_combined_multiple(9, 20, game_headers, [platform_list[8]])
#individual_combined_timed(0, 200, game_headers, url_arr)

''' LOCAL APPENDING METHODS '''
# Stores the local file set page source code in an array
open_multiple_local_fileset(pwd, [platform_list[2], platform_list[3], platform_list[4], platform_list[5], platform_list[6], platform_list[7], platform_list[8], platform_list[9]], 0, 21, local_set_arr)
# Iterates thru local file array and parses to soup objects
local_soup_build(local_set_arr, local_soup_arr)
# Appends parsed information into arrays
local_platform_append(local_soup_arr, platform_main_dict)
game_arr = np.array([title_arr, score_arr, rank_arr, url_arr, platform_arr, release_date_arr])

''' WRITE TO FILES '''
# WRITES NP ARRAY TO CSV / TRANSPOSED CSV
platform_np = pd.DataFrame(game_arr)
platform_np.to_csv(pwd + "/db/game_db_np.csv")
platform_npT = platform_np.T
platform_npT.to_csv(pwd + "/db/game_db_npT.csv")

''' READ / SAVE FILES '''
# Reads CSV exported to
platform_read = pd.read_csv(pwd + "/db/game_db_npT.csv")

''' READ / ANALYZE FILES '''
# IN MEMORY COPY SAVED
platform_analysis = platform_read.copy()
# DROPS ROW
platform_analysis = platform_analysis.drop(index = [0])
# NAMES COLUMNS
platform_analysis.columns = ['', 'title', 'score', 'rank', 'url', 'platform', 'release_date']
# DROPS COLUMNS
platform_analysis.drop(platform_analysis.columns[[0]], axis=1, inplace=True)

# FORMATS OLD DATETIME TO BETTER FORMAT
correct_date = pd.to_datetime(platform_analysis['release_date'])
# APPENDS NEW DATE FORMAT COLUMN TO DF
platform_analysis = pd.concat([platform_analysis, correct_date], axis = 1)
# SAVES NEW VERSION
platform_analysis.to_csv(pwd + "/db/game_db_analysis.csv")

