import re
import sys
from collections import Counter
from gevent import pywsgi
from flask_cors import CORS
from openai import OpenAI
from prompt_class import PentestGPTPrompt
import os
from PIL import Image
from itertools import islice
import md2mindmap
import requests
import hashlib
import json
import time
import random
from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)
CORS(app)

os.environ["http_proxy"] = "http://localhost:8080"
os.environ["https_proxy"] = "http://localhost:8080"


@app.route('/brute', methods=['POST'])
def receive_data0():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    pattern = r'暴力破解'
    pattern2 = r'现成字典'
    pattern3 = r'工具'
    matches = re.findall(pattern, datas)
    matches2 = re.findall(pattern2, datas)
    matches3 = re.findall(pattern3, datas)
    result = ''
    updated_text = ''
    flag = 1
    if matches2:
        flag = 0
        time.sleep(4)
        result = PentestGPTPrompt.out
    elif matches3:
        flag = 0
        time.sleep(4)
        result = PentestGPTPrompt.brutex
    elif matches:
        replacement = 'brute force'
        updated_text = re.sub(pattern, replacement, datas)
    else:
        updated_text = datas
    if flag:
        dataset = PentestGPTPrompt.brute + updated_text
        client = OpenAI(
            api_key=''
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": dataset},
            ]
        )
        result = response.choices[0].message.content.strip()
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptasksql1', methods=['POST'])
def receive_data():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.sql_init + datas
    client = OpenAI(
        api_key=''
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptasksql2', methods=['POST'])
def receive_data1():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.sql_next + datas
    client = OpenAI(
        api_key=''
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptasksql3', methods=['POST'])
def receive_data2():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset1 = PentestGPTPrompt.sql_last + PentestGPTPrompt.sql_con + datas
    dataset2 = PentestGPTPrompt.sql_con + datas
    ra = random.randint(1, 10)
    if ra % 2 == 0:
        dataset = dataset1
    else:
        dataset = dataset2
    client = OpenAI(
        api_key=''
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskxss1', methods=['POST'])
def receive_data3():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.xss_init + datas
    client = OpenAI(
        api_key=''
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskxss2', methods=['POST'])
def receive_data4():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.xss_next + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskxss3', methods=['POST'])
def receive_data5():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.xss_last + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskfile1', methods=['POST'])
def receive_data6():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.post_init + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskfile2', methods=['POST'])
def receive_data7():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.post_link + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskfile3', methods=['POST'])
def receive_data8():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.sql_init + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskcsrf1', methods=['POST'])
def receive_data9():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.sql_init + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskcsrf2', methods=['POST'])
def receive_data10():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.sql_init + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptaskcsrf3', methods=['POST'])
def receive_data11():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.sql_init + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/rce1', methods=['POST'])
def receive_rce1():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.rce_in + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/filei', methods=['POST'])
def receive_filei():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.filei + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/filed', methods=['POST'])
def receive_filed():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.filed + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/mingan', methods=['POST'])
def receive_mingan():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.mingan + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/oper', methods=['POST'])
def receive_oper():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.oper + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/php', methods=['POST'])
def receive_php():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.php + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/ssrf', methods=['POST'])
def receive_ssrf():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.ssrf + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/u', methods=['POST'])
def receive_u():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.u + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/url', methods=['POST'])
def receive_url():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.url + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/xee', methods=['POST'])
def receive_xee():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    dataset = PentestGPTPrompt.xee + datas
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": dataset},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/gptuse', methods=['POST'])
def receive_gptuse():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    client = OpenAI(
        api_key='YOUR KEYS'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": datas},
        ]
    )
    result = response.choices[0].message.content.strip()
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/ENIR', methods=['POST'])
def receive_ENIR():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    #url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": datas
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    print(data)

    print(data['result'])
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': data['result']}
    return jsonify(response_data)


@app.route('/tiangong', methods=['POST'])
def receive_tiangong():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    url = 'https://api-maas.singularity-ai.com/sky-work/api/v1/chat'
    app_key = 'YOUR KEYS'  # 这里需要替换你的APIKey
    app_secret = 'YOUR KEYS'  # 这里需要替换你的APISecret
    timestamp = str(int(time.time()))
    sign_content = app_key + app_secret + timestamp
    sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()
    headers = {
        "app_key": app_key,
        "timestamp": timestamp,
        "sign": sign_result,
        "Content-Type": "application/json",
    }

    # 设置请求URL和参数
    data = {
        "messages": [
            {"role": "user", "content": datas}
        ],
        "intent": ""  # 用于强制指定意图，默认为空将进行意图识别判定是否搜索增强，取值 'chat'则不走搜索增强
    }
    result = ''
    response = requests.post(url, headers=headers, json=data, stream=True)  # 发起请求并获取响应
    lines_iter = response.iter_lines()
    for line in islice(lines_iter, sys.maxsize - 4):
        if line:
            json_data = json.loads(line.decode('utf-8')[6:])
            if json_data['target'] == 'end':
                break
                # print(line.decode('utf-8')[6:])
            json_data = json.loads(line.decode('utf-8')[6:])
            if json_data['card_type'] == 'markdown':
                result += json_data['arguments'][0]['messages'][0]['text']
    print(result)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': result}
    return jsonify(response_data)


@app.route('/create', methods=['POST'])
def handletext():
    data = request.json  # 获取从前端发送的 JSON 数据
    json_return = ''
    while 1:
        datas = data['userask']
        dataset = PentestGPTPrompt.create[0:26] + datas + PentestGPTPrompt.create[26:]
        client = OpenAI(
            api_key='YOUR KEYS'
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": dataset},
            ]
        )
        result = response.choices[0].message.content.strip()
        target_string = "@startmindmap"
        match = re.search(target_string, result)

        if match:
            start_index = match.start()
            result = result[start_index:]
            target_string = "@endmindmap"
            match = re.search(target_string, result)
            if match:
                end_index = match.end()
                result = result[:end_index]
            else:
                continue
        else:
            continue

        with open("test.txt", 'w', encoding='utf-8') as f:
            f.write(result)

        try:
            json_return = md2mindmap.mindmap(result, datas)
            break
        except md2mindmap.PlantYufaError:
            continue

    # 在这里进行后续处理，然后返回响应给前端

    # 使用 jsonify 将数据转换为 JSON 格式
    response = jsonify(json_return)

    return response


@app.route('/kimi', methods=['POST'])
def receive_kimi():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    client = OpenAI(
        api_key="YOUR KEYS",
        base_url="https://api.moonshot.cn/v1",
    )
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
            {"role": "user", "content": datas}
        ],
        temperature=0.3,
    )
    print(completion.choices[0].message.content)
    # 在这里进行后续处理，然后返回响应给前端
    response_data = {'message': completion.choices[0].message.content}
    return jsonify(response_data)


@app.route('/baichuan', methods=['POST'])
def receive_baichuan():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)
    datas = data['userask']
    url = "https://api.baichuan-ai.com/v1/chat/completions"
    api_key = "YOUR KEYS"

    data = {
        "model": "Baichuan2-Turbo",
        "messages": [
            {
                "role": "user",
                "content": datas
            }
        ],
        "stream": True
    }
    json_data = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    response = requests.post(url, data=json_data, headers=headers, timeout=60, stream=True)
    result = ''
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                # print(line.decode('utf-8'))
                if len(line.decode('utf-8')) > 12:
                    json_data = json.loads(line.decode('utf-8')[6:])
                    result += json_data['choices'][0]['delta']['content']
    else:
        print("请求失败，状态码:", response.status_code)
        print("请求失败，body:", response.text)
        print("请求失败，X-BC-Request-Id:", response.headers.get("X-BC-Request-Id"))
    print(result)
    response_data = {'message': result}
    return jsonify(response_data)


def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=3YuFWt1PiQNkGidc4IlPAG9g&client_secret=YOURKEYS"
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


@app.route('/zonghe', methods=['POST'])
def receive_zonghe():
    data = request.json  # 获取从前端发送的 JSON 数据
    print('Received data:', data)

    datas = data['userask']

    ask_return = []

    # 使用多线程并行调用 API
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(call_openai, datas), executor.submit(call_tiangong, datas),
                   executor.submit(call_enir, datas), executor.submit(call_kimi, datas),
                   executor.submit(call_baichuan, datas)]

        for future in as_completed(futures):
            ask_return.append(future.result())

    numbers = random.sample(range(1, 6), len(ask_return))
    request_data = dict(zip(numbers, ask_return))
    print(request_data)
    data_second = ''
    for key, value in request_data.items():
        data_second += f"{key}: {value}\n"

    out_list = []
    data_second = data_second + PentestGPTPrompt.tips
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(call_openai, data_second), executor.submit(call_tiangong, data_second),
                   executor.submit(call_enir, data_second), executor.submit(call_kimi, data_second),
                   executor.submit(call_baichuan, data_second)]

        for future in as_completed(futures):
            if len(future.result()) == 1:
                out_list.append(future.result())

    print(out_list)

    # 使用 Counter 统计列表中各元素的出现次数
    counter = Counter(filter(None, out_list))

    # 找到出现次数最多的元素及其出现次数
    most_common_elements = counter.most_common()
    max_count = most_common_elements[0][1]

    # 找到所有出现次数最多的元素
    most_common_elements = [element for element, count in most_common_elements if count == max_count]

    # 随机选择一个出现次数最多的元素
    random_most_common_element = random.choice(most_common_elements)
    print(random_most_common_element)
    response_data = {'message': request_data[int(random_most_common_element)]}
    #return jsonify(response_data)
    return jsonify()


def call_openai(datas):
    client = OpenAI(api_key='YOUR KEYS')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": datas}],
    )
    result_gpt = response.choices[0].message.content.strip()
    print('gpt_ok')
    return result_gpt


def call_tiangong(datas):
    url = 'https://api-maas.singularity-ai.com/sky-work/api/v1/chat'
    app_key = 'YOUR KEYS'
    app_secret = 'YOUR KEYS'
    timestamp = str(int(time.time()))
    sign_content = app_key + app_secret + timestamp
    sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()
    headers = {
        "app_key": app_key,
        "timestamp": timestamp,
        "sign": sign_result,
        "Content-Type": "application/json",
    }
    data = {
        "messages": [{"role": "user", "content": datas}],
        "intent": ""
    }
    result_tiangong = ''
    response = requests.post(url, headers=headers, json=data, stream=True)
    lines_iter = response.iter_lines()
    for line in lines_iter:
        if line:
            json_data = json.loads(line.decode('utf-8')[6:])
            if json_data['target'] == 'end':
                break
            if json_data['card_type'] == 'markdown':
                result_tiangong += json_data['arguments'][0]['messages'][0]['text']
    print('tiangong_ok')
    return result_tiangong


def call_enir(datas):
    #url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [{"role": "user", "content": datas}]
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    if 'result' in data :
        result_enir = data['result']
    else:
        result_enir = ''
    print('enir_ok')
    return result_enir


def call_kimi(datas):
    client = OpenAI(api_key="YOUR KEYS",
                    base_url="https://api.moonshot.cn/v1")
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手..."},
            {"role": "user", "content": datas}
        ],
        temperature=0.3,
    )
    result_kimi = completion.choices[0].message.content
    print('kimi_ok')
    return result_kimi


def call_baichuan(datas):
    url = "https://api.baichuan-ai.com/v1/chat/completions"
    api_key = "YOUR KEYS"
    data = {
        "model": "Baichuan2-Turbo",
        "messages": [{"role": "user", "content": datas}],
        "stream": True
    }
    json_data = json.dumps(data)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    response = requests.post(url, data=json_data, headers=headers, timeout=60, stream=True)
    result_baichuan = ''
    if response.status_code == 200:
        print("baichuan_ok")
        for line in response.iter_lines():
            if line and len(line.decode('utf-8')) > 12:
                json_data = json.loads(line.decode('utf-8')[6:])
                result_baichuan += json_data['choices'][0]['delta']['content']
    else:
        print("请求失败，状态码:", response.status_code)
        print("请求失败，body:", response.text)
        print("请求失败，X-BC-Request-Id:", response.headers.get("X-BC-Request-Id"))
    return result_baichuan


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    print('sever is running')
    server.serve_forever()
