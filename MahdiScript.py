import pandas as pd
#==================================== Merging country of citizenship columns=================================================
Df= pd.read_table("C:/Users/Mahdi Kouretchian/Desktop/applied_multivariable_analysis/project/us_perm_visas.txt")
#==================================== Merging country of citizenship columns=================================================
Df['country_of_citizenship'].fillna(" ", inplace = True)
Df['country'].fillna(" ", inplace = True)
Df['Country_final']=Df['country_of_citizenship'].astype(str)+Df['country'].astype(str)
Df.to_csv("/Users/kianamac/Dropbox (UFL)/courses/Spring 2019/MultivariateDataAnalysis/project/output.csv", index=False)

government and public administration=['government and public administration','foreign service','governance','national security','national','planning','public management','public management and administration','regulation','revenue','taxation','revenue and taxation']
Health Science=['health science','health','biotechnology research','biotechnology','biotechnology research and development','diagnostic services','health information','support services','therapeutic services']
Hospitality and tourism=['hospitality','tourism','hospitality and tourism','loading','recreation','amusements','attraction','recreation, amusements and attractions','restaurants','restaurant','beverage','food','beverage services','travel','travel and tourism']
Human Services=['consumer','consumer services','counseling','mental health','mental health services','early childhood development','childhood development','early childhood development and services','family','community services','family and community services','personal care','personal care services']
Information Technology=['information','information support','information support and services','network','network systems','programming','software development','programming and software development','web','digital communication','web and digital communication']
Law_public_safety=['law','public safety','corrections','correction','correction services','law enforcement','law enforcement services','legal','legal services','security','protective','protective services','security and protective services']
manufacturing=['manufacturing','environmentalassurance','logistics','inventory control','logistics and inventory control','maintenance','installation','repair','production process','production','quality','quality assurance']
marketing=['marketing','marketing communications','marketing management','marketing research','professional sales']
Science_technology=['science','technology','engineering','mathematics']
transportation=['transportation','distribution','mobile equipment','logistics planning','transportation operation','planning','warehousing']