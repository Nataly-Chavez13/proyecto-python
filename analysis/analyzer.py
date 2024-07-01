import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scraping.utils import logit, timeit
import logging

@logit
@timeit
def analyze_data(df):
    if df.empty:
        logging.error('DataFrame vacío. No se puede realizar el análisis.')
        return
    
    # Calcular estadísticas básicas
    author_counts = df['Autor'].value_counts()
    logging.info(f'Cantidad de citas por autor:\n{author_counts}')
    
    # Visualización de la cantidad de citas por autor
    plt.figure(figsize=(12, 6))
    sns.countplot(y='Autor', data=df, order=df['Autor'].value_counts().index)
    plt.title('Cantidad de citas por autor')
    plt.xlabel('Cantidad de citas')
    plt.ylabel('Autor')
    plt.show()
    
    # Análisis de la longitud de las citas
    df['Longitud_Cita'] = df['Cita'].apply(len)
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Longitud_Cita'], bins=20, kde=True)
    plt.title('Distribución de la longitud de las citas')
    plt.xlabel('Longitud de la cita')
    plt.ylabel('Frecuencia')
    plt.show()
