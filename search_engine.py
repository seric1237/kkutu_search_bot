import pandas as pd
import numpy as np
Location = 'C:\kkutu'
ao = 'wordlist.xlsx'
column = 0

data_pd = pd.read_excel('{}/{}'.format(Location, ao), header=None, index_col=None, names=None)
data_np = pd.DataFrame.to_numpy(data_pd)

r = list(range(1, 447758))
pgd_list = []
for i in r:
    pgd_list.append(str(data_np[i][column]))

search_result = []
searchword_start = '가'
searchword_end = '톤'
searchword_mission = '사'
num = list(range(0, 5))

# 첫글자 끝글자 검색기

for i in pgd_list:
    if i.find(searchword_start) == 0:
        search_result.append(i)

search_result.sort(key=len)
result = search_result[::-1]

num = list(range(0, 5))
for i in num:
    print(result[i])




# 미션 검색기

# mission_len = []
# mission_search = []
#
# for word in pgd_list:
#     c = word.count(searchword_mission)
#     if c > 0 and word.find(searchword_start) == 0:
#         mission_len.append(c)
#         mission_search.append(word)
# mission = np.array(mission_search)
#
# mission_len_array = np.array(mission_len)
# sorting_index = np.argsort(mission_len_array)
# mission_result = mission[sorting_index]
# result = mission_result[::-1]
#
#
#
# for i in num:
#     print(result[i])






