import os
from appbuilder import Message, Playground

# 设置环境变量
os.environ['APPBUILDER_TOKEN'] = 'bce-v3/ALTAK-5UDvwPuPdcyo9jLaJ5GT9/d23842dc0b335b51be49a0335449c6e72f271ded'

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

# 获取商品信息
# 填充prompt_template参数的参数映射表，需要与prompt_template对应
prompt_template_kwargs = {
    'product_name': '特斯拉Model Y'
}
response = product_information_generation(Message(prompt_template_kwargs), stream=False, temperature=0.5)
product_information = response.content
print(f'商品信息：\n{product_information}')
