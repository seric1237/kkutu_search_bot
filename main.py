# 표국대 및 우샘 정리 코드

import pandas as pd
Location = 'C:\kkutu'
ao ='integrated.xlsx'
column = 0

data_pd = pd.read_excel('{}/{}'.format(Location, ao),
                            header=None, index_col=None, names=None)
print('1')
data_np = pd.DataFrame.to_numpy(data_pd)
r = list(range(0, 292634))
a_pgd = []
for i in r:
    a_pgd.append(str(data_np[i][column]))
print('2')
re_list = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '^']

for i, word in enumerate(a_pgd):
    for v in re_list:
        a_pgd[i] = a_pgd[i].replace(v, '')
print('3')

for i in a_pgd:
    if len(i) == 1:
        a_pgd.remove(i)

pgd_list = list(set(a_pgd))

print('4')

df = pd.DataFrame(pgd_list)
df.to_excel('kkutu_integrated.xlsx', index=False)

# 단어 데이터베이스 정리 코드
# import pandas as pd
# Location = 'C:\kkutu'
# db = 'onlyKoreanDB.xlsx'
# column = 0
#
# data_pd = pd.read_excel('{}/{}'.format(Location, db),
#                             header=None, index_col=None, names=None)
# data_np = pd.DataFrame.to_numpy(data_pd)
# r = list(range(0, 431367))
# a_db = []
# database = []
# for i in r:
#     a_db.append(str(data_np[i][column]))
# for i in a_db:
#     if '하다' not in str(i)[-2:] and '이다' not in str(i)[-2:] and '되다' not in str(i)[-2:] and '지다' not in str(i)[-2:] \
#             and '답다' not in str(i)[-2:] and '대다' not in str(i)[-2:] and len(str(i)) > 1:
#         database.append(i)
# db_df = pd.DataFrame(database)
# db_df.to_excel('dblist.xlsx', index=False)

# 두 단어 중복 제거
# import pandas as pd
# Location = 'C:\kkutu'
# fin = 'semifinal.xlsx'
# column = 0
#
# fin_pd = pd.read_excel('{}/{}'.format(Location, fin),
#                             header=None, index_col=None, names=None)
# data_np = pd.DataFrame.to_numpy(fin_pd)
# r = list(range(0, 823136))
# fin_list = []
# for i in r:
#     fin_list.append(str(data_np[i][column]))
# final = list(set(fin_list))
# fin_df = pd.DataFrame(final)
# fin_df.to_excel('final.xlsx', index=False)