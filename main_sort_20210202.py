#!/usr/bin/env python
# coding: utf-8

# - 61 unisort
# - 60 bisort
# 
# all covered in the code: tools

# In[1]:


from tools.crosssection import *


# ### read data

# In[2]:


file = 'data_Jan2021/chars60/rank/chars60_rank_imputed.pkl'
df = read_pickle_file(file)

# file = 'data_Jan2021/chars60/raw/chars60_raw_imputed.pkl'
# df_raw = read_pickle_file(file)


# In[3]:


df.columns


# In[4]:


char_list = ['me',
           'mom6m', 'acc', 'beta', 'bm_ia',
           'herf', 'rna', 'cash', 'std_dolvol', 'seas1a',
           'lgr', 'dolvol', 'nincr', 'turn', 'hire',
           'mom12m', 'pscore', 'noa', 'rd_sale', 'mom60m',
           'ato', 'roe', 'rdm', 'sue', 'lev',
           'mom1m', 'chcsho', 'ni', 'ill', 'chpm',
           'cfp', 'baspread', 'cashdebt', 'pm', 'abr',
           'depr', 'rsup', 'bm', 'maxret', 'rvar_capm',
           'cinvest', 'rvar_mean', 're', 'mom36m',
           'ep', 'sp', 'gma', 'me_ia', 'zerotrade',
           'op', 'pctacc', 'chtx', 'rvar_ff3', 'adm',
           'alm', 'dy', 'std_turn', 'sgr', 'agr',
           'grltnoa', 'roa']
# char_list = ['roe','mom12m','beta']
print(len(char_list))
rank_char_list = ['rank_'+i for i in char_list]

# identifiers
ids = ['gvkey','permno','date','ret','lag_me','log_me']


# ### delete obs. with NA me

# In[5]:


df1 = df[ids+rank_char_list]
print(df1.shape)
df1 = df1[~df1['lag_me'].isna()]
print(df1.shape)


# In[6]:


print(df1.head())


# # 20210128
# - do sorting based on the rank
# - construct decile portfolios
# - calculate the ls factors

# In[ ]:


cs_vw = cs(df1, char_list, 5, 'lag_me')
cs_vw.update_all(parallel=True)


# In[ ]:


cs_ew = cs(df1, char_list, 5, 'ew')
cs_ew.update_all(parallel=True)


# In[ ]:


with open('cs_vw.pkl', 'wb') as f:
    pkl.dump(cs_vw, f)

with open('cs_ew.pkl', 'wb') as f:
    pkl.dump(cs_ew, f)

