# %%
import datetime
import json
import csv
import os

import requests
import pandas as pd

# %%
url = 'https://ddragon.leagueoflegends.com/cdn/15.2.1/data/pt_BR/champion.json'

resp = requests.get(url)
# %%

data = resp.json()
data

# %%

base = "/Users/joaon/OneDrive/Área de Trabalho/data-lol/contents/csv/"

# %%

def save_data(data):
    
    version = data.get("version")

    json_path = os.path.join(base,"json", f"{version}.json")
    csv_path = os.path.join(base,"json", f"{version}.csv")

    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    with open (f"/Users/joaon/OneDrive/Área de Trabalho/data-lol/contents/csv/json/{version}.json", "w") as open_file:
            json.dump(data, open_file, indent = 4)
        
   
    df = pd.DataFrame(data)
    df.to_csv(f"/Users/joaon/OneDrive/Área de Trabalho/data-lol/contents/csv/{version}.csv", index= False)
# %%
save_data(data)

# %%
