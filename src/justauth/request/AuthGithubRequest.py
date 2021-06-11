# -*-coding: utf-8-*-
import string

from src.justauth.config.AuthSourceConfig import AuthSourceConfig
from src.justauth.request.AuthRequest import AuthRequest
from selenium import webdriver

class AuthGithubRequest(AuthRequest):
    def __init__(self, driver, config_path) -> object:
        self.driver = driver
        self.source_config = AuthSourceConfig(driver).config
        self.config = AuthRequest.getConfig(config_path, self.driver)

    def authorize(self):
        auth_url = self.source_config.authorize
        return auth_url + '?' + 'client_id=' + self.config['client_id'] + '&redirect_uri=' + self.config['redirect_uri']

    def getUserInfo(self):
        return self.driver

    def getAccessToken(self):
        return self.driver

