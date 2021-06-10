# -*-coding: utf-8-*-
import abc
import os.path
import configparser

from src.justauth.exception.AuthException import AuthException


class AuthRequest(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def authorize(self):
        pass

    @abc.abstractmethod
    def getAccessToken(self):
        pass

    @abc.abstractmethod
    def getUserInfo(self):
        pass

    @staticmethod
    def getConfig(config_path, driver):
        config = configparser.ConfigParser()
        if os.path.exists(config_path):
            config.read(config_path)
            if driver not in config.sections():
                raise AuthException()
            return config[driver]
        else:
            raise AuthException()
