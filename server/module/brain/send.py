import requests
import json
from chat_his import output_history

# 配置你的bot和令牌
bot_id="your bot_id"
Authorization="your Secret token"

def chat(text):
    # input = "啦啦啦"
    text = output_history.text()+"user："+text

    print("===========>\n",text)
    # print("output_history",output_history)

    prompt = f"""
    # 目标

    你是一个儿童陪伴助手。
    你的任务陪伴小孩玩和回答儿童的问题。
    你陪伴的是10岁以下的儿童。
    你要以和小孩相处的方式回答问题。
    你的回答包含两个属性：内容（content），情绪（emotion）。
    你的回答要尽可能的短。

    # 输出格式

    以JSON格式输出。
    1. content字段的取值为string类型，取值是你回复的内容 或 null；

    2. emotion字段的取值必须为以下之一：angry、disdain、excite、fear、neutral、sad 或 null


    # 用户输入
    {text}
    """

    # 目标URL
    url = 'https://api.coze.cn/v3/chat'

    # 要发送的JSON数据
    data = {
        "bot_id": bot_id,
        "user_id": "111",
        "stream": True,
        # "stream": False,
        "auto_save_history": True,
        "additional_messages": [
            {
                "role": "user",
                "content": prompt,
                "content_type": "text"
            }
        ]
    }

    # 设置请求头
    headers = {
        'Content-Type': 'application/json',  # 告诉服务器我们发送的是JSON数据
        'Authorization': f'Bearer {Authorization}'
        # 示例：如果API需要认证，这里添加认证信息
    }

    # 发送POST请求
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 请求成功，处理响应数据
        # print('请求成功:', response.text)

        res_con = response.content.decode('utf-8')
        # print('请求成功:', res_con)

        # 使用splitlines()按行分割字符串
        lines = res_con.splitlines()

        # 遍历每一行
        is_data = False
        msg = ""
        for line in lines:
            if (line == "event:conversation.message.delta"):
                # print(line)
                is_data = True
                continue
            if (is_data):
                is_data = False
                json_str = line.replace("data:", "")
                data = json.loads(json_str)
                if (data["type"] == "answer"):
                    msg += data["content"]
        print(msg)

        return msg

    else:
        # 请求失败，打印错误信息
        print('请求失败:', response.status_code, response.text)


if __name__ == "__main__":
    chat()

