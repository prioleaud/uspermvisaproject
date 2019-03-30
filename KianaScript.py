#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:44:29 2019

@author: kianamac
"""


import pandas as pd 
import numpy as np

#====================== Reading the Data============================#

Df = pd.read_table('us_perm_visas.txt')

#====================== Task 1====================#
"""according to https://data.oecd.org/entrepreneur/enterprises-by-business-size.htm the 0 to 10 employee is micro size enterprise, 11-49 Smalll, 
50-249 medium, 250-inf large"""
Df.head()
Df.replace('', -1, inplace=True)
Df['employer_num_employees'].fillna(-1, inplace = True)

Df['employer_num_employees'] = Df['employer_num_employees'].astype(int)
Df['employer_size']='Unknown'
bins = [-1,0, 10, 49, 249,np.inf]
names = ['Unknown', 'Micro', 'Small', 'Medium', 'Large']

Df['employer_size'] = pd.cut(Df['employer_num_employees'], bins, labels=names)
Df.to_csv("data.txt", sep='\t')

#=========================== Task 2 =======
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


VT_state_index = Df.loc[Df['employer_state'].isin(Vermont_center_states),'Center'] = 'VT'
VT_visa_index = Df.loc[Df['class_of_admission'].isin(Vermont_center_visa),'Center'] ='VT'

CA_state_index = Df.loc[Df['employer_state'].isin(California_center_states),'Center'] = 'CA'
CA_visa_index = Df.loc[Df['class_of_admission'].isin(California_center_visa),'Center'] = 'CA'
both_visa_index = Df.loc[Df['class_of_admission'].isin(Both_centers_visa),'Center'] ='CA or VT'

#=================================== Task 3=======================