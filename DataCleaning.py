import numpy as np
import csv
import os
import pandas as pd
from MahdiScript import sjoin
from KianaScript import EmployerRangeMapping,StateMapping,MajorMapping, RowMapping


""" reading the data after Diandra script was ran"""


path = os.path.join(os.path.dirname(__file__), 'clean_data.csv')

visa_data = pd.read_csv(path)



""" use Kiana Code to do the tasks """

visa_data['employer_size'] = EmployerRangeMapping(visa_data)
visa_data['Center'] = StateMapping(visa_data)
visa_data['Career_Cluster'] = MajorMapping(visa_data)

# replace the maximum wage offer part
#groups = visa_data.groupby(['wage_offer_unit_of_pay_9089'], as_index=False)[['wage_offer_from_9089']].max()
# groups = visa_data.groupby('wage_offer_unit_of_pay_9089').wage_offer_from_9089.max()



# print(groups)


""" select the target variables and form the final data"""


