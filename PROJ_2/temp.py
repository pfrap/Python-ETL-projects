# Code for ETL operations on Country-GDP data
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import sqlite3 as sql
import numpy as np
from datetime import datetime

# Importing the required libraries

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format='%Y-%h-%d-%H:%M:%S' 
    now=datetime.now()
    timestamp=now.strftime(timestamp_format)
    with open ("log_file.txt","a") as f:
        f.write(f"{timestamp}: {message}\n")

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    http=requests.get(url).text
    data=bs(http, "html.parser")
    table=data.find_all("tbody")[0]
    rows=table.find_all("tr")
    df=pd.DataFrame(columns=table_attribs)
    i=0
    for n in rows: 
        column=n.find_all("td")
        if i>0:
            temp_dict={"Name":column[1].find_all("a")[1].contents[0],"MC_USD_Billion":float(column[2].contents[0])}
            temp_df=pd.DataFrame(temp_dict, index=[0])
            df=pd.concat([df,temp_df],ignore_index=True)
        i+=1
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

#DATI PRELIMINARI
url="https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
Exchange_rate_CSV_path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
Table_Attributes_extraction=["Name", "MC_USD_Billion"]
Table_Attributes=["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
Output_CSV_Path="./Largest_banks_data.csv"
Database_name="Banks.db"
Table_name="Largest_banks"
Log_file="code_log.txt"

extract(url,Table_Attributes_extraction)


