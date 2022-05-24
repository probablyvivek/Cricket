import pandas as pd
import numpy as np
from cricscraper.cricsheet import CricSheet
import os
pd.set_option('display.max_columns', None)


#read all the yaml files in the folder
os.getcwd()

#read all the files
data = []
for file in os.listdir(os.getcwd()+"/Python/Cricket/ipl/"):
    if file.endswith(".yaml"):
        data.append(file)

#save the data
sheets = CricSheet(files=[os.getcwd()+"/Python/Cricket/ipl/"+file for file in data])

sheets.save(os.getcwd()+"/Python/Cricket/ipl/ipldata.csv")
