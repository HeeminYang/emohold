import pandas as pd
import numpy as np

import os
from collections import Counter

dir_list = os.listdir('/home/projects/Metaverse2021/Seg_5sec_Edu/')

theshold = 0.275

total_result = []

for file in dir_list:
    df = pd.read_csv('/home/projects/Metaverse2021/Seg_5sec_Edu/'+file)

    l1 = df['total_count'].tolist()
    l2 = df['emotion'].tolist()
    df1 = pd.DataFrame([l1,l2]).T
    df1['index'] = df1[0]
    a = list(range(1, l1[-1]+1))
    index_df = pd.DataFrame(a, columns=['index'])
    df2 = pd.merge(index_df, df1, how="outer", on='index')
    df2 = df2.fillna('none')
    emolist = df2[1].to_list()
    emocount = Counter(emolist)
    top3 = emocount.most_common(n=3)
    l3 = []

    total_len = len(l1)
    p10_len = int(total_len * theshold)

    if top3[0][0] == 'none':
        if len(top3) == 1:
            l3.append('Neutral')
        elif top3[1][0] == 'Neutral':
            if len(top3) == 3:
                if top3[2][1] >= p10_len:
                    l3.append(top3[2][0])
                else:
                    l3.append(top3[1][0])
            else:
                l3.append(top3[1][0])
        else:
            l3.append(top3[1][0])
    elif top3[0][0] == 'Neutral':
        if len(top3) == 1:
            l3.append('Neutral')
        elif top3[1][0] == 'none':
            if len(top3) == 2: 
                l3.append('Neutral')
            else:
                if top3[2][1] >= p10_len:
                    l3.append(top3[2][0])
                else:
                    l3.append(top3[0][0])
        else:
            if top3[1][1] >= p10_len:
                l3.append(top3[1][0])
            else:
                l3.append(top3[0][0])
    else:
        l3.append(top3[0][0])
    
    total_result.append([file, l3[0]])
tt = pd.DataFrame(total_result, columns=['file', 'emotion'])
tt.to_csv('./result.csv')
