#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import json


# In[ ]:





# In[3]:


with open('brands.json') as inputfile:
    df = pd.read_json(inputfile , lines = True)

# Step 1 = Clean the unncessary fields from id columns. Convert the id's to strings in order to pull only the necessary data from the middle of the string.

type(str(df['_id']))
df['_id'] = df['_id'].astype("string")
df['_id'] = df['_id'].str[10:34]
print(df['_id'])


##df.to_csv('brands.csv', index=False)


# In[ ]:





# In[5]:


with open('receipts.json') as inputfile:
    df = pd.read_json(inputfile , lines = True)
#df

# Step 1 = Clean the unncessary fields from id and date columns. Convert the id's and date to strings in order to pull only the necessary data from the middle of the string.
# Step 2 = Remove the trailing zeros from the timestamps in order to convert from UNIX timestamps to dates.

type(str(df['_id']))
df['_id'] = df['_id'].astype("string")
df['_id'] = df['_id'].str[10:34]
#print(df['_id'])

type(str(df['createDate']))
df['createDate'] = df['createDate'].astype("string")
df['createDate'] = df['createDate'].str[10:20]
#print(df['dateScanned'])

type(str(df['dateScanned']))
df['dateScanned'] = df['dateScanned'].astype("string")
df['dateScanned'] = df['dateScanned'].str[10:20]
#print(df['dateScanned'])

type(str(df['finishedDate']))
df['finishedDate'] = df['finishedDate'].astype("string")
df['finishedDate'] = df['finishedDate'].str[10:20]
#print(df['finishedDate'])

type(str(df['modifyDate']))
df['modifyDate'] = df['modifyDate'].astype("string")
df['modifyDate'] = df['modifyDate'].str[10:20]
#print(df['modifyDate'])

type(str(df['pointsAwardedDate']))
df['pointsAwardedDate'] = df['pointsAwardedDate'].astype("string")
df['pointsAwardedDate'] = df['pointsAwardedDate'].str[10:20]
#print(df['pointsAwardedDate'])

type(str(df['purchaseDate']))
df['purchaseDate'] = df['purchaseDate'].astype("string")
df['purchaseDate'] = df['purchaseDate'].str[10:20]
#print(df['purchaseDate'])

type(str(df['rewardsReceiptItemList']))
df['rewardsReceiptItemList'] = df['rewardsReceiptItemList'].astype("string")
df['rewardsReceiptItemList'] = df['rewardsReceiptItemList'].str[2:]
df['rewardsReceiptItemList'] = df['rewardsReceiptItemList'].str[:-2]
#print(df['rewardsReceiptItemList'])

df['rewardsReceiptItemList'] = df['rewardsReceiptItemList'].str.replace('\'', '')
#df['rewardsReceiptItemList'].str.split(',', n=20, expand = True) 
print(df['rewardsReceiptItemList'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[72]:


with open('users.json') as inputfile:
    df = pd.read_json(inputfile , lines = True)
df

# Step 1 = Clean the unncessary fields from id columns. Convert the id'sto strings in order to pull only the necessary data from the middle of the string.

type(str(df['_id']))
df['_id'] = df['_id'].astype("string")
df['_id'] = df['_id'].str[10:34]
print(df['_id'])


type(str(df['createdDate']))
df['createdDate'] = df['createdDate'].astype("string")
df['createdDate'] = df['createdDate'].str[10:20]
#print(df['createdDate'])

type(str(df['lastLogin']))
df['lastLogin'] = df['lastLogin'].astype("string")
df['lastLogin'] = df['lastLogin'].str[10:20]
#print(df['lastLogin'])


df.to_csv('users.csv', index=False)


# In[18]:


from datetime import datetime
ts = int("1609687530")
print(datetime.utcfromtimesta(ts).strftime('%Y-%m-%d %H:%M:%S'))


# In[75]:


with open('rewardsReceiptItemList.csv') as inputfile:
    df = pd.read_csv(inputfile)
df.to_json('rewardsReceiptItemList.json', orient='records', lines=True)

