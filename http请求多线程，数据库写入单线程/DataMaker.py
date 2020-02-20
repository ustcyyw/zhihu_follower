# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 下午 5:52
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 数据处理类

import json
from Config import Setting

class DataParser:
    """对一个url中的follower的信息提取"""

    @classmethod
    def json_to_python(cls, data):
        """
        将str形式的数据通过json模块转换为python对象
        :param data: 关注者url得到的数据
        :return:
        """
        if isinstance(data, str):
            return json.loads(data)
        else:
            return data

    def __init__(self, data, followers_queue):
        self.data = self.json_to_python(data)
        self.followers_queue = followers_queue

    def parse_follower_data(self):
        """
        获得关注者数据列表：包括名字 主页url 简介 性别 粉丝数 回答数 文章数 徽章数量 及简单判断是否为假粉
        :return: 提取后的关注者数据列表
        """
        if self.data is None:
            return
        followers = self.data.get('data')
        for follower in followers:
            _dict = {}
            _dict['name'] = follower['name'].replace("'", "*")
            _dict['page_url'] = Setting.page_url_pattern.format(follower['url_token'])
            _dict['headline'] = follower['headline'] if follower['headline'] != '' else 'null'
            _dict['gender'] = follower['gender']
            _dict['follower_count'] = follower['follower_count']
            _dict['answer_count'] = follower['answer_count']
            _dict['articles_count'] = follower['articles_count']
            _dict['badge_count'] = len(follower['badge'])
            if (_dict['follower_count'] == 0 and _dict['answer_count'] == 0
                    and _dict['articles_count'] == 0 and _dict['badge_count'] == 0
                    and _dict['headline'] == 'null'):
                _dict['is_fake'] = 1
            else:
                _dict['is_fake'] = 0

            self.followers_queue.put(_dict)
