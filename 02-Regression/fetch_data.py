# Small code to fetch and save the data locally
import pandas as pd


def fetch_save_csv(url, path):
    df = pd.read_csv(url)
    df.to_csv(path, index=False)
    return None


url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
path = '/home/nyangweso/Desktop/Ds_1/ML-Zoomcamp/02-Regression/car_price_data.csv'
fetch_save_csv(url, path)
