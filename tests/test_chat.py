# tests/test_chat.py
import unittest
from chaty.chat import ChatGPT
import config

class TestChatGPT(unittest.TestCase):
    def setUp(self):
        self.api_key = config.OPENAI_API_KEY
        self.chatgpt = ChatGPT(self.api_key)

    def test_generate_response(self):
        prompt = "Tell me a joke about programming."
        response = self.chatgpt.generate_response(prompt)
        print(response)
        self.assertTrue(len(response) > 0)

if __name__ == '__main__':
    unittest.main()
