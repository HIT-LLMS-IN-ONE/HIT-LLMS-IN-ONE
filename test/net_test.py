import unittest
import requests
import json

class TestFlaskApp(unittest.TestCase):

    base_url = 'http://localhost:5001'  # Replace with your Flask app's base URL

    def test_gptuse_endpoint(self):
        url = f'{self.base_url}/gptuse'
        data = {'userask': 'Can you help me with a math problem?'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_ENIR_endpoint(self):
        url = f'{self.base_url}/ENIR'
        data = {'userask': 'How is the weather today?'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_tiangong_endpoint(self):
        url = f'{self.base_url}/tiangong'
        data = {'userask': 'Tell me a joke.'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_kimi_endpoint(self):
        url = f'{self.base_url}/kimi'
        data = {'userask': 'What is the capital of France?'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_baichuan_endpoint(self):
        url = f'{self.base_url}/baichuan'
        data = {'userask': 'Translate hello to Chinese.'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_zonghe_endpoint(self):
        url = f'{self.base_url}/zonghe'
        data = {'userask': 'How does photosynthesis work?'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_zuiyou_endpoint(self):
        url = f'{self.base_url}/zuiyou'
        data = {'userask': 'Tell me something interesting.'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())


if __name__ == '__main__':
    unittest.main()
