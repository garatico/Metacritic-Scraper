'''
from sys import platform
from random import randint

#filepath = pwd + "/db/game_db_sql"

# DATE / TIME REFERENCES
todays_date = datetime.date.today()
todays_year = str(todays_date.year)
todays_month = str(todays_date.month)
todays_day = str(todays_date.day)
print(todays_month + "." + todays_day + "." + todays_year)

# TRANSPOSES DATA TO CORRECT FORMAT
platform_np = platform_np.T
#Transforms copy and writes to dbT
platform_read_copy = platform_read_copy.T
platform_read_copy.to_csv(pwd + "/db/game_db_npT.csv")


'''

''' WORKFLOW TESTING
# WRITES NP ARRAY TO CSV
platform_np = pd.DataFrame(game_arr)
#platform_np = platform_np.T
platform_np.to_csv(pwd + "/db/game_db_np.csv")
# WRITES TO DICT TO CSV
platform_pd_dict = pd.DataFrame(platform_main_dict)
platform_pd_dict.to_csv(pwd + "/db/game_db.csv")

'''


'''
# SQL CODE
game_db_connect = sqlite3.connect(filepath)
game_db_cursor = game_db_connect.cursor()
game_db_cursor.execute(""" DROP TABLE meta_games """)
game_db_cursor.execute("""CREATE TABLE meta_games (
                            title TEXT,
                            score INTEGER,
                            rank TEXT,
                            url TEXT,
                            platform TEXT,
                            release_date TEXT,
                            developer TEXT,
                            publisher TEXT,
                            esrb TEXT
                                                    )""")
game_db_cursor.execute("INSERT INTO meta_games VALUES ")
game_db_connect.commit()
game_db_connect.close()
'''