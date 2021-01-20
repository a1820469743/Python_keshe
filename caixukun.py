#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.io.json import json_normalize

plt.style.use('ggplot')
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决seaborn中文字体显示问题
plt.rc('figure', figsize=(10, 10))  #把plt默认的图片size调大一点
plt.rcParams["figure.dpi"] =mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv('D://caixukun.csv')


# In[3]:


data.info()


# In[4]:


data.sample(5)


# #### 1. 数据清洗
# 由于数据入库的时候没有进行清洗，所以数据多出了很多没用的字段，需要先清洗掉

# In[5]:


data.columns


# In[6]:


in_columns = ['attitudes_count', 'comments_count', 'reposts_count', 'mid', 'raw_text', 
          'source', 'user.description', 'user.follow_count', 'user.followers_count', 
          'user.gender', 'user.id', 'user.mbrank', 'user.mbtype', 'user.profile_url', 
          'user.profile_image_url', 'user.screen_name', 'user.statuses_count', 
          'user.urank', 'user.verified', 'user.verified_reason']


# In[7]:


data = data[in_columns]


# In[8]:


data.info()


# In[9]:


data.to_csv('caixukun.csv', index=False)


# 问题：
# 1. 蔡徐坤的微博转发是否存在假流量？
# 2. 真假流量所占的比例各有多少？
# 3. 假流量粉丝是如何生产出来的？
# 4. 真流量粉的粉丝画像

# ### 1. 蔡徐坤的微博转发是否存在假流量？

# In[10]:


# 先来看看蔡徐坤的粉丝性别比例
fans_num = data['user.gender'].value_counts()
fans_num


# In[11]:


from pyecharts import Bar

bar = Bar("蔡徐坤粉丝性别比例初探", width = 600,height=500)
bar.add("(总数据102313条)", ['男', '女'], fans_num.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar


# In[12]:


np.round(fans_num/fans_num.sum()*100, 2)


# In[13]:


data[data['user.gender']=='m'].sample(5)


# ### 2. 真假流量所占的比例各有多少？

# In[14]:


data_fake = data[((data['user.follow_count']<=5)|(data['user.followers_count']<=5))&
                 (data['user.description']=='')&
                 (data['comments_count']==0)&
                (data['attitudes_count']==0)&
                (data['reposts_count']==0)&
                (data['user.mbrank']==0)]
data_fake.sample(5)


# In[15]:


data_fake.shape


# In[16]:


# 昵称里包含“用户”的，基本上可以断定是假粉丝
data_fake2_index = data[(data['user.follow_count']>5)&
                        (data['user.followers_count']>5)&
                        (data['user.screen_name'].str.contains('用户'))].index


# In[17]:


# 把假的流量粉丝转发组合起来
data_fake = pd.concat([data_fake, data.iloc[data_fake2_index]])


# In[18]:


data_fake.shape


# In[19]:


# 取出真粉的转发
data_true = data.drop(data_fake.index)


# In[20]:


data_true.shape


# In[21]:


print('真粉丝转发数占总转发数的{}%'.format(np.round(data_true.shape[0]/data.shape[0]*100, 2)))
print('假粉丝转发数占总转发数的{}%'.format(np.round(data_fake.shape[0]/data.shape[0]*100, 2)))


# In[22]:


bar = Bar("蔡徐坤真假流量的转发量", width = 600,height=500)
bar.add("(总数据102313条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
        [data.shape[0], data_fake.shape[0], data_true.shape[0]], is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar


# In[23]:


real_fans_num = data_true.drop_duplicates(subset='user.id').shape[0]


# In[24]:


bar = Bar("蔡徐坤真假流量的转发量与真实转发粉丝量(总数据102313条)", width = 600,height=500)
bar.add('', ['总转发量', '假粉丝转发量', '真粉丝转发量', '真实转发粉丝量'], 
        [data.shape[0], data_fake.shape[0], data_true.shape[0], real_fans_num], is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=20)
bar


# In[25]:


print('真实转发粉丝量占总转发数的{}%'.format(np.round(real_fans_num/data.shape[0]*100, 2)))


# -----------------吴青峰微博数据做对比-----------------

# In[193]:


db = conn.get_database('WuQingFeng')  # WuQingFeng

repost = db.get_collection('repost') # repost
mon_data = repost.find()  # 查询这个集合下的所有记录


# In[194]:


wqf_data = json_normalize([comment for comment in mon_data])


# In[195]:


wqf_data = wqf_data[in_columns]


# In[196]:


wqf_data.shape


# In[229]:


wqf_data_fake = wqf_data[((wqf_data['user.follow_count']<=5)|(wqf_data['user.followers_count']<=5))&
                         (wqf_data['user.description']=='')&
                         (wqf_data['comments_count']==0)&
                         (wqf_data['attitudes_count']==0)&
                         (wqf_data['reposts_count']==0)&
                         (wqf_data['user.mbrank']==0)]

wqf_data_fake2_index = wqf_data[(wqf_data['user.follow_count']>5)&
                                (wqf_data['user.followers_count']>5)&
                                (wqf_data['user.screen_name'].str.contains('用户'))].index
wqf_data_fake = pd.concat([wqf_data_fake, wqf_data.iloc[wqf_data_fake2_index]])
wqf_data_true = wqf_data.drop(wqf_data_fake.index)


# In[230]:


print('吴青峰真粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_true.shape[0]/wqf_data.shape[0]*100, 2)))
print('吴青峰假粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_fake.shape[0]/wqf_data.shape[0]*100, 2)))


# In[231]:


bar = Bar("吴青峰真假流量的转发量", width = 600,height=500)
bar.add("(总数据10006条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
        [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0]], is_stack=True,
        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar


# In[232]:


wqf_real_fans_num = wqf_data_true.drop_duplicates(subset='user.id').shape[0]

bar = Bar("吴青峰真假流量的转发量与真实转发粉丝量(总数据10006条)", width = 600,height=500)
bar.add('', ['总转发量', '假粉丝转发量', '真粉丝转发量', '真实转发粉丝量'], 
        [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0], 
         wqf_real_fans_num], is_stack=True, 
        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=20)
bar


# In[237]:


wqf_data.sample(5)


# In[239]:


data.sample(5)


# ### 3. 假流量粉丝是如何生产出来的？

# In[26]:


data_fake_gender = data_fake.drop_duplicates(subset='user.id')['user.gender'].value_counts()
data_fake_gender


# In[27]:


data_fake[data_fake['user.gender']=='f'].sample(5)


# In[28]:


bar = Bar("蔡徐坤假粉丝性别比例", width = 600,height=500)
bar.add("(假粉丝总数为40838)", ['男', '女'], data_fake_gender.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar


# In[29]:


38969/40838


# In[30]:


data_fake['raw_text'].value_counts()


# In[31]:


fake_source = data_fake['source'].value_counts()[:10]


# In[32]:


bar = Bar("蔡徐坤假粉丝Top10转发设备", width = 600,height=600)
bar.add("", fake_source.index, fake_source.values, is_stack=True, 
       xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
bar


# In[33]:


data_fake['user.follow_count'].mean()


# In[34]:


data_fake['user.followers_count'].mean()


# In[35]:


data_fake_sample = data_fake.sample(5)


# In[36]:


data_fake_sample['user.screen_name']


# In[37]:


data_fake_sample['user.profile_image_url'].values


# In[38]:


data_fake.sample(5)['user.screen_name']


# In[39]:


data_fake['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()


# In[40]:


data_fake.shape[0]


# In[41]:


data_fake['user.statuses_count'].mean()


# ### 4. 真流量粉的粉丝画像

# In[42]:


data_true.sample(5)


# In[43]:


data_true_gender = data_true.drop_duplicates(subset='user.id')['user.gender'].value_counts()
data_true_gender


# In[44]:


bar = Bar("蔡徐坤真粉丝性别比例", width = 600,height=500)
bar.add("(真粉丝总数为3926)", ['女', '男'], data_true_gender.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar


# In[45]:


data_true['raw_text'].value_counts()


# In[46]:


true_source = data_true['source'].value_counts()[:10]


# In[47]:


bar = Bar("蔡徐坤真粉丝Top10转发设备", width = 600,height=600)
bar.add("", true_source.index, true_source.values, is_stack=True, 
       xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
bar


# In[48]:


data_true['user.follow_count'].mean()


# In[49]:


data_true['user.followers_count'].mean()


# In[50]:


data_true.sample(5)['user.screen_name']


# In[51]:


data_true['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()


# In[52]:


data_true.shape[0]


# In[53]:


# 绘制蔡徐坤真粉丝的简介词云图
import jieba
from collections import Counter
from pyecharts import WordCloud

jieba.add_word('蔡徐坤')

swords = [x.strip() for x in open ('stopwords.txt')]


# In[54]:


def plot_word_cloud(data, swords, columns):
    text = ''.join(data[columns])
    words = list(jieba.cut(text))
    ex_sw_words = []
    for word in words:
        if len(word)>1 and (word not in swords):
            ex_sw_words.append(word)
    c = Counter()
    c = Counter(ex_sw_words)
    wc_data = pd.DataFrame({'word':list(c.keys()), 'counts':list(c.values())}).sort_values(by='counts', ascending=False).head(100)
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", wc_data['word'], wc_data['counts'], word_size_range=[20, 100])
    return wordcloud


# In[309]:


plot_word_cloud(data=data_true, swords=swords, columns='user.description')


# In[310]:


plot_word_cloud(data=data_true, swords=swords, columns='raw_text')

