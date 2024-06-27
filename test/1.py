import unittest
import requests
import json
import unittest
import requests
import json

class TestFlaskAppEndpoints(unittest.TestCase):
    base_url = 'http://localhost:5001'  # 根据实际情况调整

    def test_brute_with_valid_input(self):
        url = f'{self.base_url}/brute'
        data = {'userask': '需要暴力破解的信息'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_brute_with_invalid_input(self):
        url = f'{self.base_url}/brute'
        data = {'userask': ''}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_gptasksql1_with_valid_data(self):
        url = f'{self.base_url}/gptasksql1'
        data = {'userask': 'SELECT * FROM users'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_gptasksql1_with_sql_injection(self):
        url = f'{self.base_url}/gptasksql1'
        data = {'userask': "1; DROP TABLE users"}  # Dangerous input, assuming your API handles it safely
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)  # Ensure the system handles this safely

    def test_gptaskxss_with_xss_attack(self):
        url = f'{self.base_url}/gptaskxss1'
        data = {'userask': '<script>alert("XSS")</script>'}  # XSS input to test handling
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<script>', response.json().get('message', ''))

    def test_file_handling_with_valid_file(self):
        url = f'{self.base_url}/filed'
        data = {'userask': 'filename.txt'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    # 测试没有找到文件的情况
    def test_file_handling_with_missing_file(self):
        url = f'{self.base_url}/filed'
        data = {'userask': 'non_existent_file.txt'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)



class TestAdvancedFlaskAppEndpoints(unittest.TestCase):
    base_url = 'http://localhost:5001'  # 根据实际情况调整

    def test_gptaskcsrf_with_valid_data(self):
        url = f'{self.base_url}/gptaskcsrf1'
        data = {'userask': 'What is CSRF?'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_gptaskcsrf_with_invalid_input(self):
        url = f'{self.base_url}/gptaskcsrf1'
        data = {}  # Empty data
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertNotEqual(response.status_code, 200)

    def test_random_behavior_endpoint(self):
        url = f'{self.base_url}/gptasksql3'
        data = {'userask': 'Please explain the use of indexes in databases.'}
        headers = {'Content-Type': 'application/json'}
        responses = [requests.post(url, json=data, headers=headers).json() for _ in range(10)]
        # Check for consistent handling or proper random behavior
        message_variety = len(set([response['message'] for response in responses if 'message' in response]))
        self.assertTrue(message_variety > 1, "Expected variability in responses due to random logic.")

    def test_external_api_integration(self):
        url = f'{self.base_url}/ENIR'
        data = {'userask': 'Tell me about the latest tech trends.'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_long_running_process(self):
        url = f'{self.base_url}/tiangong'
        data = {'userask': 'What is the future of AI?'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_create_endpoint_with_invalid_mindmap(self):
        url = f'{self.base_url}/create'
        data = {'userask': 'Invalid input that should not generate a mindmap.'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

class TestIntegrationAndEdgeCases(unittest.TestCase):
    base_url = 'http://localhost:5001'  # 根据实际情况调整

    def test_error_handling_for_nonexistent_user(self):
        # 测试不存在的用户错误处理
        auth_url = f'{self.base_url}/authenticate'
        data = {'username': 'nonexistent', 'hash2Hex': 'fake_hash', 'auth_code': 'fake_code'}
        response = requests.post(auth_url, json=data)
        self.assertEqual(response.status_code, 500)

    def test_zuiyou_with_valid_input(self):
        url = f'{self.base_url}/zuiyou'
        data = {'userask': 'Provide a summary of AI advancements.'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_kimi_with_culture_sensitive_query(self):
        url = f'{self.base_url}/kimi'
        data = {'userask': 'Tell me about cultural events in China.'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_baichuan_with_multilingual_input(self):
        url = f'{self.base_url}/baichuan'
        data = {'userask': '¿Cómo están las tendencias tecnológicas actuales?'}  # Spanish input
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

# 如果是独立运行这个测试模块
if __name__ == '__main__':
    unittest.main()
