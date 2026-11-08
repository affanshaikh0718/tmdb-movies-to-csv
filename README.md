# TMDB Top Rated Movies to CSV

A small Python project that fetches top-rated movies from the [TMDB API](https://www.themoviedb.org/documentation/api), cleans the data with pandas, and saves it as a CSV file.

I built this to learn how APIs work, how JSON data is handled in Python, and how to keep secrets (API keys) safe when using GitHub.

## What it does

1. Asks how many pages of movies you want (20 movies per page, max 500 pages).
2. Calls the TMDB `top_rated` endpoint once per page using `requests`.
3. Converts each page's JSON response into a pandas DataFrame.
4. Keeps only the useful columns and combines all pages into one table.
5. Saves the result to `toprated.csv`.


## Setup

**1. Clone the repo and install the libraries**
```
pip install -r requirements.txt
```

**2. Get a free TMDB API key**
Create an account at themoviedb.org, then go to Settings, then API, and request a Developer key (v3 auth).

**3. Create a `.env` file** in the project folder with one line (no quotes, no spaces around `=`):
```
TMDB_KEY=your_api_key_here
```

**4. Run the script**
```
python topratedmovies.py
```
Enter a number of pages when asked. Start small (like 5) to test, since each page is a separate request and 500 pages takes several minutes.

## What I learned

- How APIs work: sending a request with `requests` and getting data back as JSON
- Converting JSON into a table with pandas and selecting only the columns I need
- Looping through multiple pages and combining them with `pd.concat`
- Saving the data as a CSV file with `to_csv`
- Keeping my API key safe using a `.env` file and `.gitignore`

## Project files

```
.
├── topratedmovies.py   # main script
├── requirements.txt     # pandas, requests, python-dotenv
├── sample_output.csv    # 50-row example output
├── .gitignore           # ignores .env and toprated.csv
└── README.md
```