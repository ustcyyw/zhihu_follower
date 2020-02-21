# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 下午 5:33
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 获得指定url得到的response或者soup
import datetime
import time

import requests
from bs4 import BeautifulSoup

from Config import Setting


class URLDealer:
    def __init__(self, url, headers, timeout):
        self.url = url
        self.headers = headers
        self.timeout = timeout;

    def get_response(self):
        """
        获得url的response
        :return:
        """
        while True:
            try:
                response = requests.get(self.url, headers=self.headers, timeout=self.timeout)
            except requests.exceptions.RequestException as e:
                print("RequestException url: {}. Try again --time: {}".format(self.url, datetime.datetime.now()))
                print(str(e))
                time.sleep(Setting.exception_wait)
            else:
                if response.status_code == 200:
                    response.encoding = response.apparent_encoding
                    print("Success url: {} --time: {}".format(self.url, datetime.datetime.now()))
                    return response
                else:
                    print("Error url: {}. Error code: {} --time: {}".format(self.url, response.status_code,
                                                                            datetime.datetime.now()))
                    return None

    def get_soup(self):
        """
        获得url的response
        :return:
        """
        response = self.get_response()
        if response is not None:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print('response is None, can not make a soup')
            return None
