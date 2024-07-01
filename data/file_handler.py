import pandas as pd
import logging
from scraping.utils import logit, timeit

@logit
@timeit
def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    logging.info(f'Datos guardados en {filename}')

@logit
@timeit
def load_from_csv(filename):
    df = pd.read_csv(filename)
    logging.info(f'Datos cargados desde {filename}')
    return df
