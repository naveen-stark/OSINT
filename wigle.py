import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from pandas.io.json import json_normalize
import geoplotlib as gp
import warnings
import os
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    warnings.simplefilter(action='ignore', category=FutureWarning)
    wigle_username = 'AIDa61f8c163a1bfd0fb1f21b672beaf3a1'
    wigle_password = '16cc2ad0adbc009fc994cf2e94008421'
    loc=input("Enter Location : ") 
    payload = {'first': '0', 'freenet': 'false', 'paynet': 'false', 'addresscode': loc, 'api_key': (wigle_username + wigle_password).encode()}
    loc_details = requests.get(url='https://api.wigle.net/api/v2/network/geocode', params=payload, auth=HTTPBasicAuth(wigle_username, wigle_password)).json()
    #print(loc_details)
    b_box = loc_details['results'][0]['boundingbox']
    payload = {'latrange1':b_box[0], 'latrange2':b_box[1], 'longrange1':b_box[2], 'longrange2':b_box[3], 'api_key': (wigle_username + wigle_password).encode()}
    results = requests.get(url='https://api.wigle.net/api/v2/network/search', params=payload, auth=HTTPBasicAuth(wigle_username, wigle_password)).json()
    df = json_normalize(results['results'])
    df = df.rename(columns={'trilat': 'lat', 'trilong': 'lon'})
    cols = list(df.columns)
    df.to_csv(dir_path + r'\Wingle_'+loc+'.csv')
    print("The information stored as .csv file")
    # PREVIEWING AVAILABLE INFORMATION:
    #print(f"Result obtained has {df.shape[0]} rows and {df.shape[1]} columns in it. \n\nThe list of columns include {cols}")
    #print(df)

if __name__ == "__main__":
    main()
