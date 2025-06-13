import streamlit as st

st.title("学生 小铠——学生档案")
st.header("🔑基础信息")
st.markdown('学生ID：NEO-2023-001')
st.markdown('注册时间: :green[2023-10-01 08:30:17]   | 精神状态:✅正常 ')
st.markdown('当前教室: :green[实训楼301]   | 安全等级: :green[绝密] ')

st.subheader('技能矩阵')
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言", value="95%",delta="2%")
c2.metric(label="python", value="87%", delta="-1%")
c3.metric(label="java", value="1500", delta="-10%")

import streamlit as st
import time
st.subheader(''' Streamlit课程进度''')
st.progress(50,text='Streamlit课程进度')
st.header(''' 📝任务日志''')
import pandas as pd   
import streamlit as st  

data={
        '日期':['2025-06-01','2025-06-02','2023-06-03'],
        '任务':['学生数字档案','课程管理系统','数据图表展示'],
        '状态':['✅完成','�进行中','❌未完成'],
        '难度':['★★☆☆☆','★☆☆☆☆','★★★☆☆'],
}
index = pd.Series(['0', '1', '2'], name='序号')
df = pd.DataFrame(data, index=index)
st.dataframe(df)

st.header("💻 最新代码成果")
# 创建要显示的Python代码块的内容
python_code = '''def camera_process():
    with TrtYOLO(lite):
        trt.detect_when_openrtty()
        expGoto()
        return ACCESS_GRANTED
    status, evade!")
'''
st.code(python_code)


st.markdown(':green[`>>SYSTEM MESSAGE:`]下一个任务目标已解锁')