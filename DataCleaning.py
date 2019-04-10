import numpy as np
import csv
import os
import pandas as pd
from clean_diandra import CleanData
from MahdiScript import sjoin
from KianaScript import EmployerRangeMapping,StateMapping,MajorMapping, RowMapping


""" reading the data """

path = os.path.join(os.path.dirname(__file__), 'us_perm_visas.txt')

data = open(path, 'rt', encoding='utf-8');
reader = csv.reader(data,delimiter='\t',quoting=csv.QUOTE_NONE)
visa_data = pd.DataFrame(list(reader))

""" run Diandra script to polish the data a little bit"""
visa_data = CleanData(visa_data)


""" Use code in Mahdi script to merge two country of citizenships but first changed the name of the columns"""

visa_data['country_of_citizenship'].fillna(" ", inplace = True)
visa_data.groupby(level=0, axis=1).apply(lambda x: x.apply(sjoin, axis=1))


""" use Kiana Code to do the tasks """

visa_data['employer_size'] = EmployerRangeMapping(visa_data)
visa_data['Center'] = StateMapping(visa_data)
visa_data['Career_Cluster'] = MajorMapping(visa_data)

# replace the maximum wage offer part

#groups = visa_data.groupby(['wage_offer_unit_of_pay_9089'], as_index=False)[['wage_offer_from_9089']].max()

#print(groups)


""" select the target variables and form the final data"""


