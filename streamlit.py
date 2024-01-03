import streamlit as st
import os
from appbuilder import Message, Playground

# 设置环境变量
os.environ['APPBUILDER_TOKEN'] = 'put token here'

# Streamlit 页面布局
st.title('商品信息查询')
st.write('请输入商品名，获取商品信息')

# 用户输入商品名
product_name = st.text_input('商品名', '特斯拉Model Y')

if st.button('获取商品信息'):
    # 输入到大模型中的prompt的模板
    prompt_template = \
    '''输入商品名，我需要你为我生成该商品的商品信息。

    要求：
    - 你生成的商品信息应该包含多方面信息。

    商品名：{product_name}
    商品信息：
    '''
    # 创建商品信息生成组件
    product_information_generation = Playground(prompt_template=prompt_template, model='ernie-bot-4')

    # 填充prompt_template参数的参数映射表
    prompt_template_kwargs = {
        'product_name': product_name
    }

    # 获取商品信息
    response = product_information_generation(Message(prompt_template_kwargs), stream=False, temperature=0.5)
    product_information = response.content

    # 展示商品信息
    st.write('商品信息：')
    st.text(product_information)

# 如果你想要应用有更多功能，可以在这里添加
