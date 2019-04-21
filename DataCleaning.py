import numpy as np
import csv
import os
import pandas as pd
from MahdiScript import sjoin
from KianaScript import EmployerRangeMapping,StateMapping,MajorMapping, RowMapping, JobMajorMapping


""" reading the data after Diandra script was ran"""


path = os.path.join(os.path.dirname(__file__), 'clean_data.csv')

visa_data = pd.read_csv(path)

""" use Kiana Code to do the tasks """
print(visa_data.size)
print(visa_data.ndim)
print(visa_data.shape)
visa_data['employer_size'] = EmployerRangeMapping(visa_data)
visa_data['Center'] = StateMapping(visa_data)
visa_data['Applicant Major'] = MajorMapping(visa_data)
visa_data['Career Major'] = JobMajorMapping(visa_data)
print("I am here!")
print(visa_data.size)
print(visa_data.ndim)
print(visa_data.shape)
def ListOfState (c) :
	List_State=['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','MD','ME','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC',
	'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
	if c in List_State:
		pass
	state=c.upper()
	if state=='ALABAMA':
		return 'AL'
	if state=='ALASKA':
		return 'AK'
	if state=='ARIZONA':
		return 'AZ'
	if state=='ARKANSAS':
		return 'AR'
	if state=='CALIFORNIA':
		return 'CA'
	if state=='COLORADO':
		return 'CO'
	if state=='CONNECTICUT':
		return 'CT'
	if state=='DELAWARE':
		return 'DE'
	if state=='FLORIDA':
		return 'FL'
	if state=='GEORGIA':
		return 'GA'
	if state=='HAWAII':
		return 'HI'
	if state=='IDAHO':
		return 'ID'
	if state=='ILLINOIS':
		return 'IL'
	if state=='INDIANA':
		return 'IN'
	if state=='IOWA':
		return 'IA'
	if state=='KANSAS':
		return 'KS'
	if state=='KENTUCKY':
		return 'KY'
	if state=='LOUISIANA':
		return 'LA'
	if state=='MAINE':
		return 'ME'
	if state=='MARYLAND':
		return 'MD'
	if state=='MASSACHUSETTS':
		return 'MA'
	if state=='MICHIGAN':
		return 'MI'
	if state=='MINNESOTA':
		return 'MN'
	if state=='MISSISSIPPI':
		return 'MS'
	if state=='MISSOURI':
		return 'MO'
	if state=='MONTANA':
		return 'MT'
	if state=='NEBRASKA':
		return 'NE'
	if state=='NEVADA':
		return 'NV'
	if state=='NEW HAMPSHIRE':
		return 'NH'
	if state=='NEW JERSEY':
		return 'NJ'
	if state=='NEW MEXICO':
		return 'NM'
	if state=='NEW YORK':
		return 'NY'
	if state=='NORTH CAROLINA':
		return 'NC'
	if state=='NORTH DAKOTA':
		return 'ND'
	if state=='OHIO':
		return 'OH'
	if state=='OKLAHOMA':
		return 'OK'
	if state=='OREGON':
		return 'OR'
	if state=='PENNSYLVANIA':
		return 'PA'
	if state=='RHODE ISLAND':
		return 'RI'
	if state=='SOUTH CAROLINA':
		return 'SC'
	if state=='SOUTH DAKOTA':
		return 'SD'
	if state=='TENNESSEE':
		return 'TN'
	if state=='TEXAS':
		return 'TX'
	if state=='UTAH':
		return 'UT'
	if state=='VERMONT':
		return 'VT'
	if state=='VIRGINIA':
		return 'VG'
	if state=='WASHINGTON':
		return 'WA'
	if state=='WEST VIRGINIA':
		return 'WV'
	if state=='WISCONSIN':
		return 'WI'
	if state=='WYOMING':
		return 'WY'

Df['job_info_work_state'] = Df['job_info_work_state'].apply(ListOfState)
""" select the target variables and form the final data"""

finalData = visa_data[['case_received_date','case_status','country_of_citizenship','decision_date','employer_name','employer_state','employer_yr_estab'
						,'foreign_worker_info_education','job_info_alt_combo_ed',
						'job_info_work_state', 'us_economic_sector','wage_offer_from_9089','wage_offer_unit_of_pay_9089','employer_size','Center','Applicant Major','Career Major']]

finalData.to_csv('Final_data.csv')



