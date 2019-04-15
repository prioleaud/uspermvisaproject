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
print(visa_data.size)
print(visa_data.ndim)
print(visa_data.shape)
visa_data['employer_size'] = EmployerRangeMapping(visa_data)
visa_data['Center'] = StateMapping(visa_data)
visa_data['Career_Cluster'] = MajorMapping(visa_data)
print(visa_data.size)
print(visa_data.ndim)
print(visa_data.shape)


""" select the target variables and form the final data"""

finalData = visa_data[['case_received_date','case_status','country_of_citizenship','decision_date','employer_state','employer_name','employer_yr_estab'
						,'foreign_worker_info_birth_country','foreign_worker_info_education','job_info_alt_combo_ed', 'job_info_alt_occ_job_title', 'job_info_job_title',
						'job_info_work_state','wage_offer_from_9089','wage_offer_unit_of_pay_9089','employer_size','Center','Career_Cluster' ]]

finalData.to_csv('Final_data.csv')