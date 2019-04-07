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

Agriculture_careers= ['agribusiness systems','agribusiness','animal systems', 'environmental', 'agriculture','food','natural resource systems','natural resource', 'food products','plant systems','power', 'structural and technical systems','structural system', 'technical system', 'power systems'];
Architecture_majors = ['architecture','mechanical construction', 'construction','design','pre-construction','maintenance','operations','accoustic'];
Arts_majors =['arts','A/V technology and film','film','movie','journalism','communications','broadcasting','performing arts','printing technology','telecommunications','liberal arts', 'media','visual arts','arts', 'media studies','drama and cinema'];
Business_majors =['administrative support','business information management','general management','human Resources Management','Operations Management','Business','Management','Administration','ACCOUNTANCY, TAXATION',
'Accounting','Advertising','Banking','Business Administration','Business Law', 'Business','commerce','buiness administration','financial engineering','finance and marketing','financial management','ACCOUNTING & BUSINESS ADMINISTRATION',
'Criminal Justice Administration','E-commerce','Economics','Entrepreneurial Studies','Finance','business information technology','agricultural economics','accountancy','ACCOUNTANCY & FINANCE','ACCOUNTANCY/COMMERCE','ACCOUNTING & AUDITING',
'Health Care Administration','Hospitality Management','Human Resource Management','Management','International Business','business administration (financial management/investment management)','teaching science and technology','teaching english language and literature',
'Labor Studies','MBA', 'Merchandising and retail','Non-Profit Administration','Operations','Administration','business administration (information technology)','ACCOUNTANCY AND BUSINESS ADMINISTRATION','ACCOUNTING / FINANCE','ACCOUNTING AND FINANCIAL MANAGEMENT'
'Organizational Behaviour','Project Management','Public Administration and Policy','Public administration','licentiate in public accounting','personnel management','ACCOUNTANT','ACCOUNTING','ACCOUNTANCY AND BUSINESS ADMINISTRATION','ACCOUNTING AND BUSINESS MANAGEMENT','ACCOUNTING AND COMMERCIAL BUSINESS','ACCOUNTING AND COMPUTER INFORMATION SYSTEM',
'Policy','Public Relations','Real Estate','Secretarial Studies','accounting and finance','management & management information systems','information systems','business administration and information systems','ACCOUNTING AND FINANCIAL ECONOMICS',
'taxation','Banking','Business','Business Finance','Insurance','london chamber of commerce private secretary certificate','business economics','ACCOUNTANCY & CONTROLLING','ACCOUNTANCY AND INCOME TAX','ACCOUNTING & FINANCE','ACCOUNTING AND AUDITING','ACCOUNTING AND BUSINESS','ACCOUNTING AND BUSINESS ADMINISTRATION','ACCOUNTING AND BUSINESS LAW','ACCOUNTING AND CONTROLLING','ACCOUNTING AND ECONOMICS',''
'securities and investment','investment','Finance','government and public administration','foreign service','bus. admin with concentration in finance','communication and information studies','ACCOUNTING & ECONOMICS',
'governance','national security','national','planning','public management','public management and administration','international management','ACCOUNTANCY AND INFORMATION SYSTEMS','ACCOUNTANCY AND LAW','ACCOUNTANCY AND TAX SPECIALIZATION','ACCOUNTANCY WITH CONCENTRATION IN TAXATION','ACCOUNTING & LEGAL STUDIES','ACCOUNTING & MANAGEMENT & MBA','ACCOUNTING & MARKETING','ACCOUNTING & MATH','ACCOUNTING & TAXATION',
'regulation','revenue','taxation','revenue and taxation','marketing','marketing communications','marketing management','business administration degree with major in accounting','english and international relations',
'marketing research','professional sales','business/management engineering/accounting and finance','business administration (indian master\'s degree)','business administration and information technology','ACCOUNTING & INFORMATION MANAGEMENT','ACCOUNTING & INFORMATION SYSTEMS','ACCOUNTING & INFORMATION TECHNOLOGY',];


Education_majors =['Education','Training','Teaching','Training','Administration','Administrative','chinese','teaching mathematics','school building leader','instructional technology',
'Professional Support Services','Child development','Child studies','Elementary education','general education','translation (german, english)','education/language and literature','teaching literacy','teaching special education','general/special education','math education',
'Secondary Education','Special education','english','spanish','history and geography','english literature','bible teaching and bible training','computational chemistry','middle childhood mathematics','teaching math']



Science_majors =['Agronomy and Crop Science','Animal Sciences','Astronomy','Agronomy and Crop Scienc',
'Atmospheric Sciences and Meteorology','science (microbiology)','political science',
'Biochemistry and Biophysics','Biology','Cellular Biology','Chemistry','Ecology','Environmental Science','science',
'Food Sciences and Technology','Forestry','Genetics','library science',
'Geological and Earth Sciences','Horticulture Science','Marine/Aquatic Biology','Microbiology and Immunology','natural science','general science',
'Natural Resources Conservation', 'molecular biology','chemistry and biology','chemisty, with emphasis in organic chemistry',
'Natural Resources Management', 'Physical Sciences','Physics','Science Education','Wildlife and Wildlands Management','Zoology','life Science_majors']


csMath_majors =['Actuarial Science','Applied Mathematics',
'Business/Management Quantitative Methods','Quantitative','Quantitative Analyst','compuer science',
'Computer and Information Sciences', 'Computer Network','software','computer','Data base','masters in information of systems','math & physics',
'Data Science','cyber-security','cyber','Computer Science','Programming','Computer Software','computer science and mathematics','computer science engineering',
'Media Application','Computer System Administration','Data Management Technology', 'Network','computer science & engineering',
'Software development','computer science and technology','computer science & systems engineering','software engineering','master of computer applications','computer applications (computer science)','computer information systems',
'Information Science', 'Management Information Systems','IT','Information Technology', 'artificial intelligence (computer science related)','technology, computer science','information science (computer science)','software systems',
'Mathematics Education','Mathematics','Statistics','Webpage Design','Statistics','information','science (computer information systems)', 'system analysis and design, unix, oracle, digital etc',
'information support','information support and services','network','network systems','programming','computer applications (3 year degree)','computer - decision & system sciences',
'software development','programming and software development','web','digital communication','science (information technology & multimedia studies)','information science','computer application',
'web and digital communication', 'computer and information science', 'science (information technology)','computer applications','information systems','information systems management (mism)','information systems management','computers & information technology']


Health_sciences =['Athletic Training','Chiropractic', 'Dentistry',
'Emergency Medical Technology','Food and Nutrition','Health/Medical Technology','psychology',
'Medical Laboratory Technology','Medical Radiologic Technology','medical technology','physical education','physical therapy',
'Medicine','Nuclear Medicine Technology','Nursing, Practical/Vocational (LPN)','pharmacy','bachelor of science in nursing','clinical psychology',
'Nursing, Registered (BS/RN)','Optometry (Pre-Optometry)','Osteopathic Medicine','speech pathology','food science & nutrition',
'Pharmacy (Pre-Pharmacy)','Physical Therapy (Pre-Physical Therapy)', 'physiology', 'science (life science)', 
'Physician Assisting','Respiratory Therapy Technology','Surgical Technology','comparative and experimental medicine','speech language pathology',
'Veterinarian Assisting/Technology','Veterinary Medicine (Pre-Vet)','health science','health','biotechnology research','biotechnology','biotechnology research and development','diagnostic services','health information','support services','therapeutic services']


Eng_majors = ['Aerospace Engineering', 'electrical engineering','Aerospace/Aeronautical Engineering','Engineering','bio-aeronautics','aeronautical science','biological systems engineering (food process engineering)','electrical and computer engineering','elecronics and communication engineering',
'Agricultural/Bioengineering','Architectural Drafting/CAD Technology','Architectural Engineering','electronic engineering and computer engineering','electrical and mechanical engineering','electronics and electrical engineering','mechannical engineering','mechanical','electronic engineering'
'Architectural Engineering Technology','Architecture, General','Automotive Engineering Technology','engineering in electronics and communication','electronics and communication engineering', 'petroleum engineering','electronic engineering','electrical & electronics','telecommunication engineering',
'Biomedical Engineering','Chemical Engineering','Civil Engineering','Civil Engineering Technology','electrotechnology', 'computer science and engineering','instrumentation engineering','electronics and telecommunication engineering', 'electrical and electronics engineering','electronics and telecommunications engineering',
'Computer Engineering','Computer Engineering Technology','Construction Engineering','Construction Management','mechancial engineering','information and automation engineering','metallurgical engineering', 'management science and engineering','electronic engineering','electrical and electronic engineering',
'Construction technology', 'Building Technology','Drafting Technology','CAD technology','Electrical, Electronic, and Communication Engineering','industrial engineering with a focus on supply chain','electric engineering','electronics and communication','electronic and communication',
'Electrical/Electronics Engineering Technology','Electromechanical/Biomedical Engineering Technology','wireless communications','electrical systems','electricity','instrumentation and control engineering','earthquake engineering (structural dynamics)','electronics and communications',
'Engineering','Engineering Technology','Environmental Control Technologies','Environmental Health Engineering','bachelor of science (mechanical)','bachelor of science in chemical engineering','electricall and electronic engineering','electronics','electronics and instrumentation engineering',
'Industrial Engineering','Industrial Production Technologies','agricultural engineering','mechanical Drafting/CAD Technology','Mechanical Engineering','Mechanical Engineering Technology','Military Technologies','production engineering','electrical branch','instrumentation and control',
'Nuclear Engineering','materials science & engineering', 'mechanical and electronic engineering technology', 'Quality Control and Safety Technologies','Surveying Technology', 'electronics engineering', 'engineering (computer)','engineering (electronic)']

Hospitality=['hotel management','urban & multicultural education', 'hospitality','tourism','hospitality and tourism','loading','recreation','amusements','attraction','recreation, amusements and attractions','restaurants','restaurant','beverage','food','beverage services','travel','travel and tourism']

Human_Services=['consumer','consumer services','human kinetics', 'counseling','mental health','rehabilitation counseling', 'mental health services','early childhood development','childhood development','educational psychology  (see section h.14)','early childhood development and services','family','community services','family and community services','personal care','personal care services']

Law_public_safety=['law','public safety','corrections','correction','correction services','law enforcement','law enforcement services','legal','legal services','security','protective','protective services','security and protective services']

manufacturing=['manufacturing','maintenance and automatisms technician','environmentalassurance','logistics','inventory control','hazardous wastecontrol','logistics and inventory control','maintenance','installation','repair','production process','production','quality','quality assurance']

transportation=['transportation','distribution','mobile equipment','logistics planning','transportation operation','planning','warehousing']

#lowercase_data = [v.lower() for v in data]
Agriculture_careers = [v.lower() for v in Agriculture_careers]
Architecture_majors = [v.lower() for v in Architecture_majors]
Arts_majors = [v.lower() for v in Arts_majors]
Business_majors = [v.lower() for v in Business_majors]
Education_majors = [v.lower() for v in Education_majors]
Science_majors = [v.lower() for v in Science_majors]
csMath_majors = [v.lower() for v in csMath_majors]
Health_sciences = [v.lower() for v in Health_sciences]
Eng_majors = [v.lower() for v in Eng_majors]
Hospitality = [v.lower() for v in Hospitality]
Human_Services = [v.lower() for v in Human_Services]
Law_public_safety = [v.lower() for v in Law_public_safety]
manufacturing = [v.lower() for v in manufacturing]
transportation = [v.lower() for v in transportation]

Df['foreign_worker_info_major'].dropna(inplace = True)
Df['Career_Cluster'] = 'Unknown'
#data["Team"]= data["Team"].str.split("t", n = 1, expand = True) 
Df['foreign_worker_info_major'] =Df['foreign_worker_info_major'].str.lower()


# for w in Agriculture_careers:
# 	if w in  Df['foreign_worker_info_major']:
# 		Df.loc[Df['foreign_worker_info_major'], 'Career_Cluster'] = 'Agriculture'

Df.loc[Df['foreign_worker_info_major'].isin(Agriculture_careers), 'Career_Cluster'] = 'Agriculture'
Df.loc[Df['foreign_worker_info_major'].isin(Architecture_majors), 'Career_Cluster'] = 'Architecture and Construction'
Df.loc[Df['foreign_worker_info_major'].isin(Arts_majors), 'Career_Cluster'] = 'Arts'
Df.loc[Df['foreign_worker_info_major'].isin(Business_majors), 'Career_Cluster'] = 'Business Management'
Df.loc[Df['foreign_worker_info_major'].isin(Education_majors), 'Career_Cluster'] = 'Education'
Df.loc[Df['foreign_worker_info_major'].isin(csMath_majors), 'Career_Cluster'] = 'Computer Science and Math'
Df.loc[Df['foreign_worker_info_major'].isin(Science_majors), 'Career_Cluster'] = 'Science'
Df.loc[Df['foreign_worker_info_major'].isin(Health_sciences), 'Career_Cluster'] = 'Health sciences'
Df.loc[Df['foreign_worker_info_major'].isin(Eng_majors), 'Career_Cluster'] = 'Engineering'
Df.loc[Df['foreign_worker_info_major'].isin(Hospitality), 'Career_Cluster'] = 'Hospitality'
Df.loc[Df['foreign_worker_info_major'].isin(Human_Services), 'Career_Cluster'] = 'Human Services'
Df.loc[Df['foreign_worker_info_major'].isin(Law_public_safety), 'Career_Cluster'] = 'Law and public safety'
Df.loc[Df['foreign_worker_info_major'].isin(manufacturing), 'Career_Cluster'] = 'manufacturing'
Df.loc[Df['foreign_worker_info_major'].isin(transportation), 'Career_Cluster'] = 'transportation'

# clusters = Df.Career_Cluster.unique()
# majors = Df.foreign_worker_info_major.unique()
# np.savetxt('clusters_unique.txt',clusters,fmt='%5s',delimiter=',')
# np.savetxt('majors_unique.txt',majors,fmt='%5s',delimiter=',')
# #np.savetxt("majors_unique.csv", majors, delimiter=",")
# Df_limited = Df[['foreign_worker_info_major', 'Career_Cluster']] 

Df[['foreign_worker_info_major','Career_Cluster']].to_csv("/Users/kianamac/Dropbox (UFL)/courses/Spring 2019/MultivariateDataAnalysis/project/df_limited.csv", index=False)
#Df[['foreign_worker_info_major','Career_Cluster']].to_csv("/Users/kianamac/Dropbox (UFL)/courses/Spring 2019/MultivariateDataAnalysis/project/df_limited.csv", index=False)
