#==================================== Merging country of citizenship columns=================================================
Df['country_of_citizenship'].fillna(" ", inplace = True)
Df['country'].fillna(" ", inplace = True)
Df['Country_final']=Df['country_of_citizenship'].astype(str)+Df['country'].astype(str)
Df.to_csv("/Users/kianamac/Dropbox (UFL)/courses/Spring 2019/MultivariateDataAnalysis/project/output.csv", index=False)

