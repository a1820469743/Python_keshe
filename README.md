```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
from pandas.io.json import json_normalize

plt.style.use('ggplot')
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决seaborn中文字体显示问题
plt.rc('figure', figsize=(10, 10))  #把plt默认的图片size调大一点
plt.rcParams["figure.dpi"] =mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
%matplotlib inline

```


```python
data = pd.read_csv('D://caixukun.csv', delimiter=';', encoding='utf8', names=['attitudes_count', 'comments_count', 'reposts_count', 'mid', 'raw_text',
          'source', 'user.description', 'user.follow_count', 'user.followers_count',
          'user.gender', 'user.id', 'user.mbrank', 'user.mbtype', 'user.profile_url',
          'user.profile_image_url', 'user.screen_name', 'user.statuses_count',
          'user.urank', 'user.verified', 'user.verified_reason'])
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0,0,0,4.34804E+15,也许可有可无是我的存在//@葵的妈奎的妹坤的妻:[抱抱]...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>102312</th>
      <td>0,0,0,4.34868E+15,Oh how'd you'd ever do that ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102313</th>
      <td>0,0,0,4.34868E+15,All I do is wait wait wait,三...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102314</th>
      <td>0,0,0,4.34868E+15,"dei tuoi gioielli l’Orrore ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102315</th>
      <td>0,0,0,4.34868E+15,"del giorno, delle strade",前...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102316</th>
      <td>0,0,0,4.34868E+15,"Verso di te, candela, la fa...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>102317 rows × 20 columns</p>
</div>




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 102317 entries, 0 to 102316
    Data columns (total 20 columns):
     #   Column                  Non-Null Count   Dtype  
    ---  ------                  --------------   -----  
     0   attitudes_count         102317 non-null  object 
     1   comments_count          0 non-null       float64
     2   reposts_count           0 non-null       float64
     3   mid                     0 non-null       float64
     4   raw_text                0 non-null       float64
     5   source                  0 non-null       float64
     6   user.description        0 non-null       float64
     7   user.follow_count       0 non-null       float64
     8   user.followers_count    0 non-null       float64
     9   user.gender             0 non-null       float64
     10  user.id                 0 non-null       float64
     11  user.mbrank             0 non-null       float64
     12  user.mbtype             0 non-null       float64
     13  user.profile_url        0 non-null       float64
     14  user.profile_image_url  0 non-null       float64
     15  user.screen_name        0 non-null       float64
     16  user.statuses_count     0 non-null       float64
     17  user.urank              0 non-null       float64
     18  user.verified           0 non-null       float64
     19  user.verified_reason    0 non-null       float64
    dtypes: float64(19), object(1)
    memory usage: 15.6+ MB
    


```python
data.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>_id</th>
      <th>attitudes_count</th>
      <th>bid</th>
      <th>can_edit</th>
      <th>cardid</th>
      <th>comments_count</th>
      <th>content_auth</th>
      <th>created_at</th>
      <th>darwin_tags</th>
      <th>edit_at</th>
      <th>...</th>
      <th>user.mbtype</th>
      <th>user.profile_image_url</th>
      <th>user.profile_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
      <th>user.verified_type</th>
      <th>user.verified_type_ext</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>76462</th>
      <td>5c85cc1af2766b0bd3eac927</td>
      <td>0</td>
      <td>HknmbuU4Q</td>
      <td>False</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>3小时前</td>
      <td>[]</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>https://m.weibo.cn/u/7012413636?uid=7012413636</td>
      <td>困困的菜ICV124</td>
      <td>33</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
      <td>-1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8855</th>
      <td>5c84a991f2766b0bd3e75385</td>
      <td>0</td>
      <td>HkgoNlxW5</td>
      <td>False</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>52分钟前</td>
      <td>[]</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>https://m.weibo.cn/u/7012480301?uid=7012480301</td>
      <td>雨露奎哥tCs622</td>
      <td>19</td>
      <td>1</td>
      <td>False</td>
      <td>NaN</td>
      <td>-1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>78023</th>
      <td>5c85d1c1f2766b0bd3eadd3a</td>
      <td>0</td>
      <td>HkoAu3MmB</td>
      <td>False</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>13分钟前</td>
      <td>[]</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>https://m.weibo.cn/u/7012731691?uid=7012731691</td>
      <td>最酷的坤XLL749</td>
      <td>27</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
      <td>-1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>88036</th>
      <td>5c85f7a0f2766b0bd3eb4fb1</td>
      <td>0</td>
      <td>HkphJ57ZE</td>
      <td>False</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>1小时前</td>
      <td>[]</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>https://m.weibo.cn/u/7017930638?uid=7017930638</td>
      <td>超赞坤哥cVR094</td>
      <td>24</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
      <td>-1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>73676</th>
      <td>5c85c47ef2766b0bd3eaab8a</td>
      <td>0</td>
      <td>HkohTnpCI</td>
      <td>False</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>2小时前</td>
      <td>[]</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.1080.1080.18...</td>
      <td>https://m.weibo.cn/u/6673451463?uid=6673451463</td>
      <td>坤的白菜丝</td>
      <td>32</td>
      <td>9</td>
      <td>False</td>
      <td>NaN</td>
      <td>-1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 97 columns</p>
</div>



#### 1. 数据清洗
由于数据入库的时候没有进行清洗，所以数据多出了很多没用的字段，需要先清洗掉


```python
data.columns
```




    Index(['_id', 'attitudes_count', 'bid', 'can_edit', 'cardid', 'comments_count',
           'content_auth', 'created_at', 'darwin_tags', 'edit_at', 'edit_count',
           'favorited', 'hide_flag', 'id', 'isLongText', 'is_imported_topic',
           'is_paid', 'mblog_vip_type', 'mblogtype', 'mid', 'more_info_type',
           'pending_approval_count', 'pic_ids', 'pic_types', 'pid', 'raw_text',
           'reposts_count', 'reward_exhibition_type', 'show_additional_indication',
           'source', 'sync_mblog', 'topic_id', 'user.avatar_hd',
           'user.badge.anniversary', 'user.badge.asiad_2018',
           'user.badge.bind_taobao', 'user.badge.cz_wed_2017', 'user.badge.dailv',
           'user.badge.dailv_2018', 'user.badge.denglong_2019',
           'user.badge.double11_2018', 'user.badge.dzwbqlx_2016',
           'user.badge.follow_whitelist_video', 'user.badge.fools_day_2016',
           'user.badge.fu_2019', 'user.badge.gongyi', 'user.badge.gongyi_level',
           'user.badge.hongbaofei_2019', 'user.badge.kpl_2018',
           'user.badge.league_badge', 'user.badge.league_badge_2018',
           'user.badge.lol_gm_2017', 'user.badge.lol_s8',
           'user.badge.meilizhongguo_2018', 'user.badge.memorial_2018',
           'user.badge.national_day_2018', 'user.badge.panda',
           'user.badge.qixi_2018', 'user.badge.suishoupai_2018',
           'user.badge.super_star_2017', 'user.badge.super_star_2018',
           'user.badge.taobao', 'user.badge.travel_2017',
           'user.badge.uefa_euro_2016', 'user.badge.unread_pool',
           'user.badge.unread_pool_ext', 'user.badge.user_name_certificate',
           'user.badge.vip_activity2', 'user.badge.wbzy_2018',
           'user.badge.wenchuan_10th', 'user.badge.wenda_v2',
           'user.badge.womensday_2018', 'user.badge.worldcup_2018',
           'user.badge.yiqijuan_2018', 'user.badge.zongyiji', 'user.close_blue_v',
           'user.cover_image_phone', 'user.description', 'user.follow_count',
           'user.follow_me', 'user.followers_count', 'user.following',
           'user.gender', 'user.id', 'user.like', 'user.like_me', 'user.mbrank',
           'user.mbtype', 'user.profile_image_url', 'user.profile_url',
           'user.screen_name', 'user.statuses_count', 'user.urank',
           'user.verified', 'user.verified_reason', 'user.verified_type',
           'user.verified_type_ext'],
          dtype='object')




```python
in_columns = ['attitudes_count', 'comments_count', 'reposts_count', 'mid', 'raw_text', 
          'source', 'user.description', 'user.follow_count', 'user.followers_count', 
          'user.gender', 'user.id', 'user.mbrank', 'user.mbtype', 'user.profile_url', 
          'user.profile_image_url', 'user.screen_name', 'user.statuses_count', 
          'user.urank', 'user.verified', 'user.verified_reason']
```


```python
data = data[in_columns]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>attitudes_count,comments_count,reposts_count,m...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0,0,0,4.34804E+15,也许可有可无是我的存在//@葵的妈奎的妹坤的妻:[抱抱]...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>102312</th>
      <td>0,0,0,4.34868E+15,Oh how'd you'd ever do that ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102313</th>
      <td>0,0,0,4.34868E+15,All I do is wait wait wait,三...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102314</th>
      <td>0,0,0,4.34868E+15,"dei tuoi gioielli l’Orrore ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102315</th>
      <td>0,0,0,4.34868E+15,"del giorno, delle strade",前...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102316</th>
      <td>0,0,0,4.34868E+15,"Verso di te, candela, la fa...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>102317 rows × 20 columns</p>
</div>




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 102317 entries, 0 to 102316
    Data columns (total 20 columns):
     #   Column                  Non-Null Count   Dtype  
    ---  ------                  --------------   -----  
     0   attitudes_count         102317 non-null  object 
     1   comments_count          0 non-null       float64
     2   reposts_count           0 non-null       float64
     3   mid                     0 non-null       float64
     4   raw_text                0 non-null       float64
     5   source                  0 non-null       float64
     6   user.description        0 non-null       float64
     7   user.follow_count       0 non-null       float64
     8   user.followers_count    0 non-null       float64
     9   user.gender             0 non-null       float64
     10  user.id                 0 non-null       float64
     11  user.mbrank             0 non-null       float64
     12  user.mbtype             0 non-null       float64
     13  user.profile_url        0 non-null       float64
     14  user.profile_image_url  0 non-null       float64
     15  user.screen_name        0 non-null       float64
     16  user.statuses_count     0 non-null       float64
     17  user.urank              0 non-null       float64
     18  user.verified           0 non-null       float64
     19  user.verified_reason    0 non-null       float64
    dtypes: float64(19), object(1)
    memory usage: 15.6+ MB
    


```python
data.to_csv('caixukun.csv', index=False)
```

问题：
1. 蔡徐坤的微博转发是否存在假流量？
2. 真假流量所占的比例各有多少？
3. 假流量粉丝是如何生产出来的？
4. 真流量粉的粉丝画像

### 1. 蔡徐坤的微博转发是否存在假流量？


```python
# 先来看看蔡徐坤的粉丝性别比例
fans_num = data['user.gender'].value_counts()
fans_num
```




    m    93618
    f     8695
    Name: user.gender, dtype: int64




```python
from pyecharts import Bar

bar = Bar("蔡徐坤粉丝性别比例初探", width = 600,height=500)
bar.add("(总数据102313条)", ['男', '女'], fans_num.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="3d94c622573f4ebab2ce5170ccf9d1cc" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_3d94c622573f4ebab2ce5170ccf9d1cc = echarts.init(document.getElementById('3d94c622573f4ebab2ce5170ccf9d1cc'), null, {renderer: 'canvas'});
var option_3d94c622573f4ebab2ce5170ccf9d1cc = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u7c89\u4e1d\u6027\u522b\u6bd4\u4f8b\u521d\u63a2",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 2406483,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "(\u603b\u6570\u636e102313\u6761)",
            "data": [
                93618.0,
                8695.0
            ],
            "stack": "stack_2406483",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 2406483
        }
    ],
    "legend": [
        {
            "data": [
                "(\u603b\u6570\u636e102313\u6761)"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u7537",
                "\u5973"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_3d94c622573f4ebab2ce5170ccf9d1cc.setOption(option_3d94c622573f4ebab2ce5170ccf9d1cc);

    });
</script>





```python
from pyecharts import Bar

bar = Bar("蔡徐坤粉丝性别比例初探", width = 600,height=500)
bar.add("(总数据102313条)", ['男', '女'], fans_num.values, is_stack=True,
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar(fans_num/fans_num.sum()*100, 2)
```




    m    91.5
    f     8.5
    Name: user.gender, dtype: float64




```python
data[data['user.gender']=='m'].sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2270</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348038635531052</td>
      <td>卷毛帅哥的自拍简直是太帅啦！//@Elvirababe-:再见啦千千//@AK47-HIAH...</td>
      <td>红米Redmi</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7020364228</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7020364228?uid=7020364228</td>
      <td>https://tvax4.sinaimg.cn/crop.160.0.640.640.18...</td>
      <td>快乐追坤Z96406</td>
      <td>30</td>
      <td>2</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14667</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348319830485901</td>
      <td>Even anticipate discrete, I met the other thei...</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6980837370</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6980837370?uid=6980837370</td>
      <td>https://tvax1.sinaimg.cn/crop.0.65.169.169.180...</td>
      <td>结愁肠百QfQ953</td>
      <td>201</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>91271</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348662274153156</td>
      <td>善良的人，善良的心//@石头打瞌睡:#东方风云榜让世界看见蔡徐坤#  [喵喵] #蔡徐坤的未...</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7011848763</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7011848763?uid=7011848763</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>AK战士phX674</td>
      <td>60</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24223</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348391876258523</td>
      <td>[吃瓜]//@蔡老板的心尖宠:#蔡徐坤[超话]#|#蔡徐坤的未完成#  用真心呵护小动物，感...</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6827212466</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6827212466?uid=6827212466</td>
      <td>https://tvax3.sinaimg.cn/default/images/defaul...</td>
      <td>用户6827212466</td>
      <td>243</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24765</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348374163394192</td>
      <td>Four</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7012476563</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7012476563?uid=7012476563</td>
      <td>https://tvax2.sinaimg.cn/crop.0.10.640.640.180...</td>
      <td>小坤的花3MB514</td>
      <td>31</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 2. 真假流量所占的比例各有多少？


```python
data_fake = data[((data['user.follow_count']<=5)|(data['user.followers_count']<=5))&
                 (data['user.description']=='')&
                 (data['comments_count']==0)&
                (data['attitudes_count']==0)&
                (data['reposts_count']==0)&
                (data['user.mbrank']==0)]
data_fake.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>85984</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348635833440929</td>
      <td>遇见你真好 好喜欢你呀</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7017942798</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7017942798?uid=7017942798</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>守护坤宝rGX399</td>
      <td>13</td>
      <td>2</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14659</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348319851483539</td>
      <td>My eyes have seen and my ears have heard.     ...</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6974693897</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6974693897?uid=6974693897</td>
      <td>https://tvax3.sinaimg.cn/crop.3.0.94.94.180/00...</td>
      <td>花花世界cu1087</td>
      <td>51</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10218</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348296446870440</td>
      <td>With the wonder of your love， the sun above al...</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7011842865</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7011842865?uid=7011842865</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>绽放光芒ofM731</td>
      <td>33</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>78725</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348610562398099</td>
      <td>身为偶像，以身作则。</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6941108958</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6941108958?uid=6941108958</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.690.690.180/...</td>
      <td>葵妹威武36F539</td>
      <td>64</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>55694</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348399592999505</td>
      <td>Distance, //@小葵花迷糊:带着我们的爱好好长大吧[米奇比心]蔡徐坤</td>
      <td>三星Galaxy NOTE III</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6940713794</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6940713794?uid=6940713794</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.446.446.180/...</td>
      <td>AK突突9TM962</td>
      <td>17</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_fake.shape
```




    (95326, 20)




```python
# 昵称里包含“用户”的，基本上可以断定是假粉丝
data_fake2_index = data[(data['user.follow_count']>5)&
                        (data['user.followers_count']>5)&
                        (data['user.screen_name'].str.contains('用户'))].index
```


```python
# 把假的流量粉丝转发组合起来
data_fake = pd.concat([data_fake, data.iloc[data_fake2_index]])
```


```python
data_fake.shape
```




    (95397, 20)




```python
# 取出真粉的转发
data_true = data.drop(data_fake.index)
```


```python
data_true.shape
```




    (6916, 20)




```python
print('真粉丝转发数占总转发数的{}%'.format(np.round(data_true.shape[0]/data.shape[0]*100, 2)))
print('假粉丝转发数占总转发数的{}%'.format(np.round(data_fake.shape[0]/data.shape[0]*100, 2)))
```

    真粉丝转发数占总转发数的6.76%
    假粉丝转发数占总转发数的93.24%
    


```python
bar = Bar("蔡徐坤真假流量的转发量", width = 600,height=500)
bar.add("(总数据102313条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
        [data.shape[0], data_fake.shape[0], data_true.shape[0]], is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="7a453fedd70e477788cbea213bd5256b" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_7a453fedd70e477788cbea213bd5256b = echarts.init(document.getElementById('7a453fedd70e477788cbea213bd5256b'), null, {renderer: 'canvas'});
var option_7a453fedd70e477788cbea213bd5256b = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u5047\u6d41\u91cf\u7684\u8f6c\u53d1\u91cf",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 3006664,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "(\u603b\u6570\u636e102313\u6761)",
            "data": [
                102313,
                95397,
                6916
            ],
            "stack": "stack_3006664",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 3006664
        }
    ],
    "legend": [
        {
            "data": [
                "(\u603b\u6570\u636e102313\u6761)"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u603b\u8f6c\u53d1\u91cf",
                "\u5047\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u7c89\u4e1d\u8f6c\u53d1\u91cf"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_7a453fedd70e477788cbea213bd5256b.setOption(option_7a453fedd70e477788cbea213bd5256b);

    });
</script>





```python
real_fans_num = data_true.drop_duplicates(subset='user.id').shape[0]
```


```python
bar = Bar("蔡徐坤真假流量的转发量与真实转发粉丝量(总数据102313条)", width = 600,height=500)
bar.add('', ['总转发量', '假粉丝转发量', '真粉丝转发量', '真实转发粉丝量'], 
        [data.shape[0], data_fake.shape[0], data_true.shape[0], real_fans_num], is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=20)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="8c10c8f69cf949f384cef0d27d6b51f9" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_8c10c8f69cf949f384cef0d27d6b51f9 = echarts.init(document.getElementById('8c10c8f69cf949f384cef0d27d6b51f9'), null, {renderer: 'canvas'});
var option_8c10c8f69cf949f384cef0d27d6b51f9 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u5047\u6d41\u91cf\u7684\u8f6c\u53d1\u91cf\u4e0e\u771f\u5b9e\u8f6c\u53d1\u7c89\u4e1d\u91cf(\u603b\u6570\u636e102313\u6761)",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 3646397,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "",
            "data": [
                102313,
                95397,
                6916,
                3926
            ],
            "stack": "stack_3646397",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 3646397
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 20,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u603b\u8f6c\u53d1\u91cf",
                "\u5047\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u5b9e\u8f6c\u53d1\u7c89\u4e1d\u91cf"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_8c10c8f69cf949f384cef0d27d6b51f9.setOption(option_8c10c8f69cf949f384cef0d27d6b51f9);

    });
</script>





```python
print('真实转发粉丝量占总转发数的{}%'.format(np.round(real_fans_num/data.shape[0]*100, 2)))
```

    真实转发粉丝量占总转发数的3.84%
    

-----------------吴青峰微博数据做对比-----------------


```python
wqf_data = json_normalize([comment for comment in data])
```


```python
wqf_data = wqf_data[in_columns]
```


```python
wqf_data.shape
```




    (10006, 20)




```python
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
```


```python
print('吴青峰真粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_true.shape[0]/wqf_data.shape[0]*100, 2)))
print('吴青峰假粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_fake.shape[0]/wqf_data.shape[0]*100, 2)))
```

    吴青峰真粉丝转发数占总转发数的96.52%
    吴青峰假粉丝转发数占总转发数的3.48%
    


```python
bar = Bar("吴青峰真假流量的转发量", width = 600,height=500)
bar.add("(总数据10006条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
        [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0]], is_stack=True,
        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="51652d94b2434047952e6e7c0e8f4ec0" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_51652d94b2434047952e6e7c0e8f4ec0 = echarts.init(document.getElementById('51652d94b2434047952e6e7c0e8f4ec0'), null, {renderer: 'canvas'});
var option_51652d94b2434047952e6e7c0e8f4ec0 = {
    "title": [
        {
            "text": "\u5434\u9752\u5cf0\u771f\u5047\u6d41\u91cf\u7684\u8f6c\u53d1\u91cf",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 263637,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "(\u603b\u6570\u636e10006\u6761)",
            "data": [
                10006,
                348,
                9658
            ],
            "stack": "stack_263637",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 263637
        }
    ],
    "legend": [
        {
            "data": [
                "(\u603b\u6570\u636e10006\u6761)"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u603b\u8f6c\u53d1\u91cf",
                "\u5047\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u7c89\u4e1d\u8f6c\u53d1\u91cf"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_51652d94b2434047952e6e7c0e8f4ec0.setOption(option_51652d94b2434047952e6e7c0e8f4ec0);

    });
</script>





```python
wqf_real_fans_num = wqf_data_true.drop_duplicates(subset='user.id').shape[0]

bar = Bar("吴青峰真假流量的转发量与真实转发粉丝量(总数据10006条)", width = 600,height=500)
bar.add('', ['总转发量', '假粉丝转发量', '真粉丝转发量', '真实转发粉丝量'], 
        [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0], 
         wqf_real_fans_num], is_stack=True, 
        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=20)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="e673131833db428886f0fdee20b31af1" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_e673131833db428886f0fdee20b31af1 = echarts.init(document.getElementById('e673131833db428886f0fdee20b31af1'), null, {renderer: 'canvas'});
var option_e673131833db428886f0fdee20b31af1 = {
    "title": [
        {
            "text": "\u5434\u9752\u5cf0\u771f\u5047\u6d41\u91cf\u7684\u8f6c\u53d1\u91cf\u4e0e\u771f\u5b9e\u8f6c\u53d1\u7c89\u4e1d\u91cf(\u603b\u6570\u636e10006\u6761)",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 7064643,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "",
            "data": [
                10006,
                348,
                9658,
                9318
            ],
            "stack": "stack_7064643",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 7064643
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 20,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u603b\u8f6c\u53d1\u91cf",
                "\u5047\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u5b9e\u8f6c\u53d1\u7c89\u4e1d\u91cf"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_e673131833db428886f0fdee20b31af1.setOption(option_e673131833db428886f0fdee20b31af1);

    });
</script>





```python
wqf_data.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6149</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>4347751288499206</td>
      <td>爱母亲一生一世</td>
      <td>红米Redmi</td>
      <td></td>
      <td>32</td>
      <td>31</td>
      <td>m</td>
      <td>5676300325</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/5676300325?uid=5676300325</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>只抓猪猪打</td>
      <td>4</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3805</th>
      <td>23</td>
      <td>4</td>
      <td>11</td>
      <td>4347895002290957</td>
      <td>哭//@囤仔:今日催泪弹</td>
      <td>iPhone客户端</td>
      <td>公主号：饭饭哒  混干皮，会写功课会发壁纸ヾ(･ω･*)ﾉ</td>
      <td>435</td>
      <td>717510</td>
      <td>f</td>
      <td>2273529342</td>
      <td>6</td>
      <td>12</td>
      <td>https://m.weibo.cn/u/2273529342?uid=2273529342</td>
      <td>https://tvax1.sinaimg.cn/crop.11.0.728.728.180...</td>
      <td>饭饭饭饭哒</td>
      <td>3380</td>
      <td>47</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6141</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4347750722696051</td>
      <td>转发微博</td>
      <td>iPhone客户端</td>
      <td>诗酒趁年华.</td>
      <td>458</td>
      <td>142</td>
      <td>f</td>
      <td>5846588842</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/5846588842?uid=5846588842</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>阿羽想当锦鲤大王</td>
      <td>1350</td>
      <td>9</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>760</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348436402625735</td>
      <td>今日的晚安曲，晚安。[心]@吳青峰</td>
      <td>vivo AI智慧拍照X21</td>
      <td>诸行无常，初心不易。</td>
      <td>173</td>
      <td>17</td>
      <td>f</td>
      <td>7026562408</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7026562408?uid=7026562408</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>Star的一纸情书</td>
      <td>3</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6493</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4347738961856732</td>
      <td>我们就这样 各自奔天涯</td>
      <td>二月🐑iPhone XS Max</td>
      <td>你是我小心维护的梦</td>
      <td>255</td>
      <td>108</td>
      <td>f</td>
      <td>2055723847</td>
      <td>6</td>
      <td>12</td>
      <td>https://m.weibo.cn/u/2055723847?uid=2055723847</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.1080.1080.18...</td>
      <td>Surisuria</td>
      <td>10184</td>
      <td>47</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>78093</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348585275987130</td>
      <td>dove sei passata,</td>
      <td>Flyme</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7011819483</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7011819483?uid=7011819483</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>思念坤坤rWM833</td>
      <td>67</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>48412</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348425962842699</td>
      <td>[嘻嘻]//@KUN的小喵咪:#东方风云榜让世界看见蔡徐坤#</td>
      <td>Android</td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>f</td>
      <td>6589900139</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6589900139?uid=6589900139</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>偎率把啦s</td>
      <td>568</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>47984</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348404173745759</td>
      <td>从现在开始努力，一切都来得及</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7010929412</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7010929412?uid=7010929412</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.99.99.180/00...</td>
      <td>音乐才子asS736</td>
      <td>29</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>88312</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348631156993811</td>
      <td>When you leave I'm begging you not to go.蔡徐坤 @蔡徐坤</td>
      <td>HUAWEI P10</td>
      <td></td>
      <td>60</td>
      <td>1</td>
      <td>m</td>
      <td>6877062416</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6877062416?uid=6877062416</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>蔡小葵_cya56</td>
      <td>189</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17507</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348333834721683</td>
      <td>#东方风云榜让世界看见蔡徐坤#It’s not about the salary</td>
      <td>Android</td>
      <td></td>
      <td>61</td>
      <td>1</td>
      <td>m</td>
      <td>6862227587</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6862227587?uid=6862227587</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>蔡小葵_cvr19</td>
      <td>36</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 3. 假流量粉丝是如何生产出来的？


```python
data_fake_gender = data_fake.drop_duplicates(subset='user.id')['user.gender'].value_counts()
data_fake_gender
```




    m    38969
    f     1869
    Name: user.gender, dtype: int64




```python
data_fake[data_fake['user.gender']=='f'].sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>64180</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348440278763521</td>
      <td>I just wanna talk to u don't be afraid//@i坤555...</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>f</td>
      <td>6730864661</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6730864661?uid=6730864661</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>小葵花籽_包</td>
      <td>175</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>79757</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348610688763958</td>
      <td>转发微博</td>
      <td>华为手机 畅享玩不停</td>
      <td></td>
      <td>61</td>
      <td>1</td>
      <td>f</td>
      <td>6791332699</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6791332699?uid=6791332699</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.131.131.180/...</td>
      <td>野的像_狗</td>
      <td>22</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>65164</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348430597589392</td>
      <td>You scratch my back and I'll scratch yours.//@...</td>
      <td>Android</td>
      <td></td>
      <td>53</td>
      <td>1</td>
      <td>f</td>
      <td>6805019442</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6805019442?uid=6805019442</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.180.180.180/...</td>
      <td>xx__xmmt</td>
      <td>349</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75228</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348576912201314</td>
      <td>[好喜欢]//@蔡徐坤内人:[心][心]//@坤坤的公主群:#东方风云榜让世界看见蔡徐坤# ...</td>
      <td>Android</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>f</td>
      <td>6619935138</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6619935138?uid=6619935138</td>
      <td>https://tvax3.sinaimg.cn/default/images/defaul...</td>
      <td>用户6619935138</td>
      <td>255</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>87263</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348651100519444</td>
      <td>蔡徐坤你的美貌在我心里收藏。#东方风云榜让世界看见蔡徐坤#好喜欢呀@蔡徐坤</td>
      <td>前置双摄vivo X9s</td>
      <td></td>
      <td>59</td>
      <td>2</td>
      <td>f</td>
      <td>6853156261</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6853156261?uid=6853156261</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.179.179.180/...</td>
      <td>我和_君莫笑晕在厕所</td>
      <td>40</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
bar = Bar("蔡徐坤假粉丝性别比例", width = 600,height=500)
bar.add("(假粉丝总数为40838)", ['男', '女'], data_fake_gender.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="a9d40cd27c3c4d80a61fd3022e326822" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_a9d40cd27c3c4d80a61fd3022e326822 = echarts.init(document.getElementById('a9d40cd27c3c4d80a61fd3022e326822'), null, {renderer: 'canvas'});
var option_a9d40cd27c3c4d80a61fd3022e326822 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u5047\u7c89\u4e1d\u6027\u522b\u6bd4\u4f8b",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 3978762,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "(\u5047\u7c89\u4e1d\u603b\u6570\u4e3a40838)",
            "data": [
                38969.0,
                1869.0
            ],
            "stack": "stack_3978762",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 3978762
        }
    ],
    "legend": [
        {
            "data": [
                "(\u5047\u7c89\u4e1d\u603b\u6570\u4e3a40838)"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u7537",
                "\u5973"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_a9d40cd27c3c4d80a61fd3022e326822.setOption(option_a9d40cd27c3c4d80a61fd3022e326822);

    });
</script>





```python
38969/40838
```




    0.954233801851217




```python
data_fake['raw_text'].value_counts()
```




    转发微博                                                                                                                                         429
    I am only waiting for love to give myself up at last into his hands.                                                                         375
    想你//@蔡徐坤的南岸末阴大小姐:#东方风云榜让世界看见蔡徐坤# /#蔡徐坤的未完成#祝千千在新家能快快乐乐 健健康康的@蔡徐坤                                                                             289
    我心悦你//@蔡徐坤的南岸末阴大小姐:#东方风云榜让世界看见蔡徐坤# /#蔡徐坤的未完成#祝千千在新家能快快乐乐 健健康康的@蔡徐坤                                                                           288
    爱你//@蔡徐坤的南岸末阴大小姐:#东方风云榜让世界看见蔡徐坤# /#蔡徐坤的未完成#祝千千在新家能快快乐乐 健健康康的@蔡徐坤                                                                             278
    花花世界静守己心蔡徐坤未来可期！//@超超超超爱蔡蔡的思思:[爱你]                                                                                                           249
    As much as I should                                                                                                                          243
    So I can't forget you                                                                                                                        239
    哥哥加油唷，我们会一直在的！//@超超超超爱蔡蔡的思思:[爱你]                                                                                                             237
    属于你一个人的特别大的舞台！//@超超超超爱蔡蔡的思思:[爱你]                                                                                                             222
    My eyes have seen and my ears have heard.                                                                                                    214
    All my days I miss you next to me                                                                                                            204
    They come with their laws and their codes to bind me fast;                                                                                   200
    Now, I ask, has the time come at last when I may go in and see thy face and offer thee mysilent salutation?                                  193
    but I evade them ever, for I am only waiting for love to give myself up at last into his hands.                                              192
    That is why it is so late and why I have been guilty of such omissions.                                                                      190
    I have had my invitation to this world's festival, and thus my life has been blessed.                                                        182
    I am only waiting for love to give myself up at last into his hands.//@石头打瞌睡:#东方风云榜让世界看见蔡徐坤#  [喵喵] #蔡徐坤的未完成# 再见千老板，带着小葵对你的爱，健康成长哦[亲亲]@蔡徐坤    178
    It was my part at this feast to play upon my instrument, and I have done all I could.                                                        177
    I hate that I miss you                                                                                                                       175
    People blame me and call me heedless; I doubt not they are right in their blame.                                                             173
    Frivolous tireless                                                                                                                           171
    The market day is over and work is all done for the busy.                                                                                    170
    I'd stop if I could                                                                                                                          170
    Life, thin and light-off time and time again                                                                                                 168
    I believe I am                                                                                                                               165
    Those who came to call me in vain have gone back in anger.                                                                                   160
    All I do is wait wait wait                                                                                                                   154
    Weight weight weight                                                                                                                         154
    You're the one I'm waiting for                                                                                                               145
                                                                                                                                                ... 
    Need to know if you care //@懒得起昵称的我:傲娇千                                                                                                        1
    will finally light up your way //@懒得起昵称的我:傲娇千                                                                                                  1
    We soon believe what we desire.//@1个蕙:Bye                                                                                                      1
    水来 我在水中等你 火来 我在灰烬中等你//@坤坤的姐姐饭:再见千千 蔡徐坤麻麻爱你                                                                                                     1
    让我们静静分享 此刻难得的坦白                                                                                                                                1
    Birds of a feather flock together.//@CandyTlll:#东方风云榜让世界看见蔡徐坤# 要一直幸福哦 千千                                                                       1
    Cos I'm running low //@ByByBy-:哈                                                                                                               1
    希望她有一个好的主人                                                                                                                                     1
    So fantastic,God damn it ah yeah//@蔡徐坤家的小懒猫:想你                                                                                                 1
    倾尽毕生所学美好的词语都不足以形容你@蔡徐坤                                                                                                                         1
    世界上美好的事有很多，但是美好的人，却只有你一个，无论未来的路有多长，有多难，我们都会陪你走下去，没有期限，希望你不受束缚，希望你可以做自己喜欢的事。我们一直在，与你共进退。你若安好，我们便安好。[心]//@Kun_tatata:你好可爱啊！！！                    1
    越努力，越幸运                                                                                                                                        1
    做你自己，因为别人都有人去做了。//@KUN坤-Tiffany:千千再见                                                                                                           1
    [亲亲]//@储蓄卡身上的痣:#东方风云榜让世界看见蔡徐坤#  cxk #蔡徐坤的未完成# 再见千千，新的家庭要健康快乐呀！也希望有天在屏幕上看到他时，你能记起这份温暖与关爱！@蔡徐坤                                                   1
    “你吃烧烤会先烤什么？”   “先烤肉啊。” “我会先考虑你”//@Kun_tatata:你好可爱啊！！！                                                                                          1
    Two feet, One dance//@-Tanny:一路陪伴                                                                                                              1
    #东方风云榜让世界看见蔡徐坤# 日常想念你，坤坤宝贝                                                                                                                     1
    举贤才而授能兮，循绳墨而不颇。//@昔年KK--:再见千老板                                                                                                                 1
    in the wind and waves //@J思-ikun:有我们呢~                                                                                                         1
    Be strong inside yourself //@嗨我其实是大号:bye                                                                                                       1
    I'm making a stand, //@ByByBy-:哈                                                                                                               1
    心自由，生活就自由，到哪都有快乐                                                                                                                               1
    蔡徐坤，你的每一个笑颜，都是我无法忘怀的瞬间//@时间会沉淀答案:#东方风云榜让世界看见蔡徐坤# 祝千千🐶生幸福                                                                                       1
    啊啊啊啊啊#东方风云榜让世界看见蔡徐坤#//@22-二甲基丙烷:#蔡徐坤[超话]# 🌻#东方风云榜让世界看见蔡徐坤# 宠物医院的义工活动，展现了少年柔软的内心。@蔡徐坤 值得所有温柔相待.                                                 1
    你说用时间证明你对音乐的忠诚，我们一定会等你，等你实现自己的梦想。                                                                                                              1
    #东方风云榜让世界看见蔡徐坤# 千千啊                                                                                                                            1
    江山如画                                                                                                                                           1
    蔡徐坤，所求皆如愿，所行化坦途。@蔡徐坤                                                                                                                           1
    想念涌上来 安安静静看指环//@小心lq:再见千千[酸]带着大家对你的爱，健康成长哦[亲亲]@蔡徐坤                                                                                             1
    闭上双眼你却在徘徊//@小心lq:再见千千[酸]带着大家对你的爱，健康成长哦[亲亲]@蔡徐坤                                                                                                 1
    Name: raw_text, Length: 12679, dtype: int64




```python
fake_source = data_fake['source'].value_counts()[:10]
```


```python
bar = Bar("蔡徐坤假粉丝Top10转发设备", width = 600,height=600)
bar.add("", fake_source.index, fake_source.values, is_stack=True, 
       xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="0a96d6a74c02489b8c8f53d41624cbfd" style="width:600px;height:600px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_0a96d6a74c02489b8c8f53d41624cbfd = echarts.init(document.getElementById('0a96d6a74c02489b8c8f53d41624cbfd'), null, {renderer: 'canvas'});
var option_0a96d6a74c02489b8c8f53d41624cbfd = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u5047\u7c89\u4e1dTop10\u8f6c\u53d1\u8bbe\u5907",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 5263789,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "",
            "data": [
                65495.0,
                2823.0,
                2455.0,
                2354.0,
                2197.0,
                1458.0,
                1254.0,
                1225.0,
                1219.0,
                1166.0
            ],
            "stack": "stack_5263789",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 5263789
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 30,
                "margin": 8,
                "textStyle": {
                    "fontSize": 11,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "Android",
                "Flyme",
                "\u4e09\u661fGalaxy NOTE III",
                "\u4e09\u661fandroid\u667a\u80fd\u624b\u673a",
                "\u7ea2\u7c73Redmi",
                "vivo X20\u5168\u9762\u5c4f\u624b\u673a",
                "\u5c0f\u7c73\u624b\u673a",
                "\u8363\u8000\u624b\u673a \u52c7\u6562\u505a\u81ea\u5df1",
                "\u524d\u540e2000\u4e07 OPPO R11",
                "HUAWEI P10"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_0a96d6a74c02489b8c8f53d41624cbfd.setOption(option_0a96d6a74c02489b8c8f53d41624cbfd);

    });
</script>





```python
data_fake['user.follow_count'].mean()
```




    3.4412612555950397




```python
data_fake['user.followers_count'].mean()
```




    1.04576663836389




```python
data_fake_sample = data_fake.sample(5)
```


```python
data_fake_sample['user.screen_name']
```




    21846       蓬蓬坤8Bd528
    80516       蓝玫瑰jov890
    55689    用户6994230787
    37178      从不认输pmb498
    11486      纵骋横驰UcL978
    Name: user.screen_name, dtype: object




```python
data_fake_sample['user.profile_image_url'].values
```




    array(['https://tvax3.sinaimg.cn/crop.0.0.640.640.180/007ExdLSly8g0kfgzq276j30hs0hsq4h.jpg',
           'https://tvax2.sinaimg.cn/crop.0.0.640.640.180/007Ezlmqly8g0kbtdsc32j30ht0hsdha.jpg',
           'https://tvax2.sinaimg.cn/crop.0.0.200.200.180/007Dl4VZly8g04u0faipsj305k05kjrg.jpg',
           'https://tvax4.sinaimg.cn/crop.0.0.640.640.180/007EEc68ly8g0l9fjqh0xj30hs0hs0tr.jpg',
           'https://tvax2.sinaimg.cn/crop.79.0.188.188.180/007CtWGgly8fzqpzemlkzj309m058dfq.jpg'],
          dtype=object)




```python
data_fake.sample(5)['user.screen_name']
```




    9413       坤色坤香gxu584
    3347        慈祥纽_tdp10
    15825    用户6503593711
    28358       怀遇不n4D084
    96873      坤也可爱wuv340
    Name: user.screen_name, dtype: object




```python
data_fake['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
```




    41766




```python
data_fake.shape[0]
```




    95397




```python
data_fake['user.statuses_count'].mean()
```




    72.4942503433022



### 4. 真流量粉的粉丝画像


```python
data_true.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>attitudes_count</th>
      <th>comments_count</th>
      <th>reposts_count</th>
      <th>mid</th>
      <th>raw_text</th>
      <th>source</th>
      <th>user.description</th>
      <th>user.follow_count</th>
      <th>user.followers_count</th>
      <th>user.gender</th>
      <th>user.id</th>
      <th>user.mbrank</th>
      <th>user.mbtype</th>
      <th>user.profile_url</th>
      <th>user.profile_image_url</th>
      <th>user.screen_name</th>
      <th>user.statuses_count</th>
      <th>user.urank</th>
      <th>user.verified</th>
      <th>user.verified_reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>76048</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348565809642641</td>
      <td>#东方风云榜让世界看见蔡徐坤# 遇见你的那天，我就没想过要分开。@蔡徐坤</td>
      <td>HUAWEI Mate 10</td>
      <td>小号轮博，互粉呀，坤坤(◍ ´꒳` ◍)</td>
      <td>251</td>
      <td>291</td>
      <td>f</td>
      <td>6505180919</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6505180919?uid=6505180919</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>葵葵吃芒果冰呀</td>
      <td>13518</td>
      <td>19</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>68749</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348485031882927</td>
      <td>想你了</td>
      <td>Android</td>
      <td>我与你隔着长风深谷 近不得 退不舍 ​​</td>
      <td>291</td>
      <td>66</td>
      <td>f</td>
      <td>6093210679</td>
      <td>3</td>
      <td>12</td>
      <td>https://m.weibo.cn/u/6093210679?uid=6093210679</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>善良小菜最好命</td>
      <td>15986</td>
      <td>14</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2162</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4347997343648508</td>
      <td>转发微博</td>
      <td>vivo智能手机</td>
      <td></td>
      <td>655</td>
      <td>97</td>
      <td>f</td>
      <td>6253839509</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6253839509?uid=6253839509</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>蔡徐坤ikun24298586</td>
      <td>1280</td>
      <td>12</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>42740</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348419025500369</td>
      <td>@蔡徐坤 我永远支持你！我们一起拿下 #明星势力榜# 第一名！</td>
      <td>明星势力榜</td>
      <td></td>
      <td>555</td>
      <td>72</td>
      <td>f</td>
      <td>6575015283</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6575015283?uid=6575015283</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>女王范的成全16</td>
      <td>274</td>
      <td>9</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>77618</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348610940850719</td>
      <td>#东方风云榜让世界看见蔡徐坤#@蔡徐坤 我永远支持你！我们一起拿下 #明星势力榜# 第一名！</td>
      <td>明星势力榜</td>
      <td></td>
      <td>97</td>
      <td>33</td>
      <td>f</td>
      <td>5635145902</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/5635145902?uid=5635145902</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>坤坤的小咪喵</td>
      <td>2548</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_true_gender = data_true.drop_duplicates(subset='user.id')['user.gender'].value_counts()
data_true_gender
```




    f    3287
    m     639
    Name: user.gender, dtype: int64




```python
bar = Bar("蔡徐坤真粉丝性别比例", width = 600,height=500)
bar.add("(真粉丝总数为3926)", ['女', '男'], data_true_gender.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="4b6e47a3d1274a8b9b6e82d2633ad487" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_4b6e47a3d1274a8b9b6e82d2633ad487 = echarts.init(document.getElementById('4b6e47a3d1274a8b9b6e82d2633ad487'), null, {renderer: 'canvas'});
var option_4b6e47a3d1274a8b9b6e82d2633ad487 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u7c89\u4e1d\u6027\u522b\u6bd4\u4f8b",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 7058092,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "(\u771f\u7c89\u4e1d\u603b\u6570\u4e3a3926)",
            "data": [
                3287.0,
                639.0
            ],
            "stack": "stack_7058092",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 7058092
        }
    ],
    "legend": [
        {
            "data": [
                "(\u771f\u7c89\u4e1d\u603b\u6570\u4e3a3926)"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u5973",
                "\u7537"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_4b6e47a3d1274a8b9b6e82d2633ad487.setOption(option_4b6e47a3d1274a8b9b6e82d2633ad487);

    });
</script>





```python
data_true['raw_text'].value_counts()
```




    转发微博                                                                                                                                                                    1045
    @蔡徐坤 我永远支持你！我们一起拿下 #明星势力榜# 第一名！                                                                                                                                          622
    #东方风云榜让世界看见蔡徐坤#                                                                                                                                                           73
    @蔡徐坤  我在#明星ALL榜[超话]#上为你加油啦，你是我今生唯一的执著哦。#蔡徐坤[超话]# 棒棒哒！快来为TA应援吧                                                                                                             50
    //@蔡徐坤工作室:#蔡徐坤[超话]#[给你小心心]#蔡徐坤的未完成#之宠物医院终于步入尾声，在短暂的相处时间里，因为工作忙碌无法养育小动物的@蔡徐坤 也获得了片刻的慰藉，感谢千千给我们带来了一段难忘的回忆[心]#蔡徐坤 ONE#                                                       42
    #东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# [太开心]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                       38
    //@万俟可儿IKun:0310，打卡//@CXK-FANSCLUB4:#蔡徐坤[超话]#｜#东方风云榜让世界看见蔡徐坤# 千千要乖哦@蔡徐坤                                                                                                   25
    蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk//@旋转的木马没有翅膀:再见千千，带着大家对你的爱，健康成长哦[亲亲]@蔡徐坤                                                                                                     23
    蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk//@旋转的木马没有翅膀:再见千千，带着大家对你的爱，健康成长哦[亲亲]@蔡徐坤              23
    #东方风云榜让世界看见蔡徐坤# [可爱]#蔡徐坤的未完成# [亲亲]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                       21
    [微笑]//@万俟可儿IKun:0310，打卡//@CXK-FANSCLUB4:#蔡徐坤[超话]#｜#东方风云榜让世界看见蔡徐坤# 千千要乖哦@蔡徐坤                                                                                               21
    #东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# [可爱]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                        21
    #东方风云榜让世界看见蔡徐坤# [可爱]#蔡徐坤的未完成# [心]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                        20
    #东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# [亲亲]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                        20
    #东方风云榜让世界看见蔡徐坤# //@Unity_蔡徐坤初心站:#蔡徐坤[超话]#|#东方风云榜让世界看见蔡徐坤# 有缘下次再见@蔡徐坤                                                                                                      19
    #东方风云榜让世界看见蔡徐坤# [可爱]#蔡徐坤的未完成# [太开心]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                      19
    轉發微博                                                                                                                                                                      19
    //@ikun涵宝0802:#东方风云榜让世界看见蔡徐坤# 加油[拳头]//@蔡徐坤正宫后援会:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千一定要健康的成长哦[心][心][心]@蔡徐坤                                                                     18
    蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk//@旋转的木马没有翅膀:再见千千，带      18
    //@蔡蔡的小猪猪:#东方风云榜让世界看见蔡徐坤# [笑而不语]#蔡徐坤的未完成# 千千会想你的@CXK-FANSCLUB2:千千要乖哦                                                                                                      17
    蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk//@旋转的木马没有翅膀:再见千千，带着大家对你的爱，健康成长哦[亲亲]@蔡徐坤                                           17
    #东方风云榜让世界看见蔡徐坤#希望每个小动物都能有一个温暖的家！#东方风云榜让世界看见蔡徐坤#希望每个小动物都能有一个温暖的家！                                                                                                          16
    #东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# [笑哈哈]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                       16
    蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk蔡徐坤舞台 cxk 蔡徐坤正能量偶像 蔡徐坤新歌好听cxk//@旋转的木马没有翅膀:再见千千，带着大家对你的爱，健康成长哦[亲亲]@蔡徐坤                                                                        15
    //@蔡徐坤粉丝团官微:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千要健康成长噢 @蔡徐坤                                                                                                                    14
    我们蔡徐坤宝贝//@竹林涓涓:#东方风云榜让世界看见蔡徐坤#  新家要好好适应啊千千                                                                                                                                13
    #东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# [憧憬]//@August-小漂亮的万花筒:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 哈哈哈哈哈哈，宝贝让千千转圈圈太可爱了[笑哈哈][笑哈哈][笑哈哈]                                                        12
    #蔡徐坤的未完成# //@Unity_蔡徐坤初心站:#蔡徐坤[超话]#|#东方风云榜让世界看见蔡徐坤# 有缘下次再见@蔡徐坤                                                                                                            12
    @蔡徐坤                                                                                                                                                                      12
    Repost                                                                                                                                                                    12
                                                                                                                                                                            ... 
    38//@坤的lxy:来了//@蔡徐坤正宫后援会:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千一定要健康的成长哦[心][心][心]@蔡徐坤                                                                                             1
    51#蔡徐坤[超话]#[心]#东方风云榜让世界看见蔡徐坤#   用心去爱，回忆满满@蔡徐坤                                                                                                                              1
    许多良辰美景，要和你一个一个去耽误。[爱你][爱你][爱你]@蔡徐坤                                                                                                                                         1
    #东方风云榜让世界看见蔡徐坤# 蔡徐坤 cxk 只因你太美好令我无法坦白说出我爱你@蔡徐坤//@看黑子多跳脚就知道蔡徐坤有多火:#东方风云榜让世界看见蔡徐坤# 千千 要乖乖的哦[亲亲][亲亲][亲亲] 哥哥好温柔哦 嘻嘻嘻[污][污]@蔡徐坤                                                  1
    斜阳草树                                                                                                                                                                       1
    蔡徐坤 谢谢你坚持这份沉甸甸的热爱，谢谢你坚持这从未做完的梦。因为你，我们会感恩，会珍惜，会成长。因为你，我们会变得有担当，会继续善良。@蔡徐坤                                                                                                   1
    加油@蔡徐坤                                                                                                                                                                     1
    32//@CXK-FANSCLUB2:千千要乖哦                                                                                                                                                   1
    总想把世界上最好的都给你，却发现世界最好的就是你@蔡徐坤                                                                                                                                               1
    #东方风云榜让世界看见蔡徐坤# 许你金海一片一片   @蔡徐坤                                                                                                                                            1
    #东方风云榜让世界看见蔡徐坤#[太开心]#蔡徐坤的未完成# 坤坤蔡徐坤 花花世界，世俗纷扰，忧愁烦恼都一笔勾销，天地之间任你逍遥20@蔡徐坤                                                                                                     1
    [偷乐]//@shelly6476767612:千千要乖哦                                                                                                                                              1
    #东方风云榜让世界看见蔡徐坤# 蔡徐坤 我喜欢你不是一见钟情也不能说停就停@蔡徐坤                                                                                                                                  1
    万物平等                                                                                                                                                                       1
    我是千千[坏笑]                                                                                                                                                                   1
    你是风儿我是沙你是哈密我是瓜你是牙膏我是刷，你不爱我我自杀[熊猫]@蔡徐坤                                                                                                                                      1
    我好想你啊，晚安[月亮]                                                                                                                                                               1
    29//@小困ikun啊://@蔡徐坤正宫后援会:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千一定要健康的成长哦[心][心][心]@蔡徐坤                                                                                             1
    他听不懂[笑cry][笑cry]#东方风云榜让世界看见蔡徐坤#                                                                                                                                            1
    千千好可爱 坤哥更可爱呀                                                                                                                                                               1
    跟可爱的千千说再见，温柔的蔡医生愿你再次出现！                                                                                                                                                    1
    We go party //@嗨我其实是大号:bye                                                                                                                                                 1
    #东方风云榜让世界看见蔡徐坤#  清新的空气，快乐的气味，透过空气射入你的灵魂里，将阳光呼吸，将幸福抱起，泡一杯甜美的咖啡，品尝幸福的意义，接受祝福的信息，祝你晨安温馨无比!                                                                                    1
    I love you//@蔡徐坤的小九九呀:哥哥要照顾好自己啊@蔡徐坤                                                                                                                                        1
    喜欢你的人很多，不缺我一个；但我爱的人很少，只有你@蔡徐坤 一个!快来为TA应援吧 #东方风云榜让世界看见蔡徐坤#                                                                                                                  1
    #东方风云榜让世界看见蔡徐坤# 宝宝我好想你啊                                                                                                                                                    1
    #东方风云榜让世界看见蔡徐坤# 棒棒棒坤坤                                                                                                                                                      1
    #东方风云榜让世界看见蔡徐坤# [微笑]#蔡徐坤的未完成# 希望蔡徐坤一直勇敢，而我们会一直保护他。@蔡徐坤                                                                                                                     1
    蔡徐坤 走在路上， 总是幻想， 只要一抬头，便能看到你。 @蔡徐坤                                                                                                                                          1
    #东方风云榜让世界看见蔡徐坤# 晚安 我睡觉啦 你也要好好休息喔 明天要早起啦 又是每天要早起的一周[跪了]                                                                                                                     1
    Name: raw_text, Length: 3738, dtype: int64




```python
true_source = data_true['source'].value_counts()[:10]
```


```python
bar = Bar("蔡徐坤真粉丝Top10转发设备", width = 600,height=600)
bar.add("", true_source.index, true_source.values, is_stack=True, 
       xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
bar
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min'
        }
    });
</script>
    <div id="3a6ee7b6de034aef82d7cf8404adf62f" style="width:600px;height:600px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_3a6ee7b6de034aef82d7cf8404adf62f = echarts.init(document.getElementById('3a6ee7b6de034aef82d7cf8404adf62f'), null, {renderer: 'canvas'});
var option_3a6ee7b6de034aef82d7cf8404adf62f = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u7c89\u4e1dTop10\u8f6c\u53d1\u8bbe\u5907",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 7265617,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "name": "",
            "data": [
                840.0,
                712.0,
                654.0,
                334.0,
                316.0,
                297.0,
                188.0,
                169.0,
                158.0,
                143.0
            ],
            "stack": "stack_7265617",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": []
            },
            "markLine": {
                "data": []
            },
            "seriesId": 7265617
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 30,
                "margin": 8,
                "textStyle": {
                    "fontSize": 11,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "iPhone\u5ba2\u6237\u7aef",
                "Android",
                "\u660e\u661f\u52bf\u529b\u699c",
                "vivo\u667a\u80fd\u624b\u673a",
                "vivo X23\u5168\u606f\u5e7b\u5f69",
                "OPPO\u667a\u80fd\u624b\u673a",
                "vivo X23 AI\u975e\u51e1\u6444\u5f71",
                "\u5c0f\u7c73\u624b\u673a4",
                "\u7ea2\u7c73Redmi",
                "Android\u5ba2\u6237\u7aef"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 14,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "splitLine": {
                "show": true
            },
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_3a6ee7b6de034aef82d7cf8404adf62f.setOption(option_3a6ee7b6de034aef82d7cf8404adf62f);

    });
</script>





```python
data_true['user.follow_count'].mean()
```




    222.0597165991903




```python
data_true['user.followers_count'].mean()
```




    178.9480913823019




```python
data_true.sample(5)['user.screen_name']
```




    90060    complemehtht_16690
    51426                 82号甜七
    75569             August菜包包
    33191           薄荷般的夏天_你的时代
    92003          Amygirl_P的坤坤
    Name: user.screen_name, dtype: object




```python
data_true['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
```




    3153




```python
data_true.shape[0]
```




    6916




```python
# 绘制蔡徐坤真粉丝的简介词云图
import jieba
from collections import Counter
from pyecharts import WordCloud

jieba.add_word('蔡徐坤')

swords = [x.strip() for x in open ('stopwords.txt')]
```

    Building prefix dict from the default dictionary ...
    Dumping model to file cache /var/folders/mc/k6p_zt453w770h63024z__vw0000gn/T/jieba.cache
    Loading model cost 1.634 seconds.
    Prefix dict has been built succesfully.
    


```python
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
```


```python
plot_word_cloud(data=data_true, swords=swords, columns='user.description')
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min', 'wordcloud': '/nbextensions/echarts/echarts-wordcloud.min'
        }
    });
</script>
    <div id="d3d393895bf740e5b8fffc9b68016313" style="width:1300px;height:620px;"></div>


<script>
    require(['echarts', 'wordcloud'], function(echarts) {

var myChart_d3d393895bf740e5b8fffc9b68016313 = echarts.init(document.getElementById('d3d393895bf740e5b8fffc9b68016313'), null, {renderer: 'canvas'});
var option_d3d393895bf740e5b8fffc9b68016313 = {
    "title": [
        {
            "text": "",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 7481583,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "wordCloud",
            "name": "",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                20,
                100
            ],
            "data": [
                {
                    "name": "\u8521\u5f90\u5764",
                    "value": 1088,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,42,14)"
                        }
                    }
                },
                {
                    "name": "ikun",
                    "value": 352,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,43,152)"
                        }
                    }
                },
                {
                    "name": "KUN",
                    "value": 242,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,9,130)"
                        }
                    }
                },
                {
                    "name": "amp",
                    "value": 224,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,87,135)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u53f7",
                    "value": 199,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,150,118)"
                        }
                    }
                },
                {
                    "name": "\u82b1\u82b1\u4e16\u754c",
                    "value": 191,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,20,114)"
                        }
                    }
                },
                {
                    "name": "\u559c\u6b22",
                    "value": 180,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,44,15)"
                        }
                    }
                },
                {
                    "name": "IKUN",
                    "value": 171,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,108,94)"
                        }
                    }
                },
                {
                    "name": "\u552f\u5764",
                    "value": 147,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,16,5)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765",
                    "value": 137,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,96,140)"
                        }
                    }
                },
                {
                    "name": "kun",
                    "value": 130,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,6,8)"
                        }
                    }
                },
                {
                    "name": "Ikun",
                    "value": 129,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,160,43)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b88\u5df1",
                    "value": 127,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,147,141)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u822a",
                    "value": 103,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,70,60)"
                        }
                    }
                },
                {
                    "name": "\u4f34\u5764",
                    "value": 101,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,23,137)"
                        }
                    }
                },
                {
                    "name": "\u52aa\u529b",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,1,1)"
                        }
                    }
                },
                {
                    "name": "\u62ab\u91d1\u6210",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,123,35)"
                        }
                    }
                },
                {
                    "name": "\u68a6\u60f3",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,119,133)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,104,24)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8fdc",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,30,97)"
                        }
                    }
                },
                {
                    "name": "\u8f6e\u535a",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,12,24)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u56de",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,50,158)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,76,19)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u7c89",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,74,87)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,34,41)"
                        }
                    }
                },
                {
                    "name": "for",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,22,1)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u661f",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,84,146)"
                        }
                    }
                },
                {
                    "name": "\u83dc\u83dc",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,64,16)"
                        }
                    }
                },
                {
                    "name": "Kun",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,41,127)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,147,138)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5764",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,70,20)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b88",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,122,157)"
                        }
                    }
                },
                {
                    "name": "cp",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,144,99)"
                        }
                    }
                },
                {
                    "name": "\u5149\u8292",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,130,115)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u68a6",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,89,90)"
                        }
                    }
                },
                {
                    "name": "\u7b3c\u7f69",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,30,92)"
                        }
                    }
                },
                {
                    "name": "\u7ec8\u4f1a",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,67,69)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u8d77",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,49,4)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,29,27)"
                        }
                    }
                },
                {
                    "name": "\u5df2\u5fc3",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,140,19)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5764",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,157,98)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8a00",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,44,142)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9700",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,52,85)"
                        }
                    }
                },
                {
                    "name": "\u60a0\u60a0",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,63,100)"
                        }
                    }
                },
                {
                    "name": "\u4e4b\u53e3",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,12,79)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u751f",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,100,145)"
                        }
                    }
                },
                {
                    "name": "\u6d6e\u534e",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,88,123)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5764\u5764",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,100,48)"
                        }
                    }
                },
                {
                    "name": "\u65d7\u4e0b",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,122,46)"
                        }
                    }
                },
                {
                    "name": "\u7b11\u8c08",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,85,142)"
                        }
                    }
                },
                {
                    "name": "is",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,148,70)"
                        }
                    }
                },
                {
                    "name": "cxk",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,105,98)"
                        }
                    }
                },
                {
                    "name": "\u731c\u731c",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,78,88)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,11,20)"
                        }
                    }
                },
                {
                    "name": "\u5931\u7720",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,151,92)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u679a",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,41,35)"
                        }
                    }
                },
                {
                    "name": "\u9047\u89c1",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,160,49)"
                        }
                    }
                },
                {
                    "name": "\u827a\u4eba",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,65,1)"
                        }
                    }
                },
                {
                    "name": "you",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,98,91)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u8def",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,91,156)"
                        }
                    }
                },
                {
                    "name": "\u552f\u7231\u5764",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,27,131)"
                        }
                    }
                },
                {
                    "name": "\u604b\u7231",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,42,9)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,78,147)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u7231",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,143,49)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,33,157)"
                        }
                    }
                },
                {
                    "name": "the",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,119,33)"
                        }
                    }
                },
                {
                    "name": "\u53ea\u4e3a",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,96,78)"
                        }
                    }
                },
                {
                    "name": "\u8521\u5148\u751f",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,51,16)"
                        }
                    }
                },
                {
                    "name": "be",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,125,52)"
                        }
                    }
                },
                {
                    "name": "\u6210\u5458",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,157,107)"
                        }
                    }
                },
                {
                    "name": "\u5e78\u8fd0",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,57,145)"
                        }
                    }
                },
                {
                    "name": "my",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,116,83)"
                        }
                    }
                },
                {
                    "name": "ONLY",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,2,102)"
                        }
                    }
                },
                {
                    "name": "\u966a\u4f60\u8d70",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,136,41)"
                        }
                    }
                },
                {
                    "name": "\u552f\u7c89",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,72,158)"
                        }
                    }
                },
                {
                    "name": "your",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,113,86)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7c89",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,78,78)"
                        }
                    }
                },
                {
                    "name": "\u5343\u519b\u4e07\u9a6c",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,12,77)"
                        }
                    }
                },
                {
                    "name": "will",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,19,34)"
                        }
                    }
                },
                {
                    "name": "\u6218\u6597",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,34,98)"
                        }
                    }
                },
                {
                    "name": "need",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,111,40)"
                        }
                    }
                },
                {
                    "name": "\u5b88\u62a4",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,135,139)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u7ebf",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,118,46)"
                        }
                    }
                },
                {
                    "name": "\u7ec4\u5408",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,108,98)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u8d1d",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,125,10)"
                        }
                    }
                },
                {
                    "name": "me",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,154,12)"
                        }
                    }
                },
                {
                    "name": "\u6211\u4f1a",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,104,46)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u5fc3",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,58,87)"
                        }
                    }
                },
                {
                    "name": "\u59d0\u59d0",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,156,126)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,93,13)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,159,151)"
                        }
                    }
                },
                {
                    "name": "\u5e0c\u671b",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,69,111)"
                        }
                    }
                },
                {
                    "name": "\u5f88\u751c",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,121,41)"
                        }
                    }
                },
                {
                    "name": "FOR",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,96,104)"
                        }
                    }
                },
                {
                    "name": "\u5f88\u7d2f",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,151,25)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u732b\u54aa",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,72,143)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u9047",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,51,41)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u8d1f",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,122,112)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50\u5708",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,21,59)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,115,129)"
                        }
                    }
                }
            ]
        }
    ],
    "legend": [
        {
            "data": [],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_d3d393895bf740e5b8fffc9b68016313.setOption(option_d3d393895bf740e5b8fffc9b68016313);

    });
</script>





```python
plot_word_cloud(data=data_true, swords=swords, columns='raw_text')
```




<script>
    require.config({
        paths: {
            'echarts': '/nbextensions/echarts/echarts.min', 'wordcloud': '/nbextensions/echarts/echarts-wordcloud.min'
        }
    });
</script>
    <div id="2992f2c2a05c4e86a9ef6c32287b9457" style="width:1300px;height:620px;"></div>


<script>
    require(['echarts', 'wordcloud'], function(echarts) {

var myChart_2992f2c2a05c4e86a9ef6c32287b9457 = echarts.init(document.getElementById('2992f2c2a05c4e86a9ef6c32287b9457'), null, {renderer: 'canvas'});
var option_2992f2c2a05c4e86a9ef6c32287b9457 = {
    "title": [
        {
            "text": "",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 8066295,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "wordCloud",
            "name": "",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                20,
                100
            ],
            "data": [
                {
                    "name": "\u8521\u5f90\u5764",
                    "value": 12685,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,159,118)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c",
                    "value": 4141,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,61,67)"
                        }
                    }
                },
                {
                    "name": "\u770b\u89c1",
                    "value": 4072,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,80,37)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9",
                    "value": 4058,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,3,114)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u4e91\u699c",
                    "value": 4057,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,4,111)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5343",
                    "value": 2065,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,24,89)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210",
                    "value": 1607,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,128,40)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u53d1",
                    "value": 1081,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,35,51)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a",
                    "value": 1032,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,97,58)"
                        }
                    }
                },
                {
                    "name": "\u7b11\u54c8\u54c8",
                    "value": 808,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,136,110)"
                        }
                    }
                },
                {
                    "name": "\u518d\u89c1",
                    "value": 740,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,86,49)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f",
                    "value": 719,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,8,45)"
                        }
                    }
                },
                {
                    "name": "cxk",
                    "value": 714,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,85,114)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u8d77",
                    "value": 704,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,49,67)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8fdc",
                    "value": 694,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,65,63)"
                        }
                    }
                },
                {
                    "name": "\u652f\u6301",
                    "value": 665,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,13,6)"
                        }
                    }
                },
                {
                    "name": "\u62ff\u4e0b",
                    "value": 658,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,28,29)"
                        }
                    }
                },
                {
                    "name": "\u7b2c\u4e00\u540d",
                    "value": 658,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,39,112)"
                        }
                    }
                },
                {
                    "name": "\u52bf\u529b",
                    "value": 658,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,77,95)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u7231",
                    "value": 594,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,54,104)"
                        }
                    }
                },
                {
                    "name": "\u54c8\u54c8\u54c8",
                    "value": 570,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,122,25)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u8bdd",
                    "value": 548,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,141,106)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7",
                    "value": 472,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,140,9)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f",
                    "value": 465,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,74,53)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5b9a",
                    "value": 437,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,140,110)"
                        }
                    }
                },
                {
                    "name": "\u540e\u63f4\u4f1a",
                    "value": 433,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,32,54)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u4eb2",
                    "value": 423,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,0,151)"
                        }
                    }
                },
                {
                    "name": "\u6e29\u6696",
                    "value": 417,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,84,113)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u8d1d",
                    "value": 395,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,92,66)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5bab",
                    "value": 394,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,63,143)"
                        }
                    }
                },
                {
                    "name": "\u5e0c\u671b",
                    "value": 382,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,156,84)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0",
                    "value": 348,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,0,160)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u91cf",
                    "value": 344,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,125,153)"
                        }
                    }
                },
                {
                    "name": "\u5076\u50cf",
                    "value": 312,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,39,86)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u7269",
                    "value": 311,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,47,69)"
                        }
                    }
                },
                {
                    "name": "\u597d\u542c",
                    "value": 303,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,71,11)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u6210\u957f",
                    "value": 270,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,35,103)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u5708\u5708",
                    "value": 269,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,30,124)"
                        }
                    }
                },
                {
                    "name": "August",
                    "value": 264,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,123,11)"
                        }
                    }
                },
                {
                    "name": "\u6f02\u4eae",
                    "value": 256,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,14,134)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u82b1\u7b52",
                    "value": 256,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,101,135)"
                        }
                    }
                },
                {
                    "name": "\u559c\u6b22",
                    "value": 251,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,69,12)"
                        }
                    }
                },
                {
                    "name": "ikun",
                    "value": 231,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,50,147)"
                        }
                    }
                },
                {
                    "name": "\u54e5\u54e5",
                    "value": 220,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,63,89)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u5fc3",
                    "value": 211,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,37,112)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5fc3",
                    "value": 206,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,29,81)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u6cb9",
                    "value": 196,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,138,14)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u7c89",
                    "value": 180,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,17,81)"
                        }
                    }
                },
                {
                    "name": "\u6e29\u67d4",
                    "value": 171,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,130,128)"
                        }
                    }
                },
                {
                    "name": "CXK",
                    "value": 167,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,54,12)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u4e2a",
                    "value": 148,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,69,98)"
                        }
                    }
                },
                {
                    "name": "\u665a\u5b89",
                    "value": 143,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,135,76)"
                        }
                    }
                },
                {
                    "name": "\u7f9e\u55d2",
                    "value": 141,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,107,53)"
                        }
                    }
                },
                {
                    "name": "AK47",
                    "value": 134,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,11,96)"
                        }
                    }
                },
                {
                    "name": "\u597d\u597d",
                    "value": 118,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,132,51)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u5947",
                    "value": 116,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,92,74)"
                        }
                    }
                },
                {
                    "name": "\u521d\u5fc3",
                    "value": 111,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,45,118)"
                        }
                    }
                },
                {
                    "name": "\u52aa\u529b",
                    "value": 108,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,46,20)"
                        }
                    }
                },
                {
                    "name": "\u7fc5\u8180",
                    "value": 104,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,35,92)"
                        }
                    }
                },
                {
                    "name": "KUN",
                    "value": 104,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,114,57)"
                        }
                    }
                },
                {
                    "name": "\u6728\u9a6c",
                    "value": 103,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,45,113)"
                        }
                    }
                },
                {
                    "name": "\u65cb\u8f6c",
                    "value": 103,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,73,8)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,11,34)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u6b21",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,156,117)"
                        }
                    }
                },
                {
                    "name": "\u5ba0\u7269\u533b\u9662",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,144,82)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7f18",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,111,149)"
                        }
                    }
                },
                {
                    "name": "Unity",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,38,86)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5fc6",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,144,114)"
                        }
                    }
                },
                {
                    "name": "FANSCLUB2",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,22,141)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,159,92)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u6765",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,41,147)"
                        }
                    }
                },
                {
                    "name": "\u611f\u8c22",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,135,131)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u6cd5",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,15,102)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u6682",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,140,51)"
                        }
                    }
                },
                {
                    "name": "\u7ec8\u4e8e",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,68,72)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,96,34)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5904",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,155,24)"
                        }
                    }
                },
                {
                    "name": "\u96be\u5fd8",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,2,48)"
                        }
                    }
                },
                {
                    "name": "ONE",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,11,107)"
                        }
                    }
                },
                {
                    "name": "BIUBIUBIUBIU",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,136,23)"
                        }
                    }
                },
                {
                    "name": "\u9c9c\u82b1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,127,40)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u6bb5",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,13,41)"
                        }
                    }
                },
                {
                    "name": "\u7247\u523b",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,54,96)"
                        }
                    }
                },
                {
                    "name": "##",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,29,145)"
                        }
                    }
                },
                {
                    "name": "\u5fd9\u788c",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,141,0)"
                        }
                    }
                },
                {
                    "name": "\u83b7\u5f97",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,6,2)"
                        }
                    }
                },
                {
                    "name": "\u5973\u5b69\u513f",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,117,116)"
                        }
                    }
                },
                {
                    "name": "\u563b\u563b",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,1,47)"
                        }
                    }
                },
                {
                    "name": "\u517b\u80b2",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,61,127)"
                        }
                    }
                },
                {
                    "name": "\u6170\u85c9",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,88,16)"
                        }
                    }
                },
                {
                    "name": "\u5c3e\u58f0",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,80,128)"
                        }
                    }
                },
                {
                    "name": "\u6b65\u5165",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,150,111)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u7b11",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,79,77)"
                        }
                    }
                },
                {
                    "name": "\u751c\u8475",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,35,44)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u5ba4",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,28,141)"
                        }
                    }
                },
                {
                    "name": "\u8bb0\u5f97",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,8,122)"
                        }
                    }
                },
                {
                    "name": "\u6bd4\u5fc3",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,82,112)"
                        }
                    }
                },
                {
                    "name": "\u5154\u5b50",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,120,118)"
                        }
                    }
                },
                {
                    "name": "\u65e9\u5b89",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,34,91)"
                        }
                    }
                },
                {
                    "name": "kun",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,128,21)"
                        }
                    }
                }
            ]
        }
    ],
    "legend": [
        {
            "data": [],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart_2992f2c2a05c4e86a9ef6c32287b9457.setOption(option_2992f2c2a05c4e86a9ef6c32287b9457);

    });
</script>



