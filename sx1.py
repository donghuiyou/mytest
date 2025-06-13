import streamlit as st
import cloudinary
import cloudinary.uploader
import datetime
import streamlit as st
# 页面配置
st.set_page_config(page_title="简历生成器", layout="wide")
st.title("📄个人简历生成器")
c1, c2 = st.columns([1,2])
with c1:
    st.header("填写个人信息")
    st.markdown(
        """
        <hr style="height:3px;border:none;background:linear-gradient(90deg, #1E90FF, #4169E1);border-radius:3px;margin:15px 0">
        """,
        unsafe_allow_html=True)
    name = st.text_input("姓名", "")
    job = st.text_input("职位", value="软件测试")
    phone = st.text_input("电话", "")
    email = st.text_input("邮箱", "")
    birthday = st.date_input("出生日期")
    gender = st.radio("性别", ["男", "女"])
    edu = st.selectbox("学历", ["本科", "硕士", "博士", "其他"])
    def my_format_func(option):
        return f'{option}'
    xueli = st.selectbox('学历:',['小学', '初中', '高中','本科','研究生','博士'],format_func=my_format_func, index=2)

    yuyan = st.multiselect('语言能力',
        ['中文', '英语', '法语','日语','韩语','德语','葡萄牙语','西班牙语'],
        format_func=my_format_func,)
    
    jineng = st.multiselect(
        '技能(可多选)',
        ['java', 'python', 'APS','机器学习','HTML/CSS','SQL','C','C++','C#'],
        format_func=my_format_func,)

    from datetime import datetime, time

    jingyan = st.slider('工作经验(年)', 0, 40, 0)
    st.write("工作经验 ", jingyan, '年')
    
    values = st.slider(
        '期望薪资(元)',
        2000, 10000, (5000, 7000))
    st.write("期望薪资 ", values, '元')
    
    grjl = st.text_area(label='个人简历：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
 
    time = st.number_input("每日最佳联系时间段")
    st.write('最佳联系时间段为：', time)

    st.text('上传个人资料')
    uploaded_file=st.file_uploader(
        "上传个人照片",
        type=['jpg','jpeg','png'])
    with c2:
        st.header('简历实时预览')
        st.markdown(
            """
            <hr style="height:3px;border:none;background:linear-gradient(90deg, #1E90FF, #4169E1);border-radius:3px;margin:15px 0">
            """,
            unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        with c3:
            if uploaded_file:
                st.image(uploaded_file)
            st.write(f'职位:{job}')
            st.write(f'电话:{phone}')
            st.write(f'邮箱:{email}')
            st.write(f'出生日期:{birthday}')
        with c4:
            st.write(f'性别:{gender}')
            st.write(f'学历:{edu}')
            st.write(f'工作经验:{jingyan}')
            st.write(f'期望薪资:{jingyan}')
            st.write(f'最佳联系时间:{time}')
            st.write(f'语言能力:{yuyan}')
        st.markdown('***')
        st.write(f'个人简历:{grjl}')
        st.markdown('***')
    