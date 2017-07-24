import pandas as pd
import os
from pprint import *
file_path='/Users/apple/Downloads/CommunityOverview.csv'
df= pd.read_csv(file_path,encoding='utf-8')
df=df.loc[:,['群名','入群人数','退群人数','在线用户数','互动用户数','互动用户率','互动次数']]
# 找到最新群，干掉老的还有记录的宣传群
xc_groups=[df[df['群名'].str.contains("^{}.+优达学城S[1-9]$".format(nd_name))] for nd_name in
['数据分析','前端开发','机器学习','深度学习']]

for groups in xc_groups:
    cohorts=[int(group[-1]) for group in groups.群名]
    latested_cohort=max(cohorts)
    group_name=groups['群名'].values[0][:4]
    for i in range(latested_cohort):
        df=df[~df.群名.str.contains("^{}.+优达学城S{}$".format(group_name,i))]
# 群分类
groups=[df[df['群名'].str.contains(key_word)] for key_word in
[".+优达学城S[1-9]$",'正式学员',"优等生$","Union A","数据分析",'编程入门',"前端开发","机器学习","深度学习",'安卓',
'^数据分析.+优达学城S[1-9]$','^前端开发.+优达学城S[1-9]$','^机器学习.+优达学城S[1-9]$','^深度学习.+优达学城S[1-9]$']]


# 所需数据
for i in groups:
    print(len(i),i['入群人数'].sum(),i['退群人数'].sum(),i['在线用户数'].sum(),i['互动用户数'].sum(),round(i['互动用户率'].mean(),2),i['互动次数'].sum())

# python3 weekly.py | pbcopy- 别名wkl
os.remove(file_path)
