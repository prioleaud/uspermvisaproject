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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

# pandas.options.mode.use_inf_as_na = True

# path = os.path.join(os.path.dirname(__file__), 'us_perm_visas.txt')

# data = open(path, 'rt', encoding='utf-8');
# reader = csv.reader(data,delimiter='\t',quoting=csv.QUOTE_NONE)
# visa_data = pandas.DataFrame(list(reader));
def CleanData(data):
    new_header = visa_data.iloc[0] #grab the first row for the header
    visa_data = visa_data[1:] #take the data less the header row
    visa_data.columns = new_header #set the header row as the df header

    #If first column for country_of_citizenship is empty, replace with 
    #country from second column for country_of_citzenship 
    visa_data['country_of_citizenship'] = np.where(visa_data['country_of_citizenship'] \
             == '',visa_data['country_of_citizenship'],visa_data['country_of_citizenship'])

    #If country_of_citizenship is still empty, replace with "Unknown"
    visa_data['country_of_citizenship'] = np.where(visa_data['country_of_citizenship'] \
             == '',"Unknown",visa_data['country_of_citizenship'])

    #Remove instances if empty:
    visa_data = visa_data[visa_data['case_status'] != '']
    visa_data = visa_data[visa_data['decision_date'] != '']


    #print(visa_data)
    #visa_data =visa_data[(visa_data['foreign_worker_info_education'] != '') & (visa_data['job_info_major'] != '')]

    # print(visa_data)

    #visa_data['wage_offered_from_9089'].to_csv('before.csv',sep=',')

    #visa_data = visa_data[visa_data['job_info_major'] != '']
    visa_data = visa_data[visa_data['job_info_alt_combo_ed'] != '']

    #visa_data['wage_offered_from_9089'].to_csv('after.csv',sep=',')


    # print(visa_data['wage_offer_from_9089'])
    #If column for wage_offer_from_9089 is empty, replace with wage_offered_from_9089 
    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_from_9089'] \
             == '',visa_data['wage_offered_from_9089'],visa_data['wage_offer_from_9089'])
    visa_data['wage_offer_unit_of_pay_9089'] = np.where(visa_data['wage_offer_from_9089'] \
             == '',visa_data['wage_offered_unit_of_pay_9089'],visa_data['wage_offer_unit_of_pay_9089'])


    #print(visa_data['wage_offer_from_9089'])

    #visa_data.to_csv('wage_before.csv',sep=',')

    #remove instances with empty wage offer
    visa_data = visa_data[visa_data['wage_offer_from_9089'] != '']

    #remove instances if wages is not a number
    visa_data = visa_data[visa_data['wage_offer_from_9089'].apply(lambda x: is_number(x) == True)]


    visa_data['wage_offer_from_9089'] = pandas.to_numeric(visa_data['wage_offer_from_9089'], downcast = 'float')



    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'Hour',visa_data['wage_offer_from_9089']*2080, \
             visa_data['wage_offer_from_9089'])

    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'hr',visa_data['wage_offer_from_9089']*2080, \
             visa_data['wage_offer_from_9089'])

    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'Week',visa_data['wage_offer_from_9089']*52, \
             visa_data['wage_offer_from_9089'])

    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'wk',visa_data['wage_offer_from_9089']*52, \
             visa_data['wage_offer_from_9089'])

    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'Bi-Weekly',visa_data['wage_offer_from_9089']*26, \
             visa_data['wage_offer_from_9089'])

    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'bi',visa_data['wage_offer_from_9089']*26, \
             visa_data['wage_offer_from_9089'])

    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'Month',visa_data['wage_offer_from_9089']*12, \
             visa_data['wage_offer_from_9089'])

    visa_data['wage_offer_from_9089'] = np.where(visa_data['wage_offer_unit_of_pay_9089'] \
             == 'mth',visa_data['wage_offer_from_9089']*12, \
             visa_data['wage_offer_from_9089'])

    #visa_data.to_csv('wage_after.csv',sep=',')
    return visa_data
