import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
from c_bls_data_api import c_bls_data_api

load_dotenv('.env')
KEY = os.environ.get('registrationkey')



# Call c_bls_data_api.py with a request for CPI data from 2002 through 2021
# and the name of the file to store the returned JSON data structure in.

print("Program started.")

# Set the register, series ID for CPI, start year, end year, and calculations. Note that setting calculations to true
# returns CPI percentages as well as the raw CPI.

parameters = json.dumps({"registrationkey":KEY, "seriesid":['CUUR0000SA0'], "startyear":"2002", "endyear":"2021", "calculations":"true"})

# Call the bls data api class with the parameters and the name of the data output file.
c_bls_data_api(parameters, 'cpi_data_report.json')

print("Program completed")





# example 2 https://towardsdatascience.com/acquire-and-analyze-inflation-data-in-the-us-with-an-api-python-and-tableau-ae81944bcbb0
