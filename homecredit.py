import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
df = pd.read_csv('d:/student/application_train.csv',nrows = 10000)
#SR_y = pd.Series(df['TARGET'], name="y_ (Target Vector Distribution)")
fig, ax = plt.subplots()
sns.distplot(df['TOT_INCOME'], bins=25, color="g", ax=ax)
plt.show()
#print(df[df['TARGET'] == 0].groupby(['GENDER','OWN_CAR']).groups['F','Y'])
#print(df[df['TARGET'] == 0].groupby(['GENDER','OWN_CAR']).groups['F','N'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','OWN_CAR']).groups['F','Y'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','OWN_CAR']).groups['F','N'])
#print(df[df['OWN_CAR']== 'Y'  ].groupby(['GENDER']).groups['F','y'])
#print(df[df['TARGET'] == 0].groupby(['GENDER','OWN_CAR']).groups['M','Y'])
#print(df[df['TARGET'] == 0].groupby(['GENDER','OWN_CAR']).groups['M','N'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','OWN_CAR']).groups['M','Y'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','OWN_CAR']).groups['M','N'])

# trying to see if for females who has repayed the loan how many have owns  a
# house or a flat
#print(df[df['TARGET'] == 0].groupby(['GENDER','OWN_REALTY']).groups['F','Y'])
#print(df[df['TARGET'] == 0].groupby(['GENDER','OWN_REALTY']).groups['F','N'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','OWN_REALTY']).groups['F','Y'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','OWN_REALTY']).groups['F','N'])

# trying to see if for females who have repayed the loan how many have taken cash
#loan
#print(df[df['TARGET'] == 0].groupby(['GENDER','LOAN_TYPE']).groups['F','CL'])
#print(df[df['TARGET'] == 0].groupby(['GENDER','LOAN_TYPE']).groups['F','RL'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','LOAN_TYPE']).groups['F','CL'])
#print(df[df['TARGET'] == 1].groupby(['GENDER','LOAN_TYPE']).groups['F','RL'])
print(df[df['TARGET'] == 0].groupby(['GENDER','LOAN_TYPE']).groups['M','CL'])
print(df[df['TARGET'] == 0].groupby(['GENDER','LOAN_TYPE']).groups['M','RL'])
print(df[df['TARGET'] == 1].groupby(['GENDER','LOAN_TYPE']).groups['M','CL'])
print(df[df['TARGET'] == 1].groupby(['GENDER','LOAN_TYPE']).groups['M','RL'])
print(df[df['TARGET'] == 0].groupby(['TOT_INCOME']))
