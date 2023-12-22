#EXTRACT
def extract_from_csv(file_to_process): 
    """Funzione che elabora un singolo file CSV e 
    restituisce un dataframe."""
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

def extract(folder): 
    """Funzione che cicla su file CSV multipli in 
    una cartella e restituisce un dataframe unico."""
    extracted_data = pd.DataFrame(columns=['name','height','weight'])
    for csvfile in glob.glob(folder+"*.csv"):
        extracted_data = pd.concat([extracted_data, 
                                    pd.DataFrame(extract_from_csv(csvfile))], 
                                    ignore_index=True) 
    return extracted_data 

#TRANSFORM
def transform(data): 
    """Trasformazione delle informazioni: modifica al 
    dataframe, unità di misura e arrotondamento."""
    data['height'] = round(data.height * 0.0254,2) 
    data['weight'] = round(data.weight * 0.45359237,2) 
    return data 

#LOAD
def load_data(target_file, transformed_data): 
    """Funzione per caricare dati su file csv."""
    transformed_data.to_csv(target_file) 

def log_progress(message): 
    """Funzione che scrive un file di log."""
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

#SEQUENZA       
import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
source_files_folder="./source/"
target_file = "transformed_data.csv" 

# 1_EXTRACTION
log_progress("ETL Job Started") 
log_progress("Extract phase Started") 
extracted_data = extract(source_files_folder) 
log_progress("Extract phase Ended") 

# 2_TRANSFORMATION
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
log_progress("Transform phase Ended") 

# 3_LOAD
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
log_progress("Load phase Ended") 
log_progress("ETL Job Ended") 

