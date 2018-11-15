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

from pandas import read_table, merge, DataFrame
def ch2int(x):
    if '万' in x:
        x = x.strip('万')
        if '.' in x:
            i = x.index('.')
            x = x.replace('.', '')
            for n in range(4 - (len(x) -i)):
                x += '0'
        else:
            x += '0000'
    elif '亿' in x:
        x = x.strip('亿')
        if '.' in x:
            i = x.index('.')
            x = x.replace('.', '')
            for n in range(8 - (len(x) -i)):
                x += '0'
        else:
            x += '00000000'     
    return int(x)
df1 = read_table('service_label_20181114.txt', names=['package', 'cat1', 'cat2', 'name', 'downloads', 'service', 'pv'])
df1['downloads'] = df1['downloads'].apply(ch2int)
sample = df1['pv'].groupby(df1['cat1']).sum()
total = df1['downloads'].groupby(df1['cat1']).sum()

if total.index.tolist() == total.index.tolist():
    df2 = DataFrame({'pv':sample.tolist(), 'downloads':total.tolist()},index=total.index.tolist())
    df2['tgi'] = (df2['pv']/df2['pv'].sum())/(df2['downloads']/df2['downloads'].sum())
    print(df2)
#     df2['pv'].hist()
    df2.to_csv('cathist_1114.txt', sep='\t', header=None)
# print(merge(sample, total, on = 'cat1'))sample.index)
# df1 = df1.downloads.apply(lambda x: x)
# type(df1['downloads'])
