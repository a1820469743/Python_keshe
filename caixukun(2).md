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
data = pd.read_csv('D://caixukun.csv')
```


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 102313 entries, 0 to 102312
    Data columns (total 20 columns):
     #   Column                  Non-Null Count   Dtype 
    ---  ------                  --------------   ----- 
     0   attitudes_count         102313 non-null  int64 
     1   comments_count          102313 non-null  int64 
     2   reposts_count           102313 non-null  int64 
     3   mid                     102313 non-null  int64 
     4   raw_text                102313 non-null  object
     5   source                  102188 non-null  object
     6   user.description        4569 non-null    object
     7   user.follow_count       102313 non-null  int64 
     8   user.followers_count    102313 non-null  int64 
     9   user.gender             102313 non-null  object
     10  user.id                 102313 non-null  int64 
     11  user.mbrank             102313 non-null  int64 
     12  user.mbtype             102313 non-null  int64 
     13  user.profile_url        102313 non-null  object
     14  user.profile_image_url  102313 non-null  object
     15  user.screen_name        102313 non-null  object
     16  user.statuses_count     102313 non-null  int64 
     17  user.urank              102313 non-null  int64 
     18  user.verified           102313 non-null  bool  
     19  user.verified_reason    356 non-null     object
    dtypes: bool(1), int64(11), object(8)
    memory usage: 14.9+ MB
    


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
      <th>54790</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348426592723839</td>
      <td>Auxiliary extreme aestheticism bait to capture...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7015030565</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7015030565?uid=7015030565</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>优秀坤哥0vF170</td>
      <td>58</td>
      <td>2</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>67499</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348413884001842</td>
      <td>I am only waiting for love to give myself up a...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7013576044</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7013576044?uid=7013576044</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>沉重重量Dpv579</td>
      <td>29</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>53722</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348423526029084</td>
      <td>[并不简单]//@坤哥迷妹丫:等风也等你@Only-For-Kun唯粉站 #蔡徐坤[超话]#</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6981564429</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6981564429?uid=6981564429</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.200.200.180/...</td>
      <td>用户6981564429</td>
      <td>147</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>89171</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348649468953519</td>
      <td>With the wonder of your love， the sun above al...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7011851850</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7011851850?uid=7011851850</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>用户7011851850</td>
      <td>69</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>84372</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348643232223947</td>
      <td>As much as I should//@是积极努力的心心唷:#东方风云榜让世界看见蔡徐坤...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6941059923</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6941059923?uid=6941059923</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.621.621.180/...</td>
      <td>皮皮葵rqK353</td>
      <td>129</td>
      <td>4</td>
      <td>False</td>
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
    RangeIndex: 102313 entries, 0 to 102312
    Data columns (total 20 columns):
     #   Column                  Non-Null Count   Dtype 
    ---  ------                  --------------   ----- 
     0   attitudes_count         102313 non-null  int64 
     1   comments_count          102313 non-null  int64 
     2   reposts_count           102313 non-null  int64 
     3   mid                     102313 non-null  int64 
     4   raw_text                102313 non-null  object
     5   source                  102188 non-null  object
     6   user.description        4569 non-null    object
     7   user.follow_count       102313 non-null  int64 
     8   user.followers_count    102313 non-null  int64 
     9   user.gender             102313 non-null  object
     10  user.id                 102313 non-null  int64 
     11  user.mbrank             102313 non-null  int64 
     12  user.mbtype             102313 non-null  int64 
     13  user.profile_url        102313 non-null  object
     14  user.profile_image_url  102313 non-null  object
     15  user.screen_name        102313 non-null  object
     16  user.statuses_count     102313 non-null  int64 
     17  user.urank              102313 non-null  int64 
     18  user.verified           102313 non-null  bool  
     19  user.verified_reason    356 non-null     object
    dtypes: bool(1), int64(11), object(8)
    memory usage: 14.9+ MB
    


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
    <div id="c061515b259643888c149fd4206323f2" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_c061515b259643888c149fd4206323f2 = echarts.init(document.getElementById('c061515b259643888c149fd4206323f2'), 'light', {renderer: 'canvas'});

var option_c061515b259643888c149fd4206323f2 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u7c89\u4e1d\u6027\u522b\u6bd4\u4f8b\u521d\u63a2",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
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
    "series_id": 2014225,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
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
            "stack": "stack_2014225",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
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
            "seriesId": 2014225
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
                "fontSize": 12
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "category",
            "splitLine": {
                "show": false
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20
                }
            },
            "data": [
                "\u7537",
                "\u5973"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "value",
            "splitLine": {
                "show": true
            },
            "axisLabel": {
                "interval": "auto",
                "formatter": "{value} ",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 14
                }
            }
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
myChart_c061515b259643888c149fd4206323f2.setOption(option_c061515b259643888c149fd4206323f2);

    });
</script>





```python
np.round(fans_num/fans_num.sum()*100, 2)
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
      <th>28557</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348343880261333</td>
      <td>Also care about what has//@ikun守护奶坤:#东方风云榜让世界看...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6975520523</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6975520523?uid=6975520523</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.400.400.180/...</td>
      <td>用户6975520523</td>
      <td>165</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>52960</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348410498348174</td>
      <td>[酷]//@坤哥迷妹丫:等风也等你@Only-For-Kun唯粉站 #蔡徐坤[超话]#</td>
      <td>Android</td>
      <td>NaN</td>
      <td>15</td>
      <td>1</td>
      <td>m</td>
      <td>6628171199</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6628171199?uid=6628171199</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>参壤撇纟j</td>
      <td>884</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>63596</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348405654377669</td>
      <td>一起走花路吧蔡//@华小葵想改变逸:#东方风云榜让世界看见蔡徐坤#  再见了您呢千千//@A...</td>
      <td>前置双摄vivo X9</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7004662767</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7004662767?uid=7004662767</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>低调行事9ar311</td>
      <td>39</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20749</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348381457756588</td>
      <td>一架钢琴，一个故事</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>6926994035</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6926994035?uid=6926994035</td>
      <td>https://tvax4.sinaimg.cn/default/images/defaul...</td>
      <td>用户6926994035</td>
      <td>60</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1892</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348008751174571</td>
      <td>We go party we go drink ladies check  //@陈晨-愿坤...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7011878855</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7011878855?uid=7011878855</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>点点小葵ZfP250</td>
      <td>9</td>
      <td>0</td>
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


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-14-d1a9f9ca80eb> in <module>
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


```python
# 把假的流量粉丝转发组合起来
data_fake = pd.concat([data_fake, data.iloc[data_fake2_index]])
```


```python
data_fake.shape
```




    (71, 20)




```python
# 取出真粉的转发
data_true = data.drop(data_fake.index)
```


```python
data_true.shape
```




    (102242, 20)




```python
print('真粉丝转发数占总转发数的{}%'.format(np.round(data_true.shape[0]/data.shape[0]*100, 2)))
print('假粉丝转发数占总转发数的{}%'.format(np.round(data_fake.shape[0]/data.shape[0]*100, 2)))
```

    真粉丝转发数占总转发数的99.93%
    假粉丝转发数占总转发数的0.07%
    


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
    <div id="506bf63cbd024bec875783c0acb44ac7" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_506bf63cbd024bec875783c0acb44ac7 = echarts.init(document.getElementById('506bf63cbd024bec875783c0acb44ac7'), 'light', {renderer: 'canvas'});

var option_506bf63cbd024bec875783c0acb44ac7 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u5047\u6d41\u91cf\u7684\u8f6c\u53d1\u91cf",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
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
    "series_id": 462469,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
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
                71,
                102242
            ],
            "stack": "stack_462469",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
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
            "seriesId": 462469
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
                "fontSize": 12
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "category",
            "splitLine": {
                "show": false
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20
                }
            },
            "data": [
                "\u603b\u8f6c\u53d1\u91cf",
                "\u5047\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u7c89\u4e1d\u8f6c\u53d1\u91cf"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "value",
            "splitLine": {
                "show": true
            },
            "axisLabel": {
                "interval": "auto",
                "formatter": "{value} ",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 14
                }
            }
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
myChart_506bf63cbd024bec875783c0acb44ac7.setOption(option_506bf63cbd024bec875783c0acb44ac7);

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
    <div id="bccecb1166a24b3eb652870d95675f65" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_bccecb1166a24b3eb652870d95675f65 = echarts.init(document.getElementById('bccecb1166a24b3eb652870d95675f65'), 'light', {renderer: 'canvas'});

var option_bccecb1166a24b3eb652870d95675f65 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u5047\u6d41\u91cf\u7684\u8f6c\u53d1\u91cf\u4e0e\u771f\u5b9e\u8f6c\u53d1\u7c89\u4e1d\u91cf(\u603b\u6570\u636e102313\u6761)",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
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
    "series_id": 621274,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "data": [
                102313,
                71,
                102242,
                44702
            ],
            "stack": "stack_621274",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
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
            "seriesId": 621274
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
                "fontSize": 12
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "category",
            "splitLine": {
                "show": false
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 20,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20
                }
            },
            "data": [
                "\u603b\u8f6c\u53d1\u91cf",
                "\u5047\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u7c89\u4e1d\u8f6c\u53d1\u91cf",
                "\u771f\u5b9e\u8f6c\u53d1\u7c89\u4e1d\u91cf"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "value",
            "splitLine": {
                "show": true
            },
            "axisLabel": {
                "interval": "auto",
                "formatter": "{value} ",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 14
                }
            }
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
myChart_bccecb1166a24b3eb652870d95675f65.setOption(option_bccecb1166a24b3eb652870d95675f65);

    });
</script>





```python
print('真实转发粉丝量占总转发数的{}%'.format(np.round(real_fans_num/data.shape[0]*100, 2)))
```

    真实转发粉丝量占总转发数的43.69%
    

-----------------吴青峰微博数据做对比-----------------


```python
db = conn.get_database('WuQingFeng')  # WuQingFeng

repost = db.get_collection('repost') # repost
mon_data = repost.find()  # 查询这个集合下的所有记录
```


```python
wqf_data = json_normalize([comment for comment in mon_data])
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




    f    36
    m    21
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
      <th>15852</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348318781836265</td>
      <td>轉發微博</td>
      <td>iPhone客户端</td>
      <td>NaN</td>
      <td>36</td>
      <td>24</td>
      <td>f</td>
      <td>6854641738</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6854641738?uid=6854641738</td>
      <td>https://tvax3.sinaimg.cn/default/images/defaul...</td>
      <td>用户6854641738</td>
      <td>87</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3973</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348247629163936</td>
      <td>转发微博</td>
      <td>荣耀畅玩8C</td>
      <td>活泼可爱</td>
      <td>843</td>
      <td>25</td>
      <td>f</td>
      <td>6609289135</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6609289135?uid=6609289135</td>
      <td>https://tvax4.sinaimg.cn/default/images/defaul...</td>
      <td>用户6609289135</td>
      <td>1424</td>
      <td>12</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>96758</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348667584649250</td>
      <td>转发微博</td>
      <td>vivo X23 AI非凡摄影</td>
      <td>NaN</td>
      <td>90</td>
      <td>11</td>
      <td>f</td>
      <td>6508705084</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6508705084?uid=6508705084</td>
      <td>https://tvax1.sinaimg.cn/crop.0.0.664.664.180/...</td>
      <td>用户6508705084</td>
      <td>437</td>
      <td>9</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>986</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348036265957654</td>
      <td>转发微博</td>
      <td>荣耀V8 脱影而出</td>
      <td>NaN</td>
      <td>525</td>
      <td>30</td>
      <td>f</td>
      <td>6555222773</td>
      <td>1</td>
      <td>2</td>
      <td>https://m.weibo.cn/u/6555222773?uid=6555222773</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.996.996.180/...</td>
      <td>用户6555222773</td>
      <td>1023</td>
      <td>9</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>78098</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348593378725645</td>
      <td>@蔡徐坤  我在#明星ALL榜[超话]#上为你加油啦，你是我今生唯一的执著哦。#蔡徐坤[超话...</td>
      <td>明星ALL榜</td>
      <td>NaN</td>
      <td>175</td>
      <td>63</td>
      <td>f</td>
      <td>6295192291</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6295192291?uid=6295192291</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.789.789.180/...</td>
      <td>用户西子西卒116</td>
      <td>9537</td>
      <td>20</td>
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
    <div id="eda9121add244ddea3288fe2a3f4450c" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_eda9121add244ddea3288fe2a3f4450c = echarts.init(document.getElementById('eda9121add244ddea3288fe2a3f4450c'), 'light', {renderer: 'canvas'});

var option_eda9121add244ddea3288fe2a3f4450c = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u5047\u7c89\u4e1d\u6027\u522b\u6bd4\u4f8b",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
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
    "series_id": 4502748,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
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
                36.0,
                21.0
            ],
            "stack": "stack_4502748",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
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
            "seriesId": 4502748
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
                "fontSize": 12
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "category",
            "splitLine": {
                "show": false
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20
                }
            },
            "data": [
                "\u7537",
                "\u5973"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "value",
            "splitLine": {
                "show": true
            },
            "axisLabel": {
                "interval": "auto",
                "formatter": "{value} ",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 14
                }
            }
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
myChart_eda9121add244ddea3288fe2a3f4450c.setOption(option_eda9121add244ddea3288fe2a3f4450c);

    });
</script>





```python
38969/40838
```




    0.954233801851217




```python
data_fake['raw_text'].value_counts()
```




    转发微博                                                                                                                                     19
    @蔡徐坤 我永远支持你！我们一起拿下 #明星势力榜# 第一名！                                                                                                           7
    @蔡徐坤  我在#明星ALL榜[超话]#上为你加油啦，你是我今生唯一的执著哦。#蔡徐坤[超话]# 棒棒哒！快来为TA应援吧                                                                             2
    #东方风云榜让世界看见蔡徐坤# 再见千千                                                                                                                      2
    #东方风云榜让世界看见蔡徐坤#@蔡徐坤 我永远支持你！我们一起拿下 #明星势力榜# 第一名！                                                                                            2
    #东方风云榜让世界看见蔡徐坤# 哥哥好善良@蔡徐坤                                                                                                                 1
    情不知所起，一往而情深[米奇飞吻]@蔡徐坤                                                                                                                     1
    蔡徐坤你最大的遗憾就是不能亲吻自己的脸！#东方风云榜让世界看见蔡徐坤#好喜欢呀@蔡徐坤                                                                                               1
    你在梦里，我不愿醒来。[太阳][太阳][太阳][太阳][太阳]@蔡徐坤                                                                                                       1
    蔡徐坤 像吃了一口草莓味的冰淇淋 像听了一段酥到耳朵的声音 像温柔融化在我唇上的雪花 一切美好都不够表达 我喜欢你@蔡徐坤                                                                             1
    [害羞]//@Zombie_热里:A@蔡徐坤                                                                                                                    1
    神的爱情从希腊开始 我的爱情从你开始[微笑][微笑][微笑][微笑]@蔡徐坤                                                                                                    1
    轉發微博                                                                                                                                      1
    [微笑]//@蔡徐坤工作室:#蔡徐坤[超话]#[给你小心心]#蔡徐坤的未完成#之宠物医院终于步入尾声，在短暂的相处时间里，因为工作忙碌无法养育小动物的@蔡徐坤 也获得了片刻的慰藉，感谢千千给我们带来了一段难忘的回忆[心]#蔡徐坤 ONE#                   1
    2//@遇见小坤坤:可爱的小千千☺//@蔡徐坤正宫后援会:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千一定要健康的成长哦[心][心][心]@蔡徐坤                                                        1
    千千会好好的，坤坤也要好好的喔[爱你]晚安唷[月亮]                                                                                                                1
    #蔡徐坤# #东方风云榜让世界看见蔡徐坤# 再见  千千 希望在新家好好的 坤哥早上好@蔡徐坤                                                                                           1
    #蔡徐坤的未完成#My eyes have seen and my ears have heard.                                                                                        1
    3//@遇见小坤坤:可爱的小千千☺//@蔡徐坤正宫后援会:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千一定要健康的成长哦[心][心][心]@蔡徐坤                                                        1
    众里寻她干百度，蓦然回首，那人却在，灯火阑珊处                                                                                                                   1
    #蔡徐坤的未完成#Also care about what has                                                                                                         1
    //@蔡徐坤粉丝团官微:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千要健康成长噢 @蔡徐坤                                                                                    1
    #东方风云榜让世界看见蔡徐坤# 蔡徐坤啊 自从见到了你我心里的小鹿就得了脑震荡@蔡徐坤                                                                                               1
    #东方风云榜让世界看见蔡徐坤# 这世间青山灼灼 星光杳杳，秋雨淅淅 晚风慢慢，也抵不过蔡公子您眉目间的星辰啊。@蔡徐坤                                                                               1
    #东方风云榜让世界看见蔡徐坤# 从不被挫折束缚道路似明似暗   @蔡徐坤                                                                                                      1
    你给予的一份关爱，一点关心，会让小动物们陪伴你一辈子//@蔡徐坤妈妈团LovelyClub:#东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 一份关爱，一份守护，陪伴世界上最好的朋友，给予小动物们更多的温暖。与我们的蔡医生@蔡徐坤 一起，浓情春日，点滴真心。     1
    4//@遇见小坤坤:可爱的小千千☺//@蔡徐坤正宫后援会:#东方风云榜让世界看见蔡徐坤#  | #蔡徐坤的未完成# 千千一定要健康的成长哦[心][心][心]@蔡徐坤                                                        1
    #东方风云榜让世界看见蔡徐坤# 喜欢胜过所有道理，原则抵不过我乐意。@蔡徐坤                                                                                                    1
    #东方风云榜让世界看见蔡徐坤# 日常表白坤坤                                                                                                                    1
    年华已旧 少年已老[挤眼][挤眼][挤眼][挤眼]@蔡徐坤                                                                                                             1
    千千                                                                                                                                        1
    一起善待动物                                                                                                                                    1
    #东方风云榜让世界看见蔡徐坤# [心]#蔡徐坤的未完成# 优秀的蔡徐坤你是最棒的加油加油@蔡徐坤                                                                                          1
    再见千千//@-HuWeiX:再见，任性的“千千” 勇敢说再见，照顾好自己#东方风云榜让世界看见蔡徐坤#                                                                                      1
    #蔡徐坤[超话]# [可爱]#东方风云榜让世界看见蔡徐坤# 关爱流浪动物，给它们一个温暖的家@蔡徐坤                                                                                        1
    #东方风云榜让世界看见蔡徐坤#                                                                                                                           1
    真想做你的影子，就算你并不在意我的存在，我也能一直陪你到最后。[赞啊][赞啊][赞啊][赞啊]@蔡徐坤                                                                                       1
    中午好蔡徐坤                                                                                                                                    1
    因为一座城，爱上一个人，因为一个人，又恋一座城。[米奇爱你][米奇爱你][米奇爱你]@蔡徐坤                                                                                            1
    [汗]//@KUN-AWM:#东方风云榜让世界看见蔡徐坤# |#蔡徐坤的未完成# 坚持自己的善良，一直陪伴@蔡徐坤                                                                                 1
    请你不要再到处释放魅力了。[米奇爱你]@蔡徐坤                                                                                                                   1
    蔡徐坤正能量@蔡徐坤                                                                                                                                1
    爱你                                                                                                                                        1
    [心]                                                                                                                                       1
    Name: raw_text, dtype: int64




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
    <div id="621c1bb89546475eaf8a0450a3e1c51e" style="width:600px;height:600px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_621c1bb89546475eaf8a0450a3e1c51e = echarts.init(document.getElementById('621c1bb89546475eaf8a0450a3e1c51e'), 'light', {renderer: 'canvas'});

var option_621c1bb89546475eaf8a0450a3e1c51e = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u5047\u7c89\u4e1dTop10\u8f6c\u53d1\u8bbe\u5907",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
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
    "series_id": 5303321,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "data": [
                16.0,
                9.0,
                7.0,
                4.0,
                3.0,
                2.0,
                2.0,
                2.0,
                2.0,
                2.0
            ],
            "stack": "stack_5303321",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
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
            "seriesId": 5303321
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
                "fontSize": 12
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "category",
            "splitLine": {
                "show": false
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 30,
                "margin": 8,
                "textStyle": {
                    "fontSize": 11
                }
            },
            "data": [
                "iPhone\u5ba2\u6237\u7aef",
                "\u660e\u661f\u52bf\u529b\u699c",
                "UC\u6d4f\u89c8\u5668",
                "Android",
                "OPPO\u667a\u80fd\u624b\u673a",
                "\u8363\u8000V20 4800\u4e073D\u76f8\u673a",
                "\u5c0f\u7c735X \u62cd\u4eba\u66f4\u7f8e",
                "\u660e\u661fALL\u699c",
                "\u4e09\u661fandroid\u667a\u80fd\u624b\u673a",
                "HUAWEI Mate 9"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "value",
            "splitLine": {
                "show": true
            },
            "axisLabel": {
                "interval": "auto",
                "formatter": "{value} ",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 14
                }
            }
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
myChart_621c1bb89546475eaf8a0450a3e1c51e.setOption(option_621c1bb89546475eaf8a0450a3e1c51e);

    });
</script>





```python
data_fake['user.follow_count'].mean()
```




    153.30985915492957




```python
data_fake['user.followers_count'].mean()
```




    20.08450704225352




```python
data_fake_sample = data_fake.sample(5)
```


```python
data_fake_sample['user.screen_name']
```




    377      用户6206301043
    63090    用户6527641218
    56350    用户6097306281
    96759    用户5215602496
    8824     用户6652320477
    Name: user.screen_name, dtype: object




```python
data_fake_sample['user.profile_image_url'].values
```




    array(['https://tvax4.sinaimg.cn/crop.0.0.960.960.180/006M10pJly8fzvgsyl37wj30qo0qoq5c.jpg',
           'https://tvax1.sinaimg.cn/crop.0.0.996.996.180/0077LjFMly8fy8pr097j0j30ro0rotah.jpg',
           'https://tvax2.sinaimg.cn/default/images/default_avatar_male_180.gif',
           'https://tvax2.sinaimg.cn/crop.0.0.960.960.180/005GY8sUly8fuwiqpq201j30qo0qot9s.jpg',
           'https://tvax4.sinaimg.cn/crop.0.0.512.512.180/007gcsrzly8fyvsqp1aaqj30e80e8mxr.jpg'],
          dtype=object)




```python
data_fake.sample(5)['user.screen_name']
```




    70943    用户6495479716
    77606    用户6765354286
    377      用户6206301043
    55036    用户6462754814
    10092    用户1082174265
    Name: user.screen_name, dtype: object




```python
data_fake['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
```




    1




```python
data_fake.shape[0]
```




    71




```python
data_fake['user.statuses_count'].mean()
```




    1359.3098591549297



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
      <th>505</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348037906434707</td>
      <td>每天看看你的脸就觉得自己在谈恋爱呢！蔡徐坤//@蔡徐坤我老公鸭://@AK47-KAKAKA...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7010905359</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7010905359?uid=7010905359</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>用户7010905359</td>
      <td>30</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9160</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348297919261885</td>
      <td>Those who came to call me in vain have gone ba...</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7012423491</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7012423491?uid=7012423491</td>
      <td>https://tvax4.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>坤坤很困f21595</td>
      <td>50</td>
      <td>2</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>64049</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>4348458258972197</td>
      <td>#东方风云榜让世界看见蔡徐坤# 愿你被这个世界温柔相待,  愿你目之所及,心之所向满满都是爱...</td>
      <td>iPhone客户端</td>
      <td>NaN</td>
      <td>68</td>
      <td>2</td>
      <td>m</td>
      <td>6785964534</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6785964534?uid=6785964534</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.1080.1080.18...</td>
      <td>金刚金鹦</td>
      <td>20</td>
      <td>3</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38806</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348413602592498</td>
      <td>[并不简单]//@坤哥迷妹丫:等风也等你@Only-For-Kun唯粉站 #蔡徐坤[超话]#</td>
      <td>Android</td>
      <td>NaN</td>
      <td>12</td>
      <td>1</td>
      <td>f</td>
      <td>6628141749</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/6628141749?uid=6628141749</td>
      <td>https://tvax3.sinaimg.cn/crop.0.0.100.100.180/...</td>
      <td>拭巡沽_j</td>
      <td>836</td>
      <td>4</td>
      <td>False</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>52209</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4348413048551537</td>
      <td>Distance the devil walked in between</td>
      <td>Android</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>m</td>
      <td>7018538568</td>
      <td>0</td>
      <td>0</td>
      <td>https://m.weibo.cn/u/7018538568?uid=7018538568</td>
      <td>https://tvax2.sinaimg.cn/crop.0.0.640.640.180/...</td>
      <td>抱抱我奎kiU311</td>
      <td>18</td>
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




    m    39585
    f     5117
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
    <div id="4481b9a277e14afea579b799d4c34393" style="width:600px;height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_4481b9a277e14afea579b799d4c34393 = echarts.init(document.getElementById('4481b9a277e14afea579b799d4c34393'), 'light', {renderer: 'canvas'});

var option_4481b9a277e14afea579b799d4c34393 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u7c89\u4e1d\u6027\u522b\u6bd4\u4f8b",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
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
    "series_id": 5656916,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
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
                39585.0,
                5117.0
            ],
            "stack": "stack_5656916",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
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
            "seriesId": 5656916
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
                "fontSize": 12
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "category",
            "splitLine": {
                "show": false
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 20
                }
            },
            "data": [
                "\u5973",
                "\u7537"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "value",
            "splitLine": {
                "show": true
            },
            "axisLabel": {
                "interval": "auto",
                "formatter": "{value} ",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 14
                }
            }
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
myChart_4481b9a277e14afea579b799d4c34393.setOption(option_4481b9a277e14afea579b799d4c34393);

    });
</script>





```python
data_true['raw_text'].value_counts()
```




    转发微博                                                                                 1455
    @蔡徐坤 我永远支持你！我们一起拿下 #明星势力榜# 第一名！                                                       644
    I am only waiting for love to give myself up at last into his hands.                  375
    想你//@蔡徐坤的南岸末阴大小姐:#东方风云榜让世界看见蔡徐坤# /#蔡徐坤的未完成#祝千千在新家能快快乐乐 健健康康的@蔡徐坤                      289
    我心悦你//@蔡徐坤的南岸末阴大小姐:#东方风云榜让世界看见蔡徐坤# /#蔡徐坤的未完成#祝千千在新家能快快乐乐 健健康康的@蔡徐坤                    288
                                                                                         ... 
    跟着你的脚步，走遍天涯海角。[微笑][微笑][微笑][微笑][微笑]@蔡徐坤                                                  1
    [心][心]可爱的千千温柔的坤坤@蔡徐坤                                                                    1
    [羞嗒嗒]//@看黑子多跳脚就知道蔡徐坤有多火:#东方风云榜让世界看见蔡徐坤# 千千 要乖乖的哦[亲亲][亲亲][亲亲] 哥哥好温柔哦 嘻嘻嘻[污][污]@蔡徐坤       1
    31//@yjdudndczhz:坤坤~@蔡徐坤 #东方风云榜让世界看见蔡徐坤#                                                1
    爱你大帅哥                                                                                   1
    Name: raw_text, Length: 15942, dtype: int64




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
    <div id="974e693f57d34272a2167d7b92734044" style="width:600px;height:600px;"></div>


<script>
    require(['echarts'], function(echarts) {

var myChart_974e693f57d34272a2167d7b92734044 = echarts.init(document.getElementById('974e693f57d34272a2167d7b92734044'), 'light', {renderer: 'canvas'});

var option_974e693f57d34272a2167d7b92734044 = {
    "title": [
        {
            "text": "\u8521\u5f90\u5764\u771f\u7c89\u4e1dTop10\u8f6c\u53d1\u8bbe\u5907",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
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
    "series_id": 4856318,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "bar",
            "data": [
                66203.0,
                2849.0,
                2466.0,
                2415.0,
                2355.0,
                1540.0,
                1283.0,
                1267.0,
                1263.0,
                1179.0
            ],
            "stack": "stack_4856318",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": true,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
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
            "seriesId": 4856318
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
                "fontSize": 12
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "category",
            "splitLine": {
                "show": false
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 30,
                "margin": 8,
                "textStyle": {
                    "fontSize": 11
                }
            },
            "data": [
                "Android",
                "Flyme",
                "\u4e09\u661fGalaxy NOTE III",
                "\u4e09\u661fandroid\u667a\u80fd\u624b\u673a",
                "\u7ea2\u7c73Redmi",
                "vivo X20\u5168\u9762\u5c4f\u624b\u673a",
                "\u524d\u540e2000\u4e07 OPPO R11",
                "\u5c0f\u7c73\u624b\u673a",
                "\u8363\u8000\u624b\u673a \u52c7\u6562\u505a\u81ea\u5df1",
                "HUAWEI P10"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "boundaryGap": true,
            "type": "value",
            "splitLine": {
                "show": true
            },
            "axisLabel": {
                "interval": "auto",
                "formatter": "{value} ",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 14
                }
            }
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
myChart_974e693f57d34272a2167d7b92734044.setOption(option_974e693f57d34272a2167d7b92734044);

    });
</script>





```python
data_true['user.follow_count'].mean()
```




    18.125290976311106




```python
data_true['user.followers_count'].mean()
```




    13.066469748244362




```python
data_true.sample(5)['user.screen_name']
```




    49914            丨浮生尽
    64749    xingyp50S649
    69788         仔A9T194
    17689       Bambi-喜乐卉
    80887           吃客丶儿儿
    Name: user.screen_name, dtype: object




```python
data_true['user.screen_name'].str.contains('蔡|坤|葵|kun').sum()
```




    44918




```python
data_true.shape[0]
```




    102242




```python
# 绘制蔡徐坤真粉丝的简介词云图
import jieba
from collections import Counter
from pyecharts import WordCloud

jieba.add_word('蔡徐坤')

swords = [x.strip() for x in open ('stopwords.txt')]
```

    Building prefix dict from the default dictionary ...
    DEBUG:jieba:Building prefix dict from the default dictionary ...
    Loading model from cache C:\Users\小帆歌\AppData\Local\Temp\jieba.cache
    DEBUG:jieba:Loading model from cache C:\Users\小帆歌\AppData\Local\Temp\jieba.cache
    Loading model cost 0.731 seconds.
    DEBUG:jieba:Loading model cost 0.731 seconds.
    Prefix dict has been built successfully.
    DEBUG:jieba:Prefix dict has been built successfully.
    


    ---------------------------------------------------------------------------

    UnicodeDecodeError                        Traceback (most recent call last)

    <ipython-input-53-1b6d40e9f502> in <module>
          6 jieba.add_word('蔡徐坤')
          7 
    ----> 8 swords = [x.strip() for x in open ('stopwords.txt')]
    

    <ipython-input-53-1b6d40e9f502> in <listcomp>(.0)
          6 jieba.add_word('蔡徐坤')
          7 
    ----> 8 swords = [x.strip() for x in open ('stopwords.txt')]
    

    UnicodeDecodeError: 'gbk' codec can't decode byte 0x99 in position 2: illegal multibyte sequence



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



