# %%
import datetime
import json
import csv

import requests
import pandas as pd

# %%
url = 'https://ddragon.leagueoflegends.com/cdn/15.2.1/data/pt_BR/champion.json'

resp = requests.get(url)
# %%

data = resp.json()
data
# %%

def save_data(data, option = "csv"):
    
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")

    if option == "json":
        with open (f"/Users/joaon/OneDrive/Área de Trabalho/Lol/contents/csv/json/{now}.json", "w") as open_file:
            json.dump(data, open_file, indent = 4)
        
    elif option == "csv":
        df = pd.DataFrame(data)
        df.to_csv(f"/Users/joaon/OneDrive/Área de Trabalho/Lol/contents/csv/{now}.csv", index= False)
# %%
save_data(data)
