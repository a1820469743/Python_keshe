# Python_keshe
蔡徐坤课设
```python
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
%matplotlib inline
```


```python

```


```python
data =pd.read_csv('D://caixukun.csv', delimiter=';', encoding='utf8', names=['attitudes_count', 'comments_count', 'reposts_count', 'mid', 'raw_text',
          'source', 'user.description', 'user.follow_count', 'user.followers_count',
          'user.gender', 'user.id', 'user.mbrank', 'user.mbtype', 'user.profile_url',
          'user.profile_image_url', 'user.screen_name', 'user.statuses_count',
          'user.urank', 'user.verified', 'user.verified_reason'])
```


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 102316 entries, 0 to 102315
    Data columns (total 20 columns):
     #   Column                  Non-Null Count   Dtype  
    ---  ------                  --------------   -----  
     0   attitudes_count         102316 non-null  object 
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
      <th>82794</th>
      <td>0,0,0,4.34863E+15,e ora che non ci sei è il vu...</td>
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
      <th>32453</th>
      <td>0,0,0,4.34838E+15,#东方风云榜让世界看见蔡徐坤#I'd stop if I...</td>
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
      <th>39610</th>
      <td>0,0,0,4.3484E+15,“kun&amp;amp,"ikun永远是一起的，我不在单枪匹马因...</td>
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
      <th>87088</th>
      <td>0,0,0,4.34863E+15,"sorsi per vivere tra le tue...</td>
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
      <th>1032</th>
      <td>0,0,0,4.34804E+15,花花世界，静守己心，千军万马，不惧流言,Android,...</td>
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
</div>



#### 1. 数据清洗
由于数据入库的时候没有进行清洗，所以数据多出了很多没用的字段，需要先清洗掉


```python
data.columns
```




    Index(['attitudes_count', 'comments_count', 'reposts_count', 'mid', 'raw_text',
           'source', 'user.description', 'user.follow_count',
           'user.followers_count', 'user.gender', 'user.id', 'user.mbrank',
           'user.mbtype', 'user.profile_url', 'user.profile_image_url',
           'user.screen_name', 'user.statuses_count', 'user.urank',
           'user.verified', 'user.verified_reason'],
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


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 102316 entries, 0 to 102315
    Data columns (total 20 columns):
     #   Column                  Non-Null Count   Dtype  
    ---  ------                  --------------   -----  
     0   attitudes_count         102316 non-null  object 
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




    Series([], Name: user.gender, dtype: int64)




```python
from pyecharts import Bar

bar = Bar("蔡徐坤粉丝性别比例初探", width = 600,height=500)
bar.add("(总数据102313条)", ['男', '女'], fans_num.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-32-89dc0b7f0230> in <module>
    ----> 1 from pyecharts import Bar
          2 
          3 bar = Bar("蔡徐坤粉丝性别比例初探", width = 600,height=500)
          4 bar.add("(总数据102313条)", ['男', '女'], fans_num.values, is_stack=True, 
          5        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
    

    ImportError: cannot import name 'Bar' from 'pyecharts' (d:\python\lib\site-packages\pyecharts\__init__.py)



```python
np.round(fans_num/fans_num.sum()*100, 2)
```




    Series([], Name: user.gender, dtype: float64)




```python
data[data['user.gender']=='m'].sample(5)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-34-000e21aa3fe9> in <module>
    ----> 1 data[data['user.gender']=='m'].sample(5)
    

    d:\python\lib\site-packages\pandas\core\generic.py in sample(self, n, frac, replace, weights, random_state, axis)
       4993             )
       4994 
    -> 4995         locs = rs.choice(axis_length, size=n, replace=replace, p=weights)
       4996         return self.take(locs, axis=axis)
       4997 
    

    mtrand.pyx in numpy.random.mtrand.RandomState.choice()
    

    ValueError: a must be greater than 0 unless no samples are taken


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


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-35-d1a9f9ca80eb> in <module>
          5                 (data['reposts_count']==0)&
          6                 (data['user.mbrank']==0)]
    ----> 7 data_fake.sample(5)
    

    d:\python\lib\site-packages\pandas\core\generic.py in sample(self, n, frac, replace, weights, random_state, axis)
       4993             )
       4994 
    -> 4995         locs = rs.choice(axis_length, size=n, replace=replace, p=weights)
       4996         return self.take(locs, axis=axis)
       4997 
    

    mtrand.pyx in numpy.random.mtrand.RandomState.choice()
    

    ValueError: a must be greater than 0 unless no samples are taken



```python
data_fake.shape
```




    (0, 20)




```python
# 昵称里包含“用户”的，基本上可以断定是假粉丝
data_fake2_index = data[(data['user.follow_count']>5)&
                        (data['user.followers_count']>5)&
                        (data['user.screen_name'].str.contains('用户'))].index
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-37-5d67f39a2e02> in <module>
          2 data_fake2_index = data[(data['user.follow_count']>5)&
          3                         (data['user.followers_count']>5)&
    ----> 4                         (data['user.screen_name'].str.contains('用户'))].index
    

    d:\python\lib\site-packages\pandas\core\generic.py in __getattr__(self, name)
       5135             or name in self._accessors
       5136         ):
    -> 5137             return object.__getattribute__(self, name)
       5138         else:
       5139             if self._info_axis._can_hold_identifiers_and_holds_name(name):
    

    d:\python\lib\site-packages\pandas\core\accessor.py in __get__(self, obj, cls)
        185             # we're accessing the attribute of the class, i.e., Dataset.geo
        186             return self._accessor
    --> 187         accessor_obj = self._accessor(obj)
        188         # Replace the property with the accessor object. Inspired by:
        189         # https://www.pydanny.com/cached-property.html
    

    d:\python\lib\site-packages\pandas\core\strings.py in __init__(self, data)
       2098 
       2099     def __init__(self, data):
    -> 2100         self._inferred_dtype = self._validate(data)
       2101         self._is_categorical = is_categorical_dtype(data.dtype)
       2102         self._is_string = data.dtype.name == "string"
    

    d:\python\lib\site-packages\pandas\core\strings.py in _validate(data)
       2155 
       2156         if inferred_dtype not in allowed_types:
    -> 2157             raise AttributeError("Can only use .str accessor with string values!")
       2158         return inferred_dtype
       2159 
    

    AttributeError: Can only use .str accessor with string values!



```python
# 把假的流量粉丝转发组合起来
data_fake = pd.concat([data_fake, data.iloc[data_fake2_index]])
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-38-c47c8ac32c41> in <module>
          1 # 把假的流量粉丝转发组合起来
    ----> 2 data_fake = pd.concat([data_fake, data.iloc[data_fake2_index]])
    

    NameError: name 'data_fake2_index' is not defined



```python
data_fake.shape
```




    (0, 20)




```python
# 取出真粉的转发
data_true = data.drop(data_fake.index)
```


```python
data_true.shape
```




    (102316, 20)




```python
print('真粉丝转发数占总转发数的{}%'.format(np.round(data_true.shape[0]/data.shape[0]*100, 2)))
print('假粉丝转发数占总转发数的{}%'.format(np.round(data_fake.shape[0]/data.shape[0]*100, 2)))
```

    真粉丝转发数占总转发数的100.0%
    假粉丝转发数占总转发数的0.0%
    


```python
bar = Bar("蔡徐坤真假流量的转发量", width = 600,height=500)
bar.add("(总数据102313条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
        [data.shape[0], data_fake.shape[0], data_true.shape[0]], is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-43-65c8f4b3a535> in <module>
    ----> 1 bar = Bar("蔡徐坤真假流量的转发量", width = 600,height=500)
          2 bar.add("(总数据102313条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
          3         [data.shape[0], data_fake.shape[0], data_true.shape[0]], is_stack=True,
          4        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
          5 bar
    

    NameError: name 'Bar' is not defined



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


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-45-861b5566d29b> in <module>
    ----> 1 bar = Bar("蔡徐坤真假流量的转发量与真实转发粉丝量(总数据102313条)", width = 600,height=500)
          2 bar.add('', ['总转发量', '假粉丝转发量', '真粉丝转发量', '真实转发粉丝量'], 
          3         [data.shape[0], data_fake.shape[0], data_true.shape[0], real_fans_num], is_stack=True,
          4        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=20)
          5 bar
    

    NameError: name 'Bar' is not defined



```python
print('真实转发粉丝量占总转发数的{}%'.format(np.round(real_fans_num/data.shape[0]*100, 2)))
```

    真实转发粉丝量占总转发数的0.0%
    

-----------------吴青峰微博数据做对比-----------------


```python
db = conn.get_database('WuQingFeng')  # WuQingFeng

repost = db.get_collection('repost') # repost
mon_data = repost.find()  # 查询这个集合下的所有记录
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-47-f913020aa4b1> in <module>
    ----> 1 db = conn.get_database('WuQingFeng')  # WuQingFeng
          2 
          3 repost = db.get_collection('repost') # repost
          4 mon_data = repost.find()  # 查询这个集合下的所有记录
    

    NameError: name 'conn' is not defined



```python
wqf_data = json_normalize([comment for comment in mon_data])
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-48-ca9a1d4293d1> in <module>
    ----> 1 wqf_data = json_normalize([comment for comment in mon_data])
    

    NameError: name 'mon_data' is not defined



```python
wqf_data = wqf_data[in_columns]
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-49-5ccba96381d3> in <module>
    ----> 1 wqf_data = wqf_data[in_columns]
    

    NameError: name 'wqf_data' is not defined



```python
wqf_data.shape
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-50-03e31aebb7d3> in <module>
    ----> 1 wqf_data.shape
    

    NameError: name 'wqf_data' is not defined



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


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-51-0bd107acec71> in <module>
    ----> 1 wqf_data_fake = wqf_data[((wqf_data['user.follow_count']<=5)|(wqf_data['user.followers_count']<=5))&
          2                          (wqf_data['user.description']=='')&
          3                          (wqf_data['comments_count']==0)&
          4                          (wqf_data['attitudes_count']==0)&
          5                          (wqf_data['reposts_count']==0)&
    

    NameError: name 'wqf_data' is not defined



```python
print('吴青峰真粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_true.shape[0]/wqf_data.shape[0]*100, 2)))
print('吴青峰假粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_fake.shape[0]/wqf_data.shape[0]*100, 2)))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-52-1386f1163bde> in <module>
    ----> 1 print('吴青峰真粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_true.shape[0]/wqf_data.shape[0]*100, 2)))
          2 print('吴青峰假粉丝转发数占总转发数的{}%'.format(np.round(wqf_data_fake.shape[0]/wqf_data.shape[0]*100, 2)))
    

    NameError: name 'wqf_data_true' is not defined



```python
bar = Bar("吴青峰真假流量的转发量", width = 600,height=500)
bar.add("(总数据10006条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
        [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0]], is_stack=True,
        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-53-5fbbbc277898> in <module>
    ----> 1 bar = Bar("吴青峰真假流量的转发量", width = 600,height=500)
          2 bar.add("(总数据10006条)", ['总转发量', '假粉丝转发量', '真粉丝转发量'], 
          3         [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0]], is_stack=True,
          4         xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
          5 bar
    

    NameError: name 'Bar' is not defined



```python
wqf_real_fans_num = wqf_data_true.drop_duplicates(subset='user.id').shape[0]

bar = Bar("吴青峰真假流量的转发量与真实转发粉丝量(总数据10006条)", width = 600,height=500)
bar.add('', ['总转发量', '假粉丝转发量', '真粉丝转发量', '真实转发粉丝量'], 
        [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0], 
         wqf_real_fans_num], is_stack=True, 
        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=20)
bar
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-54-7106e86e519b> in <module>
    ----> 1 wqf_real_fans_num = wqf_data_true.drop_duplicates(subset='user.id').shape[0]
          2 
          3 bar = Bar("吴青峰真假流量的转发量与真实转发粉丝量(总数据10006条)", width = 600,height=500)
          4 bar.add('', ['总转发量', '假粉丝转发量', '真粉丝转发量', '真实转发粉丝量'], 
          5         [wqf_data.shape[0], wqf_data_fake.shape[0], wqf_data_true.shape[0], 
    

    NameError: name 'wqf_data_true' is not defined



```python
wqf_data.sample(5)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-55-97c52ba19689> in <module>
    ----> 1 wqf_data.sample(5)
    

    NameError: name 'wqf_data' is not defined



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
      <th>59458</th>
      <td>0,0,0,4.3484E+15,宝//@是蔡徐坤的cooky:#东方风云榜让世界看见蔡徐坤...</td>
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
      <th>1787</th>
      <td>0,0,0,4.34801E+15,没有意外 我还喜欢你,Android,,0,1,m,69...</td>
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
      <th>101447</th>
      <td>0,0,0,4.34869E+15,Every cloud has a silver lin...</td>
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
      <th>97832</th>
      <td>0,0,0,4.34867E+15,"ritmo, profumo, luce, mia u...</td>
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
      <th>20224</th>
      <td>0,0,0,4.34837E+15,[思考]//@Cai欢Kun:82千老板[酸][酸][酸...</td>
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
</div>



### 3. 假流量粉丝是如何生产出来的？


```python
data_fake_gender = data_fake.drop_duplicates(subset='user.id')['user.gender'].value_counts()
data_fake_gender
```




    Series([], Name: user.gender, dtype: int64)




```python
data_fake[data_fake['user.gender']=='f'].sample(5)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-58-5d6974b84482> in <module>
    ----> 1 data_fake[data_fake['user.gender']=='f'].sample(5)
    

    d:\python\lib\site-packages\pandas\core\generic.py in sample(self, n, frac, replace, weights, random_state, axis)
       4993             )
       4994 
    -> 4995         locs = rs.choice(axis_length, size=n, replace=replace, p=weights)
       4996         return self.take(locs, axis=axis)
       4997 
    

    mtrand.pyx in numpy.random.mtrand.RandomState.choice()
    

    ValueError: a must be greater than 0 unless no samples are taken



```python
bar = Bar("蔡徐坤假粉丝性别比例", width = 600,height=500)
bar.add("(假粉丝总数为40838)", ['男', '女'], data_fake_gender.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-59-70d8aab48a44> in <module>
    ----> 1 bar = Bar("蔡徐坤假粉丝性别比例", width = 600,height=500)
          2 bar.add("(假粉丝总数为40838)", ['男', '女'], data_fake_gender.values, is_stack=True, 
          3        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
          4 bar
    

    NameError: name 'Bar' is not defined



```python
38969/40838
```




    0.954233801851217




```python
data_fake['raw_text'].value_counts()
```




    Series([], Name: raw_text, dtype: int64)




```python
fake_source = data_fake['source'].value_counts()[:10]
```


```python
bar = Bar("蔡徐坤假粉丝Top10转发设备", width = 600,height=600)
bar.add("", fake_source.index, fake_source.values, is_stack=True, 
       xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
bar
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-63-db44e19c1c6d> in <module>
    ----> 1 bar = Bar("蔡徐坤假粉丝Top10转发设备", width = 600,height=600)
          2 bar.add("", fake_source.index, fake_source.values, is_stack=True, 
          3        xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
          4 bar
    

    NameError: name 'Bar' is not defined



```python
data_fake['user.follow_count'].mean()
```




    nan




```python
data_fake['user.followers_count'].mean()
```




    nan




```python
data_fake_sample = data_fake.sample(5)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-66-84d2eabdf0f3> in <module>
    ----> 1 data_fake_sample = data_fake.sample(5)
    

    d:\python\lib\site-packages\pandas\core\generic.py in sample(self, n, frac, replace, weights, random_state, axis)
       4993             )
       4994 
    -> 4995         locs = rs.choice(axis_length, size=n, replace=replace, p=weights)
       4996         return self.take(locs, axis=axis)
       4997 
    

    mtrand.pyx in numpy.random.mtrand.RandomState.choice()
    

    ValueError: a must be greater than 0 unless no samples are taken



```python
data_fake_sample['user.screen_name']
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-67-d3411bd94798> in <module>
    ----> 1 data_fake_sample['user.screen_name']
    

    NameError: name 'data_fake_sample' is not defined



```python
data_fake_sample['user.profile_image_url'].values
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-68-fbe42d1fbca7> in <module>
    ----> 1 data_fake_sample['user.profile_image_url'].values
    

    NameError: name 'data_fake_sample' is not defined



```python
data_fake.sample(5)['user.screen_name']
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-69-381dba7d3da0> in <module>
    ----> 1 data_fake.sample(5)['user.screen_name']
    

    d:\python\lib\site-packages\pandas\core\generic.py in sample(self, n, frac, replace, weights, random_state, axis)
       4993             )
       4994 
    -> 4995         locs = rs.choice(axis_length, size=n, replace=replace, p=weights)
       4996         return self.take(locs, axis=axis)
       4997 
    

    mtrand.pyx in numpy.random.mtrand.RandomState.choice()
    

    ValueError: a must be greater than 0 unless no samples are taken



```python
data_fake['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-70-ae67f9dbeca1> in <module>
    ----> 1 data_fake['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
    

    d:\python\lib\site-packages\pandas\core\generic.py in __getattr__(self, name)
       5135             or name in self._accessors
       5136         ):
    -> 5137             return object.__getattribute__(self, name)
       5138         else:
       5139             if self._info_axis._can_hold_identifiers_and_holds_name(name):
    

    d:\python\lib\site-packages\pandas\core\accessor.py in __get__(self, obj, cls)
        185             # we're accessing the attribute of the class, i.e., Dataset.geo
        186             return self._accessor
    --> 187         accessor_obj = self._accessor(obj)
        188         # Replace the property with the accessor object. Inspired by:
        189         # https://www.pydanny.com/cached-property.html
    

    d:\python\lib\site-packages\pandas\core\strings.py in __init__(self, data)
       2098 
       2099     def __init__(self, data):
    -> 2100         self._inferred_dtype = self._validate(data)
       2101         self._is_categorical = is_categorical_dtype(data.dtype)
       2102         self._is_string = data.dtype.name == "string"
    

    d:\python\lib\site-packages\pandas\core\strings.py in _validate(data)
       2155 
       2156         if inferred_dtype not in allowed_types:
    -> 2157             raise AttributeError("Can only use .str accessor with string values!")
       2158         return inferred_dtype
       2159 
    

    AttributeError: Can only use .str accessor with string values!



```python
data_fake.shape[0]
```




    0




```python
data_fake['user.statuses_count'].mean()
```




    nan



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
      <th>12019</th>
      <td>0,0,0,4.3483E+15,L’innamorato ansante piegato ...</td>
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
      <th>70500</th>
      <td>0,0,0,4.34852E+15,你笑起来真像好天气。,Android,,0,1,m,70...</td>
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
      <th>3242</th>
      <td>0,0,0,4.348E+15,阳光青年努力向上//@华小葵想改变逸:#东方风云榜让世界看见...</td>
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
      <th>10537</th>
      <td>0,0,0,4.3483E+15,No man can serve two masters....</td>
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
      <th>46909</th>
      <td>0,0,0,4.34842E+15,[心]//@坤坤味的小IKUN://@CXK-FANSC...</td>
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
</div>




```python
data_true_gender = data_true.drop_duplicates(subset='user.id')['user.gender'].value_counts()
data_true_gender
```




    Series([], Name: user.gender, dtype: int64)




```python
bar = Bar("蔡徐坤真粉丝性别比例", width = 600,height=500)
bar.add("(真粉丝总数为3926)", ['女', '男'], data_true_gender.values, is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
bar
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-75-bec88fef0f03> in <module>
    ----> 1 bar = Bar("蔡徐坤真粉丝性别比例", width = 600,height=500)
          2 bar.add("(真粉丝总数为3926)", ['女', '男'], data_true_gender.values, is_stack=True, 
          3        xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True)
          4 bar
    

    NameError: name 'Bar' is not defined



```python
data_true['raw_text'].value_counts()
```




    Series([], Name: raw_text, dtype: int64)




```python
true_source = data_true['source'].value_counts()[:10]
```


```python
bar = Bar("蔡徐坤真粉丝Top10转发设备", width = 600,height=600)
bar.add("", true_source.index, true_source.values, is_stack=True, 
       xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
bar
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-78-f7976d958d26> in <module>
    ----> 1 bar = Bar("蔡徐坤真粉丝Top10转发设备", width = 600,height=600)
          2 bar.add("", true_source.index, true_source.values, is_stack=True, 
          3        xaxis_label_textsize=11, yaxis_label_textsize=14, is_label_show=True, xaxis_rotate=30)
          4 bar
    

    NameError: name 'Bar' is not defined



```python
data_true['user.follow_count'].mean()
```




    nan




```python
data_true['user.followers_count'].mean()
```




    nan




```python
data_true.sample(5)['user.screen_name']
```




    43937   NaN
    22655   NaN
    41256   NaN
    22346   NaN
    44003   NaN
    Name: user.screen_name, dtype: float64




```python
data_true['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-82-a3c5af8be75c> in <module>
    ----> 1 data_true['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
    

    d:\python\lib\site-packages\pandas\core\generic.py in __getattr__(self, name)
       5135             or name in self._accessors
       5136         ):
    -> 5137             return object.__getattribute__(self, name)
       5138         else:
       5139             if self._info_axis._can_hold_identifiers_and_holds_name(name):
    

    d:\python\lib\site-packages\pandas\core\accessor.py in __get__(self, obj, cls)
        185             # we're accessing the attribute of the class, i.e., Dataset.geo
        186             return self._accessor
    --> 187         accessor_obj = self._accessor(obj)
        188         # Replace the property with the accessor object. Inspired by:
        189         # https://www.pydanny.com/cached-property.html
    

    d:\python\lib\site-packages\pandas\core\strings.py in __init__(self, data)
       2098 
       2099     def __init__(self, data):
    -> 2100         self._inferred_dtype = self._validate(data)
       2101         self._is_categorical = is_categorical_dtype(data.dtype)
       2102         self._is_string = data.dtype.name == "string"
    

    d:\python\lib\site-packages\pandas\core\strings.py in _validate(data)
       2155 
       2156         if inferred_dtype not in allowed_types:
    -> 2157             raise AttributeError("Can only use .str accessor with string values!")
       2158         return inferred_dtype
       2159 
    

    AttributeError: Can only use .str accessor with string values!



```python
data_true.shape[0]
```




    102316




```python
# 绘制蔡徐坤真粉丝的简介词云图
import jieba
from collections import Counter
from pyecharts import WordCloud

jieba.add_word('蔡徐坤')

swords = [x.strip() for x in open ('stopwords.txt')]
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-84-1b6d40e9f502> in <module>
          2 import jieba
          3 from collections import Counter
    ----> 4 from pyecharts import WordCloud
          5 
          6 jieba.add_word('蔡徐坤')
    

    ImportError: cannot import name 'WordCloud' from 'pyecharts' (d:\python\lib\site-packages\pyecharts\__init__.py)



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


```python
plot_word_cloud(data=data_true, swords=swords, columns='raw_text')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-85-b7c7d4b5ce4f> in <module>
    ----> 1 plot_word_cloud(data=data_true, swords=swords, columns='raw_text')
    

    NameError: name 'plot_word_cloud' is not defined



