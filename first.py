import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(5, 2) / [20, 50] + [22.8, 108.2],
    columns=['latitude', 'longitude'])

df.index.name='序号'

st.subheader('南宁餐厅经度纬度')
st.dataframe(df[1:6])

st.subheader('在南宁地图上随机画点')
st.map(df)


st.subheader('🛎️餐厅评分')

data ={

      '餐厅':['阿常炒粉', '阿杰煮粉', '小李桂林米粉','福记老友粉','玉林牛巴粉'],
       '评分':[4.5,2.4,3.9,4.8,5.0]
}
chifan=pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4 ,5 ], name='序号')
df.index = index
st.write(chifan)
st.bar_chart(chifan, x='餐厅')
st.header("不同类型餐厅价格")
data={
        '月份':['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'],
        '阿常炒粉':[8.0,8.5,8.0,9.5,9.0,8.0,8.5,7.5,8.0,9.0,10.0,9.5],
        '阿杰煮粉':[9.0,9.5,9.0,9.5,10.0,9.5,9.0,8.5,9.0,9.5,9.5,9.0],
        '小李桂林米粉':[5.0,5.5,6.0,5.0,5.5,5.0,6.0,5.0,5.0,5.0,5.5,5.0],
        '福记老友粉':[9.0,9.0,9.0,9.0,9.0,9.0,9.0,9.0,9.0,9.0,9.0,9.0],
        '玉林牛巴粉':[8.5,8.5,8.5,8.0,8.0,8.0,8.0,8.0,8.0,8.5,8.0,8.5]
}
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4, 5,6,7,8,9,10,11,12], name='序号')
df.index = index
st.write(df)
st.line_chart(df, x='月份')

st.header("用餐高峰时段")
data2={
        '时间':['11点','12点','13点','14点','15点','16点','17点','18点','19点'],
        '阿常炒粉':[118.0,128.0,108.0,109.0,119.0,128.0,138.0,127.0,118.0],
        '阿杰煮粉':[91.0,95.0,91.0,95.0,100.0,95.0,90.0,85.0,90.0],
        '小李桂林米粉':[50.0,55.0,60.0,50.0,55.0,50.0,60.0,50.0,50.0],
        '福记老友粉':[90.0,90.0,90.0,99.0,90.0,99.0,90.0,95.0,90.0],
        '玉林牛巴粉':[85.0,85.0,85.0,80.0,80.0,80.0,80.0,80.0,80.0,]
}
df2 = pd.DataFrame(data2)
index = pd.Series([1, 2, 3, 4, 5,6,7,8,9], name='序号')
df2.index = index
st.write(df)
st.area_chart(df2, x='时间')


import streamlit as st
# 自定义format_func函数
def my_format_func(option):
    return f'{option}'

st.header('选择餐厅')
canting = st.selectbox('选择餐厅查看详情：', ['阿常炒粉', '福记老友粉', '阿杰煮粉','小李桂林米粉','玉林牛巴粉'], format_func=my_format_func, index=2)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
if canting == '阿常炒粉':
    st.subheader('阿常炒粉')
    st.metric(label="评分", value="4.8/5.0")
    st.metric(label="人均消费", value="10元")
    st.subheader('推荐菜品:')
    st.write('蛋炒粉')
    st.write('肉蛋炒粉')
    st.write('火腿炒粉')
    
elif canting == '福记老友粉':
    st.subheader('福记老友粉')
    st.metric(label="评分", value="4.5/5.0")
    st.metric(label="人均消费", value="10元")
    st.subheader('推荐菜品:')
    st.write('老友粉')
    st.write('干锅老友粉')
    st.write('爆炒老友粉')
elif canting == '阿杰煮粉':
    st.subheader('阿杰煮粉')
    st.metric(label="评分", value="4.0/5.0")
    st.metric(label="人均消费", value="9元")
    st.subheader('推荐菜品:')
    st.write('招牌牛巴粉')
    st.write('招牌牛腩粉')
    st.write('招牌牛杂粉')
elif canting == '小李桂林米粉':
    st.subheader('小李桂林米粉')
    st.metric(label="评分", value="4.5/5.0")
    st.metric(label="人均消费", value="7元")
    st.subheader('推荐菜品:')
    st.write('金牌套餐')
    st.write('省钱套餐')
    st.write('畅饮套餐')
else:
    st.subheader('玉林牛巴粉')
    st.metric(label="评分", value="4.6/5.0")
    st.metric(label="人均消费", value="10元")
    st.subheader('推荐菜品:')
    st.write('超多牛巴粉')
    st.write('牛巴粉')
    st.write('干拌牛巴粉')
import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st
import time
st.subheader(''' 当前拥挤程度''')
st.progress(94,text='当前拥挤程度')
st.header("今日午餐推荐")

st.title('😍今日推荐')
st.markdown("<span style='color:red; border:2px solid red; border-radius:8px; padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)

# 初始化会话状态
if 'count' not in st.session_state:
    st.session_state.count = 0

count = 0;
if st.button(' :red[今天吃什么]'):
   st.session_state.count += 1
if st.session_state.count % 6 == 1:
   st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：阿常炒粉</span>",    unsafe_allow_html=True)
   st.markdown("![阿常炒粉](https://th.bing.com/th/id/R.2398b8a3a20d9b68fc8fad66a3541b14?rik=IZQyf5hf%2buBfqg&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn01%2f244%2fw640h404%2f20180412%2f81d6-fyzeyqa7634568.jpg&ehk=XOJvZUJRXrfgZA5M%2f2ZEOK2vtuOfHXduvZmwcZyP%2bns%3d&risl=&pid=ImgRaw&r=0)")
if st.session_state.count % 6 == 2:
   st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：福记老友粉</span>",    unsafe_allow_html=True)
   st.markdown("![福记老友粉](https://th.bing.com/th/id/OIP.yPIc2hxDDdsXYGfnml7cYwHaHa?rs=1&pid=ImgDetMain)")
if st.session_state.count % 6 == 3:
   st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：阿杰煮粉</span>",    unsafe_allow_html=True)
   st.markdown("![图片](https://www.bing.com/th/id/OSK.da871e49064cee649e936ae556c95d9d?w=300&h=200&c=7&rs=1&qlt=80&o=6&cdv=1&pid=16.1)")
if st.session_state.count % 6 == 4:
   st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：小李桂林米粉</span>",    unsafe_allow_html=True)
   st.markdown("![图片](https://th.bing.com/th/id/R.5289aef1bf3e1ce904065ad42375abc0?rik=yi%2bRwPX2aV9Kug&riu=http%3a%2f%2fpic.ntimg.cn%2f20130114%2f11367899_174222154000_2.jpg&ehk=IC%2bD78FQoFPotQXY27k9RP31coDCMbLui5bVwAnChoA%3d&risl=&pid=ImgRaw&r=0)")
if st.session_state.count % 6 == 5:
   st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：玉林牛巴粉</span>",    unsafe_allow_html=True)
   st.markdown("![图片](https://th.bing.com/th/id/OIP.7HSIpHfu2_ZKfg9GDMDmVwHaFC?rs=1&pid=ImgDetMain)")


    