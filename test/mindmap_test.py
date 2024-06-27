import unittest
from io import StringIO
from unittest.mock import patch
from tempfile import TemporaryDirectory
from sever.md2mindmap import *

class TestMindMap(unittest.TestCase):

    def test_mindmap_test(self):
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
        result = result.replace("* 基本功能", "+ 基本功能")  # 引发语法错误
        try:
            output = mindmap(result, "example.jm", 1)
            self.fail("Mindmap function did not raise PlantYufaError for syntax error!")
        except PlantYufaError as e:
            self.assertEqual(str(e), "语法错误")

    def test_get_image_size2_non_existing_file(self):
        image_path = "non_existing_image.png"  # 一个不存在的文件路径
        size = get_image_size2(image_path)
        self.assertFalse(size)

    def test_find_matching_files(self):
        directory = "."  # 当前目录
        pattern = r".*\.py$"  # 匹配所有.py文件
        matching_files = find_matching_files(directory, pattern)
        self.assertTrue(all(file.endswith('.py') for file in matching_files))

if __name__ == '__main__':
    unittest.main()
