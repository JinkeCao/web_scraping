from pandas import read_table
df1 = read_table('20181117_service.txt', names=['service','pv'])
df1['service'] = df1.service.apply(lambda x: '.'.join(x.split('.')[0:2]))
print(df1.shape)
print(df1.pv.sum())
# sr1 = df1['pv'].groupby(df1['service']).sum()
sr1 = df1.groupby(['service']).sum()
sr1.sort_values(by='pv', ascending=False, inplace=True)
print(sr1.head(20))
# sr1 = sr1[sr1['pv']>99]
# sr1.to_csv('level2_origin.txt', sep='\t', header=False)
# print(type(sr1),sr1.shape, sr1.head())
