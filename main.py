from scraping.scraper import scrape_quotes
from analysis.analyzer import analyze_data
from data.file_handler import save_to_csv, load_from_csv
import pandas as pd

def main():
    url = 'http://quotes.toscrape.com/page/'
    max_pages = 10  # Máximo de páginas a scrapear

    all_data = []
    for page in range(1, max_pages + 1):
        page_url = f"{url}{page}/"
        df = scrape_quotes(page_url)
        if not df.empty:
            all_data.append(df)

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        save_to_csv(final_df, 'quotes.csv')
        analyze_data(final_df)
    else:
        print("No se encontraron datos.")

if __name__ == "__main__":
    main()
