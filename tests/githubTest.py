import unittest
import os

from src.justauth.request.AuthGithubRequest import AuthGithubRequest


class GithubAuthTest(unittest.TestCase):
    def test_getUserInfo(self):
        driver = AuthGithubRequest('github', os.path.dirname(os.path.abspath(__file__)) + '/auth.ini').getUserInfo()
        self.assertEqual('github', driver)

    def test_authorize(self):
        authorize_url = AuthGithubRequest('github',
                                          os.path.dirname(os.path.abspath(__file__)) + '/auth.ini').authorize()
        self.assertIn('github', authorize_url)


if __name__ == '__main__':
    unittest.main()
