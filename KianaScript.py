#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:44:29 2019

@author: kianamac
"""


import pandas as pd 
import numpy as np

#====================== Reading the Data============================

Df = pd.read_table("/Users/kianamac/Dropbox (UFL)/courses/Spring 2019/MultivariateDataAnalysis/project/us_perm_visas.txt")

#====================== Define rnage for employer size====================#
"""according to https://data.oecd.org/entrepreneur/enterprises-by-business-size.htm the 0 to 10 employee is micro size enterprise, 11-49 Smalll, 
50-249 medium, 250-inf large"""

Df.replace('', -1, inplace=True)
Df['employer_num_employees'].fillna(-1, inplace = True)

Df['employer_num_employees'] = Df['employer_num_employees'].astype(int)
Df['employer_size']='Unknown'
bins = [-1,0, 10, 49, 249,np.inf]
names = ['Unknown', 'Micro', 'Small', 'Medium', 'Large']

Df['employer_size'] = pd.cut(Df['employer_num_employees'], bins, labels=names)


#=========================== mapping of applications to centers =======
"""this information has been gathered from this page"""
California_center_states = ['Alaska','Arizona','California','Colorado','Commonwealth of the Northern Mariana Islands',
                    'Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana',
                    'Iowa', 'Kansas','Michigan','Minnesota','Missouri','Montana',
                    'Nebraska','Nevada','North Carolina','North Dakota','Ohio','Oregon',
                    'South Dakota', 'Texas', 'Utah', 'Washington', 'Wisconsin', 'Wyoming']

Vermont_center_states =['Alabama', 'Arknsas', 'Connecticut', 'Delaware', 'District of Columbia',
                        'Kentucky','Louisiana','Maine','Maryland','Massachusetts','Mississippi',
                        'New Hampshire', 'New Jersey', 'New Mexico', 'Oklahoma','Pennsylvania',
                        'Puerto Rico','Rhode Island','South Carolina','Tennessee', 'U.S. Virgin Islands',
                        'Vermont','Virginia','West Virginia']

California_center_visa =['E-1','E-2','L','L-1A', 'L-1B','LZ','R-1' ]

Vermont_center_visa =['P','E-3','P-1A','P-1','TN-1','TN-2']
Both_centers_visa = ['H-1B','H-1B2','H-1B','O-1A', 'O-1B','O-2',
                     'O','P-1B', 'P-1S', 'P-2', 'P-2S',' P-3',
                     'P-3S','Q-1']

Df['Center'] = 'Unknown'


Df.loc[Df['employer_state'].isin(Vermont_center_states),'Center'] = 'VT'
Df.loc[Df['class_of_admission'].isin(Vermont_center_visa),'Center'] ='VT'

Df.loc[Df['employer_state'].isin(California_center_states),'Center'] = 'CA'
Df.loc[Df['class_of_admission'].isin(California_center_visa),'Center'] = 'CA'
Df.loc[Df['class_of_admission'].isin(Both_centers_visa),'Center'] ='CA or VT'

#=================================== Finding max wage offer======================================================
groups = Df.groupby(['wage_offer_unit_of_pay_9089'], as_index=False)[['wage_offer_from_9089']].max()
#Df.loc[Df.groupby('wage_offer_unit_of_pay_9089')['wage_offer_from_9089'].idxmax()]
#Df['wage_max']
#Df.to_csv("/Users/kianamac/Dropbox (UFL)/courses/Spring 2019/MultivariateDataAnalysis/project/output.csv", index=False)

#================================== maping majors into clusters ================================================

Agriculture_careers= ['Agribusiness Systems','Agribusiness','Animal Systems', 'Environmental', 'Agriculture','Food','Natural Resource Systems','Natural resource', 'Food Products','Plant Systems','Power, Structural and Technical Systems','structural system', 'technical system', 'Power Systems'];
Architecture_majors = ['Architecture','Construction','Design','Pre-Construction','Maintenance','Operations','Accoustic'];
Arts_majors =['Arts','A/V technology and Film','Film','Movie','Journalism','Communications','Broadcasting','Performing Arts','Printing Technology','Telecommunications','Media','Visual Arts','Arts'];
Business_majors =['Administrative Support','Business Information Management','General Management','Human Resources Management','Operations Management','Business','Management','Administration',
'Accounting','Advertising','Banking','Business Administration','Business Law', 'Business','commerce',
'Criminal Justice Administration','E-commerce','Economics','Entrepreneurial Studies','Finance',
'Health Care Administration','Hospitality Management','Human Resource Management','Management','International Business',
'Labor Studies','MBA', 'Merchandising and retail','Non-Profit Administration','Operations','Administration',
'Organizational Behaviour','Project Management','Public Administration and Policy','Public administration','Policy','Public Relations','Real Estate','Secretarial Studies',
'taxation','Banking','Business','Business Finance','Insurance','securities and investment','investment','Finance'];
Education_majors =['Education','Training','Teaching','Training','Administration','Administrative','Professional Support Services','Child development','Child studies','Elementary education','Secondary Education','Special education']
Science_majors =['Agronomy and Crop Science','Animal Sciences','Astronomy','Agronomy and Crop Scienc','Atmospheric Sciences and Meteorology',
'Biochemistry and Biophysics','Biology','Cellular Biology','Chemistry','Ecology','Environmental Science','Food Sciences and Technology','Forestry','Genetics',
'Geological and Earth Sciences','Horticulture Science','Marine/Aquatic Biology','Microbiology and Immunology','Natural Resources Conservation',
'Natural Resources Management', 'Physical Sciences','Physics','Science Education','Wildlife and Wildlands Management','Zoology','life Science_majors']

csMath_majors =['Actuarial Science','Applied Mathematics',
'Business/Management Quantitative Methods','Quantitative','Quantitative Analyst',
'Computer and Information Sciences', 'Computer Network','software','computer','Data base','Data Science','cyber-security','cyber',
'Computer Science','Programming','Computer Software','Media Application',
'Computer System Administration','Data Management Technology',
'Information Science', 'Management Information Systems','IT','Information Technology',
'Mathematics Education','Mathematics','Statistics','Webpage Design','Statistics']

Medical_majors =['Athletic Training','Chiropractic', 'Dentistry',
'Emergency Medical Technology','Food and Nutrition','Health/Medical Technology',
'Medical Laboratory Technology','Medical Radiologic Technology',
'Medicine','Nuclear Medicine Technology','Nursing, Practical/Vocational (LPN)',
'Nursing, Registered (BS/RN)','Optometry (Pre-Optometry)','Osteopathic Medicine',
'Pharmacy (Pre-Pharmacy)','Physical Therapy (Pre-Physical Therapy)',
'Physician Assisting','Respiratory Therapy Technology','Surgical Technology',
'Veterinarian Assisting/Technology','Veterinary Medicine (Pre-Vet)']
Eng_majors = ['Aerospace Engineering','Aerospace/Aeronautical Engineering',
'Agricultural/Bioengineering','Architectural Drafting/CAD Technology','Architectural Engineering',
'Architectural Engineering Technology','Architecture, General','Automotive Engineering Technology',
'Biomedical Engineering','Chemical Engineering','Civil Engineering','Civil Engineering Technology',
'Computer Engineering','Computer Engineering Technology','Construction Engineering','Construction Management',
'Construction technology', 'Building Technology','Drafting Technology','CAD technology','Electrical, Electronic, and Communication Engineering',
'Electrical/Electronics Engineering Technology','Electromechanical/Biomedical Engineering Technology',
'Engineering','Engineering Technology','Environmental Control Technologies','Environmental Health Engineering',
'Industrial Engineering','Industrial Production Technologies','Mechanical Drafting/CAD Technology','Mechanical Engineering','Mechanical Engineering Technology','Military Technologies',
'Nuclear Engineering','Quality Control and Safety Technologies','Surveying Technology']




Df['Career_Cluster'] = 'Unknown'

Agriculture_careers = [x.upper() for x in Agriculture_careers]
Architecture_majors = [x.upper() for x in Architecture_majors]
Arts_majors = [x.upper() for x in Arts_majors]
Business_majors = [x.upper() for x in Business_majors]
Education_majors = [x.upper() for x in Education_majors]
Science_majors = [x.upper() for x in Science_majors]
csMath_majors = [x.upper() for x in csMath_majors]
Medical_majors = [x.upper() for x in Medical_majors]
Eng_majors = [x.upper() for x in Eng_majors]

Df.loc[Df['foreign_worker_info_major'].isin(Agriculture_careers), 'Career_Cluster'] = 'Agriculture'
Df.loc[Df['foreign_worker_info_major'].isin(Architecture_majors), 'Career_Cluster'] = 'Architecture and Construction'
Df.loc[Df['foreign_worker_info_major'].isin(Arts_majors), 'Career_Cluster'] = 'Arts'
Df.loc[Df['foreign_worker_info_major'].isin(Business_majors), 'Career_Cluster'] = 'Business Management'
Df.loc[Df['foreign_worker_info_major'].isin(Education_majors), 'Career_Cluster'] = 'Education'
Df.loc[Df['foreign_worker_info_major'].isin(csMath_majors), 'Career_Cluster'] = 'Computer Science and Math'
Df.loc[Df['foreign_worker_info_major'].isin(Science_majors), 'Career_Cluster'] = 'Science'
Df.loc[Df['foreign_worker_info_major'].isin(Medical_majors), 'Career_Cluster'] = 'Medical Sciences'
Df.loc[Df['foreign_worker_info_major'].isin(Eng_majors), 'Career_Cluster'] = 'Engineering'


clusters = Df.Career_Cluster.unique()
majors = Df.foreign_worker_info_major.unique()
np.savetxt('clusters_unique.txt',clusters,fmt='%5s',delimiter=',')
np.savetxt('majors_unique.txt',majors,fmt='%5s',delimiter=',')
#np.savetxt("majors_unique.csv", majors, delimiter=",")
Df_limited = Df[['foreign_worker_info_major', 'Career_Cluster']] 
Df_limited.to_csv("/Users/kianamac/Dropbox (UFL)/courses/Spring 2019/MultivariateDataAnalysis/project/df_limited.csv", index=False)



#==========