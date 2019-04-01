# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:28:42 2019

@author: Diandra
"""

"""---------Import Dependencies---------"""
import numpy as np
import csv
import os
import pandas
pandas.options.mode.use_inf_as_na = True

path = os.path.join(os.path.dirname(__file__), 'us_perm_visas.txt')

data = open(path, 'rt', encoding='utf-8');
reader = csv.reader(data,delimiter='\t',quoting=csv.QUOTE_NONE)
visa_data = pandas.DataFrame(list(reader));

new_header = visa_data.iloc[0] #grab the first row for the header
visa_data = visa_data[1:] #take the data less the header row
visa_data.columns = new_header #set the header row as the df header

#If first column for country_of_citizenship is empty, replace with 
#country from second column for country_of_citzenship 
visa_data['country_of_citizenship'] = np.where(visa_data['country_of_citizenship'] \
         == '',visa_data['country_of_citzenship'],visa_data['country_of_citizenship'])

#If country_of_citizenship is still empty, replace with "Unknown"
visa_data['country_of_citizenship'] = np.where(visa_data['country_of_citizenship'] \
         == '',"Unknown",visa_data['country_of_citizenship'])
