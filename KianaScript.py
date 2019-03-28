#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:44:29 2019

@author: kianamac
"""


import pandas as pd 
import numpy as np

#====================== Reading the Data============================#

Df = pd.read_table('new_data.txt')

#====================== Categorize employer size====================#
"""according to https://data.oecd.org/entrepreneur/enterprises-by-business-size.htm the 0 to 10 employee is micro size enterprise, 11-49 Smalll, 
50-249 medium, 250-inf large"""
Df.head()
Df.replace('', -1, inplace=True)
Df['employer_num_employees'].fillna(-1, inplace = True)

Df['employer_num_employees'] = Df['employer_num_employees'].astype(int)

#if(Df['employer_num_employees'] >0 and Df['employer_num_employees'] <50):
#    Df['employer_num_employees'] = 'Small'
#elif(Df['employer_num_employees'] >50 and Df['employer_num_employees'] <300):
#    Df['employer_num_employees'] = 'Medium'
#else:
#    Df['employer_num_employees'] = 'Large'
bins = [-1,0, 10, 49, 249,np.inf]
names = ['Unknown', 'Micro', 'Small', 'Medium', 'Large']

Df['employer_num_employees'] = pd.cut(Df['employer_num_employees'], bins, labels=names)
Df.to_csv("data.txt", sep='\t')




#=========================== mapping states into the office locations=======
"""this information has been gathered from this page"""
Californa_center_states = ['Alaska','Arizona','California','Colorado','Commonwealth of the Northern Mariana Islands',
                    'Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana',
                    'Iowa', 'Kansas','Michigan','Minnesota','Missouri','Montana',
                    'Nebraska','Nevada','North Carolina','North Dakota','Ohio','Oregon',
                    'South Dakota', 'Texas', 'Utah', 'Washington', 'Wisconsin', 'Wyoming']

Vermont_center_states =['Alabama', 'Arknsas', 'Connecticut', 'Delaware', 'District of Columbia',
                        'Kentucky','Louisiana','Maine','Maryland','Massachusetts','Mississippi',
                        'New Hampshire', 'New Jersey', 'New Mexico', 'Oklahoma','Pennsylvania',
                        'Puerto Rico','Rhode Island','South Carolina','Tennessee', 'U.S. Virgin Islands',
                        'Vermont','Virginia','West Virginia']

california_centers_visa =['E-1','E-2','L','L-1A', 'L-1B','LZ','R-1' ]

Vermont_centers_visa =['P','E-3','P-1A','P-1','TN-1','TN-2']
Both_centers_visa = ['H-1B','H-1B2','H-1B','O-1A', 'O-1B','O-2',
                     'O','P-1B', 'P-1S', 'P-2', 'P-2S',' P-3',
                     'P-3S','Q-1']


