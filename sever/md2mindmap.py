from plantuml import PlantUML
import os
import plantuml
from PIL import Image
import re
import numpy as np
import io
import json


# 定义一个自定义错误类
class PlantYufaError(Exception):
    def __init__(self, message="语法错误"):
        self.message = message
        super().__init__(self.message)


def get_image_size2(image_path):
    try:
        with Image.open(image_path) as img:
            return img.size
    except FileNotFoundError:
        return False


def find_matching_files(directory, pat):
    matching_files = []

    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 使用正则表达式匹配文件名
            if re.match(pat, file):
                matching_files.append(os.path.join(root, file))

    return matching_files


def mindmap(resu, position, is_root_only=1):
    uml_code = resu.split('\n')

    uml = PlantUML('http://www.plantuml.com/plantuml/img/')

    #见REAMADE.md
    try:
        img = uml.processes(resu)

        with open("png/" + position + ".png", 'wb') as f:
            f.write(img)
    except:
        raise PlantYufaError()

    result = []
    no_second = 0
    no_third = 0
    no_root = 0
    no_forth = 0

    for i in uml_code:
        if len(i) == 0:
            continue
        if i[0] == "@" :
            continue
        if i[0] == "+":
            raise PlantYufaError()
        if i[0] == "-":
            raise PlantYufaError()

        if i[3] == "*":
            no_forth = no_forth + 1
            result.append(forth_node(no_forth, no_third, no_second, i))
            continue
        if i[2] == "*":
            no_third = no_third + 1
            result.append(third_node(no_third, no_second, i))
            no_forth = 0
            #print(i)
            continue
        if i[1] == "*":
            no_second = no_second + 1
            result.append(second_node(no_second, i))
            no_third = 0
            #print(i)
            continue
        if i[0] == "*":
            no_root = no_root + 1
            if no_root == 1:
                result.append(root_node(i))
            else:
                raise PlantYufaError()
            #print(i)
            continue

    # with open("txt/" + position + ".txt", 'w', encoding='utf-8') as f:
    #     f.write(result)

    return result


def forth_node(id, parentid, garndpaid, topic):
    topic = topic[5:]
    while topic[0] == " " or topic[0] == "*":
        topic = topic[1:]
    id = "forth" + str(garndpaid) + "." + str(parentid) + "." + str(id)
    parentid = "third" + str(garndpaid) + "." + str(parentid)
    data = {
        "id": id,
        "parentid": parentid,
        "topic": topic
    }
    return data

def third_node(id, parentid, topic):
    topic = topic[4:]
    id = "third" + str(parentid) + "." + str(id)
    parentid = "second" + str(parentid)

    data = {
               "id": id,
               "parentid": parentid,
               "topic": topic
    }


    return data


def second_node(id, topic):
    topic = topic[3:]
    id = "second" + str(id)

    data = {
               "id": id,
               "parentid": "root",
               "topic": topic,
               "direction": "left"
    }


    return data


def root_node(topic):
    topic = topic[2:]

    data = {
        "id": "root",
        "isroot": True,
        "topic": topic
    }


    return data


if __name__ == '__main__':
    result = """@startmindmap
* 思维导图使用说明
** 基本功能
*** 保存：保存为.jm文件
*** 下载：下载为图片
*** 右键：编辑、删除、添加节点
** 上传导图
*** 1.点击上传选择jm文件
*** 2.再点击打开文件
** GPT问询
*** 在右上角输入想要生成思维导图的关键词
@endmindmap"""
    try:
        mindmap(result, "map")
    except PlantYufaError as e:
        print("error")
