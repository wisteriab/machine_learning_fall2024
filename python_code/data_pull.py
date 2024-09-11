import requests
import re  
import pandas as pd 
url = (
    'https://api.census.gov/data/2023/cps/asec/mar?get='
    'A_LINENO,'
    'A_AGE,'
    'A_DTIND,'
    'A_DTOCC,'
    'A_ENRLW,'
    'A_EXPLF,'
    'A_FAMNUM,'
    'A_FTLF,'
    'A_FTPT,'
    'A_HGA,'
    'A_HSCOL,'
    'A_GRSWK,'
    'A_HRLYWK,'
    'A_HRS1,'
    'A_LFSR,'
    'A_MARITL,'
    'A_MJOCC,'
    'A_SEX,'
    'A_UNCOV,'
    'A_UNMEM,'
    'A_UNTYPE,'
    'A_WKSLK,'
    'A_WKSTAT,'
    'AGE1,'
    'AGI,'
    'CHCARE_YN,'
    'HCHCARE_VAL,'
    'HCHCARE_YN,'
    'COV_CYR,'
    'DEPPRIV,'
    'ESICOULD,'
    'FAMLIS,'
    'FEARNVAL,'
    'FFPOS,'
    'FMED_VAL,'
    'FMOOP,'
    'FOTC_VAL,'
    'FRNTVAL,'
    'GESTFIPS,'
    'GTCBSAST'
    '&for=state:*'
    '&key=b4cdb850b47d0c5c108b69a6d44a5c1c60f98e3b'
)
response = requests.get(url)
result = response.json()
df = pd.DataFrame(result)
df.columns=df.iloc[0] 
df = df.iloc[1:]
df.to_csv("../data/raw_data/census_raw.csv")