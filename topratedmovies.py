import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("TMDB_KEY")

df = pd.DataFrame()

pages=int(input("Enter the number of pages you want to fetch: "))
pages = max(1, min(pages, 500))

for i in range(1,pages+1):
    response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=en-US&page={i}',timeout=20)
    response.raise_for_status()
    temp_df = pd.DataFrame(response.json()["results"])
    temp_df = temp_df[['id', 'title', 'overview', 'popularity', 'vote_count', 'vote_average', 'release_date']]  
    df = pd.concat([df,temp_df],ignore_index=True)

print(df)
df.to_csv("toprated.csv", index=False)