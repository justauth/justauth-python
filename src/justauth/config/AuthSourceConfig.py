# -*-coding: utf-8-*-
import operator

from src.justauth.exception.AuthException import AuthException


class AuthSource:
    __slots__ = ('authorize', 'accessToken', 'userInfo')

    def __init__(self, d):
        for i in self.__slots__:
            setattr(self, i, d[i] if i in d else None)


class AuthSourceConfig:

    def __init__(self, driver):
        if hasattr(self, driver):
            self.config = operator.methodcaller(driver)(self)
        else:
            raise AuthException()

    @staticmethod
    def github():
        return AuthSource({
            'authorize': 'https://github.com/login/oauth/authorize',
            'accessToken': 'https://github.com/login/oauth/access_token',
            'userInfo': 'https://api.github.com/user/repos',
        })
