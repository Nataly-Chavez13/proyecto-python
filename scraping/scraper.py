import requests
from bs4 import BeautifulSoup
import pandas as pd
from scraping.utils import logit, timeit

@logit
@timeit
def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        texts = []
        authors = []
        all_tags = []
        
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            
            texts.append(text)
            authors.append(author)
            all_tags.append(", ".join(tags))
        
        return pd.DataFrame({'Cita': texts, 'Autor': authors, 'Tags': all_tags})
    else:
        print(f'Error al realizar la solicitud: {response.status_code}')
        return pd.DataFrame()
